from requests import Session, Request, utils, exceptions

#CERT = utils.DEFAULT_CA_BUNDLE_PATH
CERT = 'cert.pem'
HEADERS = utils.default_headers()
UA_STRING = 'Curl 7/59.1'


class Web:
        crawled = set()
        tocrawl = dict()
        rel     = tuple()
        seed    = tuple()

def print_url(r, *args, **kwargs):
    print(r.url)

def record_hook(r, *args, **kwargs):
    r.hook_called = True
    # catchme
    Web.crawled.add(r.url)
    return r

def get(url: str, ua_string=None):
    """
    function to get http response in text.
    :return response object
    """
    headers = utils.default_headers()
    headers['User-Agent'] = ua_string
#    data=b'send exactly these bytes.'
    hooks={'response': [print_url, record_hook]}
    s = Session()
    req = Request('GET', url, headers=headers, hooks=hooks)
#    req.register_hook('request', hooks)

    try:
        prepped = s.prepare_request(req)
        resp = s.send(prepped,
                      stream=True,
                      verify=True,
                      proxies=None,
                      cert='cert.pem',
                      timeout=(3, 20)
                     )
    except Exception as e:
        print(e, url)
#        print('Perhaps you meant: \r\n{}'.format(''.join(
#            (
#                get_domain(Web.crawled[-1]),url
#            )
#        )))
        return -1

    return resp.text

def get_next_target(page: str) -> tuple():
    if isinstance(page, int):
        return None, 0
    elif isinstance(page, str):
        start_link = page.find('<a href')
        if start_link == -1:
            return None, 0
        start_pos = page.find('"', start_link)
        end_pos   = page.find('"', start_pos + 1)
        url = page[start_pos+1:end_pos]
        return url, end_pos

def get_all_links(page: str) -> str():
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(q: list, p: list):
    for e in p:
#        if q:
        if e not in q:
            q.append(e)

def crawl(seed, max_depth):
    _tocrawl = [seed]
    tocrawl = set()
    crawled = []
    next_depth = []
    depth = 0
    while _tocrawl and depth <= max_depth:
        entry = _tocrawl.pop()  # empty
        Web.tocrawl.update({depth: entry})
        if entry not in crawled:
            union(_tocrawl, get_all_links(get(entry)))
            crawled.append(entry)
        if not _tocrawl:
            _tocrawl, next_depth = next_depth, []
            depth = depth + 1
#    return crawled, _tocrawl, tocrawl

def get_domain(self: str) -> str:
    return '/'.join(self.split('/', 3)[0:3])

if __name__ == '__main__':
#    url = 'https://www.example.com'
#    url = 'http://localhost:8000/test1'
    url = 'https://example.com'
    print(crawl(url, 4))
