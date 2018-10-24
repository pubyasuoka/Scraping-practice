import lxml.html

parser=lxml.html.HTMLParser(encoding='utf-8')
tree = lxml.html.parse("index.html",parser)
html=tree.getroot()

  
for a in html.cssselect('a'):
  print(a.get('href'),a.text)
