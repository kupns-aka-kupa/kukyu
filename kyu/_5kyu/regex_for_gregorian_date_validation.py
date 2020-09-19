import re


def date_validation(s):
    delimeters = "[.]"
    years = "(1[6-9]|[2-9]\d)\d{2})"
    factor = "(?:0[48]|[2468][048]|[13579][26])"
    reg = "^(?:" \
          "(?:31%d(?:0[13578]|1[02]))|" \
          "(?:(?:29|30)%d(?:0[13-9]|1[0-2]))" \
          ")%d" \
          "(?:%y" \
          "$|^(?:29%d02%d" \
          "(?:" \
          "(?:\d\d%f)|" \
          "(?:%f00)" \
          ")" \
          ")$|^(?:" \
          "(?:0[1-9]|1\d|2[0-8])" \
          "%d" \
          "(?:(?:0[1-9])|(?:1[0-2]))" \
          "%d" \
          "(?:%y" \
          ")$".replace("%d", delimeters).replace("%y", years).replace("%f", factor)
    return bool(re.match(reg, s))
