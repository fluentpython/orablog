from concurrent import futures
from requests import get

orgs = 'acm care ceres eff gnu msf wwf'.split()
urls = ('http://www.%s.org' % org for org in orgs)

with futures.ThreadPoolExecutor(len(orgs)) as executor:
    for page in executor.map(get, urls):
        length = int(page.headers['Content-Length'])
        print('{:5} {}'.format(length, page.url))
