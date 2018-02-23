#!/usr/bin/env python
import sys
import time

def timeit(method):
  def timed(*args, **kw):
    ts = time.time()
    result = method(*args, **kw)
    te = time.time()

    if 'log_time' in kw:
      name = kw.get('log_name', method.__name__.upper())
      kw['log_time'][name] = int((te - ts) * 1000)
    else:
      print('%r  %2.2f ms' % \
          (method.__name__, (te - ts) * 1000))
    return result
  
  return timed

DURL = "http://www.udacity.com/cs101x/crawling.html"
try:
  import requests
except ImportError() as e:
  print(e.code)

if len(sys.argv[1]) == 0:
  url=DURL
else:
  url=sys.argv[1]

r = requests.get(url)
if r.content > 0:
  page = r.content

def get_page(url):
    try:
      if url == "":
        print("Missing arg1.\n")
        return ''
      elif url == "https://jradd.com":
        return ''
    except:
      if len(sys.argv[1] > 0):
        url = sys.argv[1]
      else:
        url = DURL
      return url
    return ""

def get_next_target(page):
  if page==0:
    page=req_page(url)
  start_link = page.find('<a href=')
  if start_link == -1: 
      return None, 0
  start_quote = page.find('"', start_link)
  end_quote = page.find('"', start_quote + 1)
  url = page[start_quote + 1:end_quote]
  return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

@timeit
def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
       # for v in links:
          #if len(v) > 1:
          #  print(v)
    return links

@timeit
def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
          union(tocrawl, get_all_links(get_page(page)))
          crawled.append(page)
          print(crawled)
          print(tocrawl)

if __name__ == '__main__':
  crawl_web(get_all_links(page))
