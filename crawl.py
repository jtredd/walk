import requests

crawled = list()
tocrawl = set([])
discard = set()
depth = 0


def crawl(seed):
    tocrawl = [seed]
    while tocrawl:
        entry = tocrawl.pop()
        if entry not in crawled:
            union(tocrawl, get_all_links(get_page(entry)))
            crawled.append(entry)
            get_pages(tocrawl)

def get_pages(L: list) -> None:
    global d
    depth = len(crawled)
    for l in L:
        d = depth - 1
        return get_all_links(get_page(l))
    seed = l

def get_page(self: str) -> str:
    user_agent_string = 'curl/7.59.1'
    headers = requests.utils.default_headers()
    headers['User-Agent'] = user_agent_string
    req = requests.get(self, headers=headers)
    if req.status_code == 200:
        crawled.append(self)
        return req.text
    return ""
    print(f'{req.status_code}: {self}')
    return None, 0

def get_slice(self: str) -> (str(), int()):
    print(self)
    start_link = self.find(' href')
    if start_link == -1:
        return None, 0
    start_pos = self.find('"', start_link)
    end_pos   = self.find('"', start_pos + 1)
    url = self[start_pos+1:end_pos]
    return url, end_pos

def get_all_links(page: str) -> str:
    links = []
    while True:
        url,endpos = get_slice(page)
        if url:
            print(f'{crawled[depth]}')
            links.append(make_absolute(url,base_url=crawled[depth], discard=False))
            page = page[endpos:]
        else:
            break
        [tocrawl.add(x) for x in links]

    return links

def make_absolute(self: str, base_url: str, discard=True) -> str:
    root = '/'.join(base_url.split('/', 3)[0:3])
    if root in self:
        return self
    if 'http' in self and discard is False:
        return self
    elif 'http' in self and discard is True:
        discard.add(self)
    else:
        return ''.join((root, self))

def union(p: set, q: list) -> None:
    for e in q:
        if e not in p:
            p.append(e)

if __name__ == '__main__':
    from sys import argv
    seed = argv[1]
    crawl(seed)
