from concurrent import futures
from requests import get

orgs = 'acm gnu eff wwf msf care ceres'.split()
urls = ('http://www.%s.org' % org for org in orgs)

with futures.ThreadPoolExecutor(len(orgs)) as executor:
    tasks = [executor.submit(get, url) for url in urls]
    for task in futures.as_completed(tasks):
        page = task.result()
        length = int(page.headers['Content-Length'])
        print('{:5} {}'.format(length, page.url))
