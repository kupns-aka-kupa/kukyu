import re


def domain_name(url):
    res = re.search(r'.*?(?=\.)', re.sub(r'www\.', '', url.split('//')[-1])).group(0)
    return res
