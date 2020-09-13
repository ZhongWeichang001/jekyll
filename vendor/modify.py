from bs4 import BeautifulSoup
import os
files = os.listdir('_site/')
for fname in files:
  if (fname.endswith('.html')):
    with open('_site/'+fname, 'r+') as f:
      soup = BeautifulSoup(f, 'html.parser')
      #
      css=soup.find_all('link')
      for c in css:
        if c['href']=='https://use.fontawesome.com/releases/v5.0.13/css/all.css':
          c.extract()
        elif c['href'].startswith("/assets"):
          c['href']=c['href'][1:]
      content=soup.prettify()
      f.seek(0)
      f.truncate()
      f.write(content)
