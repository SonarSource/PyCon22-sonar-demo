import re


def my_regex():
    re.compile(r'(^Successfully built |sha256:)([0-9a-f]+)$')
