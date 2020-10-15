import requests
import re
from bs4 import BeautifulSoup as bs

def parseCookieFile(cookiefile):
    """Parse a cookies.txt file and return a dictionary of key value pairs
    compatible with requests."""

    cookies = {}
    with open (cookiefile, 'r') as fp:
        for line in fp:
            if not re.match(r'^\#', line):
                lineFields = line.strip().split('\t')
                cookies[lineFields[5]] = lineFields[6]
    return cookies

cookies = parseCookieFile('cookies.txt')

import pprint
pprint.pprint(cookies)
video="/videos/dist/videos.c6e7c3fa04187a2546a2.js?t=1598915737387"
#r = requests.get('https://learning.oreilly.com/videos/ruby-on-rails/9780136733461/9780136733461-ROR6_01_01_02_03'+video, cookies=cookies)
oreilly="https://learning.oreilly.com"
r = requests.get(oreilly+video, cookies=cookies)
soup = bs(r.text, 'lxml')
print(soup.prettify())
