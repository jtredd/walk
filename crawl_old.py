class Web:

    wseed = set()
    crawled = set()
    tocrawl = list()
    #seed = 'https://www.example.com'
    seed = 'https://packetstormsecurity.com/Crackers/wordlists/page4/'
    tocrawl.append(seed)

    def __init__(self: str, max_depth: int):
        self._tocrawl = [self]
        tocrawl = set()
        self.next_depth = list()
        depth = 0

def crawl(seed, max_depth):
    _tocrawl=[seed]
    crawled = list()
    tocrawl = set()
    next_depth = list()
    depth = 0
    while Web.tocrawl and depth <= max_depth:
        entry = Web.tocrawl.pop()
        if entry not in crawled:
            print(entry)
            union(Web.tocrawl, get_all_links(get_page(entry)))
            Web.crawled.add(entry)
#            tocrawl.add(normalize(entry, Web.seed))
        if not _tocrawl:
            Web.tocrawl, next_depth = next_depth, []
            depth = depth + 1


def crawl2(seed, max_depth):
    __tocrawl=[seed]
    __crawled=list()
    __next_depth=list()
    depth=0
    while __tocrawl and depth <= max_depth:
        entry = __tocrawl.pop()
        if entry not in __crawled:
            union(__tocrawl, get_all_links(get_page(entry)))
            __crawled.append(entry)
        if not __tocrawl:
            __tocrawl, __next_depth = __next_depth, []
            print(depth)
            depth = depth + 1
        Web.crawled = __tocrawl.copy
#        union(tocrawl, _tocrawl)
#    return crawled, _tocrawl
#            get_pages(tocrawl)

def get_page(self: str) -> str:
    import requests
    user_agent_string = 'curl/7.59.1'
    headers = requests.utils.default_headers()
    headers['User-Agent'] = user_agent_string
    if isinstance(self, str): 
        req = requests.get(normalize(self), headers=headers)
        if req.status_code == 200:
            Web.crawled.add(req.url)
            return req.text
        Web.crawled.add((req.url, self))

def get_slice(self: str):
    start_link = self.find(' href')
    if start_link == -1:
        return None, 0
    start_pos = self.find('"', start_link)
    end_pos   = self.find('"', start_pos + 1)
    url = self[start_pos+1:end_pos]
    return url, end_pos

def normalize(self: str) -> str:
    base_url = Web.seed
    if base_url in self:
        return self
    if 'http' in self:
        return
    else:
        return ''.join(('/'.join(base_url.split('/', 3)[0:3]), self))



def get_all_links(page: str) -> str:
    links = []
#    schema = dict()
    while True:
        url,endpos = get_slice(page)
        if url:
#            print(f'{crawled[depth]}')
#            links.append(make_absolute(url,base_url=crawled[depth], discard=False))
            links.append(url)
            page = page[endpos:]
        else:
            break
#        Web.crawled.append(page[0])
#    [Web.tocrawl.add(normalize(x, Web.seed)) for x in links]
#    schema += {Web.seed: [Web.tocrawl.add(normalize(x, Web.seed)) for x in links]}
#    print(schema)
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
    crawl2(seed, 1)
