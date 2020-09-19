import bs4
from yaml import load, dump, Loader, Dumper
import asyncio
import re
import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from meta import *

SCROLL_PAUSE_TIME = 2

cap = webdriver.common.desired_capabilities.DesiredCapabilities().FIREFOX
cap["marionette"] = False

options = Options()
options.log.level = "trace"
# options.add_argument('--headless')

BROWSER_BINARY_PATH = '/usr/bin/firefox'
DRIVER_BINARY_PATH = '/usr/local/bin/geckodriver'
BROWSER_CONFIG = {"capabilities": cap,
                  "executable_path": DRIVER_BINARY_PATH,
                  "firefox_binary": FirefoxBinary(BROWSER_BINARY_PATH),
                  "options": options}

META_DATA = "meta.yml"
USER_AGENT = "headers.yml"
KATA_DATA = None
KATA_TYPE = ("completed", "authored", "unfinished")


def sync_kata_type(data, t):
    url = data["codewars"]["url"] + "/users/" + data["user"]["name"] + "/" + t
    soup = get_page_source(url)
    data["user"]["kata"][t] = [{"href": kata.find("a").get("href").split("/")[-1],
                                "text": re.sub(r"[^\w+]", " ", kata.find("a").text),
                                "level": int(kata.find("span").text[0]),
                                "solution": re.sub(r"[^\w+]", "self", kata.find("a").text.lower()),
                                "ext": "py",
                                }
                               for kata in soup.find_all("div", attrs={"class": "item-title"})]


def sync_kata(kata_type=None):
    if kata_type is None:
        kata_type = KATA_TYPE

    with open(META_DATA, 'r') as meta:
        data = load(meta, Loader=Loader)

    for t in kata_type:
        sync_kata_type(data, t)

    with open(META_DATA, 'w') as d:
        dump(data, d, Dumper=Dumper)

    return data


def parse_kata_body():
    pass


def load_full_page(browser):
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def get_page_source(url):
    # html = requests.get(url, headers=headers).text
    browser = webdriver.Firefox(**BROWSER_CONFIG)
    browser.get(url)
    load_full_page(browser)
    html = browser.page_source
    browser.quit()
    return bs4.BeautifulSoup(html.encode('utf-8', 'ignore'), 'lxml')


def generate_function_body(url):
    with open(META_DATA, 'r') as d:
        data = load(d, Loader=Loader)

    url = data["codewars"]["url"] + "/kata/" + url + "/train/python"
    soup = get_page_source(url)
    code = soup.body.find(id="code")
    fixture = soup.body.find(id="fixture")

    func_body = "" if code is None else "\n".join(map(lambda t: t.text, code.find_all("span", role="presentation")))
    func_name = re.search(r'(?<=def ).*(?=\()', func_body)
    func = {"body": func_body,
            "name": "" if func_name is None else func_name.group(0)}
    test_body = generate_test_body(func["name"], fixture.find_all("span", role="presentation"))
    return func, test_body


def generate_project_test(test_file, import_str, test_body):
    import_re = re.compile(r"(^import unittest)")
    body_re = re.compile(r"(^class.*:)")

    with open(test_file, "r+") as f:
        contents = f.readlines()
        for i, line in enumerate(contents):
            if re.search(import_re, line):
                contents.insert(i + 1, import_str)
            if re.search(body_re, line):
                contents.insert(i + 1, test_body)
        f.seek(0)
        f.writelines(contents)


def generate_project_files(kata=None, gen_test=True):
    with open(META_DATA, 'r') as meta:
        data = load(meta, Loader=Loader)

    if kata is None:
        kata = data["user"]["kata"]["unfinished"][:1]

    for k in kata:
        ext = f".{k['ext']}"
        file_name = re.sub(r"[^\w+]", "self", k["text"].lower())
        file_path = f"_{k['level']}kyu"

        test_file = "test/test" + file_path + ext
        source_file = file_path + "/" + file_name + ext

        if os.path.exists(file_path):
            with open(source_file, 'w') as f:
                func, test = generate_function_body(k["href"])
                f.write(func["body"])
            if gen_test:
                import_str = f"from ..{file_path}.{file_name} import {func['name']}\n"
                generate_project_test(test_file, import_str, test)


def load_data():
    global KATA_DATA
    if KATA_DATA is None:
        with open(META_DATA, 'r') as d:
            KATA_DATA = load(d, Loader=Loader)
