import urllib.request as urllib
import re

keyword = re.compile("schistosoma", re.IGNORECASE)
url = "http://www.ncbi.nlm.nih.gov/pubmed?term=18235848"

handler = urllib.urlopen(url)
html = handler.read() ## it's class 'bytes'
utf = str(html)

titlereg = re.compile("<h1>.{5,400}</h1>")
matchtitle = titlereg.search(utf)

title = matchtitle.group()

word = keyword.search(title)
