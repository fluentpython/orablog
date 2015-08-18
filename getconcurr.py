from concurrent import futures
from requests import get

orgs = 'acm gnu eff wwf msf care ceres'.split()
urls = ('http://www.%s.org' % org for org in orgs)

with futures.ThreadPoolExecutor(len(orgs)) as executor:
    results = list(executor.map(get, urls))

for page in results:
    length = int(page.headers['Content-Length'])
    print('{:5} {}'.format(length, page.url))
