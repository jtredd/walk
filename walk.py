#!/usr/bin/env python
import sys


def get_next_target(page):
  start_link = page.find('<a href=')
  if start_link == -1: 
      return None, 0
  start_quote = page.find('"', start_link)
  end_quote = page.find('"', start_quote + 1)
  url = page[start_quote + 1:end_quote]
  return url, end_quote


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
        for v in links:
          if len(v) > 1:
            print(v)
    return links

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def crawl_web(seed):
  tocrawl = [seed]
  crawled = []
  while tocrawl:
    entry = tocrawl.pop()
    if entry not in crawled:
      union(tocrawl, get_all_links(page))
      crawled.append(entry)



if __name__ == "__main__":
  import requests
  target = str(sys.argv[1])
  r = requests.get(target)
  if len(r.content) > 0:
    page = str(r.content)
    crawl_web(target)
