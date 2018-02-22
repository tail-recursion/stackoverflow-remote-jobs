import requests
from bs4 import BeautifulSoup

base_url = 'https://stackoverflow.com'
first = '/jobs/remote-developer-jobs'

def get_tags(url=base_url+first, tags=[],j=0):
  response = requests.get(url)
  soup = BeautifulSoup(response.text,'lxml')
  anchors = soup.findAll('a',{'class':'post-tag job-link no-tag-menu'})
  for a in anchors: tags.append(a.text)
  next = soup.findAll('a',{'class':'test-pagination-next'})
  if next != []:
    next_url = base_url + next[0]['href']
    return get_tags(next_url,tags,j)
  else: return tags

def get_counts(tags):
    counts={}
    for tag in tags:
        if tag in counts: counts[tag] += 1
        else: counts[tag] = 1
    return counts

if __name__ == "__main__":
    tags = get_tags()
    counts = get_counts(tags)
    counts = list(counts.items())
    counts.sort(key=lambda x:x[1],reverse=True)
    for i in counts: print(i[0] + ': ' + str(i[1]))
