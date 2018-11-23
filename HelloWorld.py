import re
import urllib.request
def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist" .+?<div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
