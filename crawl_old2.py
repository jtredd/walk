#!/usr/local/bin/python

user_agent_string = 'User-Agent: Chrome/88 Safari/538'
#user_agent_string = 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'


crawled = []
tocrawl = set()


def get_page(self: str) -> str:
  import requests
  headers = requests.utils.default_headers()
  headers['User-Agent'] = user_agent_string
  req = requests.get(self, headers=headers)
  return req.text


def get_next_target(self: str) -> str:
  start_link = self.find(' href')
  if start_link == -1:
    return None, 0
  start_quote = self.find('"', start_link)
  end_quote = self.find('"', start_quote + 1)
  url = self[start_quote + 1:end_quote]
  return url, end_quote

def get_all_links(page: str) -> list:
  links =[]
  while True:
    url,endpos = get_next_target(page)
    if url:
      links.append(url)
      page = page[endpos:]
    else:
      break
  return links

def union(p, q):
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

def unique(l):
  found = set([])
  keep = []
  for item in l:
    if item not in found:
      found.add(item)
      keep.append(item)
  print('found: {}\n{}'.format(len(found), found))
  return sort(keep)


def absolute(path, paths):
  plist = []
  root_url = '/'.join(path.split('/')[0:3])
  for path in paths:
    if 'http' not in path:
      plist.append(root_url + path)
    plist.append(path)
  return plist


def main(CURL):
  return get_all_links(get_page(CURL))


if __name__ == '__main__':
  from sys import argv
  listings = []
  if argv[1] == '-h':
    print("""
        usage: crawl.py -u [url]
        """
        )
  if argv[1] == '-u' or '--url':
    CURL = argv[2]
  else:
    CURL = 'https://www.iana.org/domains/example'
  ROOT = '/'.join(CURL.split('/')[0:3])
