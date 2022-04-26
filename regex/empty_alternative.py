import re


def my_regex():
    re.compile("utf[ -]?(8|16|32)[ -]?(le|be|)?(sig)?", flags=re.IGNORECASE)
