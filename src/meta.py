import re

TAB_CHAR = " " * 4

KATA_LEVELS = {
    1: "indigo",
    2: "purple",
    3: "darkblue",
    4: "blue",
    5: "darkorange",
    6: "orange",
    7: "silver",
    8: "white"
}

COMMANDS = ((re.compile(r'^[\s*]test(?=\.)'), "self"),
            (re.compile(r"assert_equals(?=\()"), "assertEqual"),
            (re.compile(r"assert_approx_equals(?=\()"), "assertAlmostEqual"),
            # extend some
            )


def convert_to_unittest(s):
    for r in COMMANDS:
        s = re.sub(r[0], r[1], s)
    return re.sub(r'[^\x00-\x7F]+', ' ', s)  # removing non-ascii char


def generate_test_body(func_name, test_body_raw):
    test_body = "\n".join(map(lambda t: f"{TAB_CHAR * 2}" + convert_to_unittest(t.text), test_body_raw))
    return f"\n{TAB_CHAR}def test_{func_name}(self):\n{test_body}"


def generate_list_item(url, href, text, level, solution, ext):
    badge_url = "https://img.shields.io/badge/"
    kata_badge_header = "CodeWars"
    sol_url = "https://github.com/kupns-aka-kupa/etc/tree/master/codewars/"
    sol_badge_header = "GitHub"
    return f"""
    <li>
        <div>
            <a target="__blank" href="{url}/kata/{href}">
                <img src="{badge_url}{kata_badge_header}%20-{text}-{KATA_LEVELS[level]}.svg" alt="{text}">
            </a>
            <a target="__blank" href="{sol_url}self{level}kyu/{solution}.{ext}"> 
                <img src="{badge_url}{sol_badge_header}%20-Solution-green.svg" alt="Solution of {text}">
            </a>
        </div>
    </li>"""


def generate_html_list(url, data):
    return "<ul>" + "".join([generate_list_item(url, **kata) for kata in data]) + "</ul>\n\n"


def generate_readme(data):
    out = ""
    for v in data["user"]["kata"]:
        out += "# " + v[0].upper() + v[1:] + "\n\n"
        out += generate_html_list(data["codewars"]["url"], sorted(data["user"]["kata"][v], key=lambda i: i["level"]))

    with open("README.md", 'w') as readme:
        readme.write(out)


def generate_html_table(mass, size=10, style='border="1"'):
    str_res = f'<table {style}>'
    rows = [mass[i:i + size] for i in range(0, len(mass), size)]
    str_res += "".join(['<tr>' + "".join(map(lambda x: '<td><p>' + str(x) + '</p></td>', i)) + '</tr>' for i in rows])
    str_res += '</table>'
    return str_res
