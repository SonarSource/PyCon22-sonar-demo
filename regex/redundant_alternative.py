import re


def my_regex():
    re.compile(
        r'[a-z\:\//\.]+(youtube|youtu)\.(com|be)/(watch\?v=|embed/|.+\?v=)?([^"&?\s]{11})?'
    )
    re.compile(r'true|false|undefined|[0-9A-Za-z]+')
