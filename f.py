import requests
import bs4

response = requests.get("https://www.linkedin.com/search/results/all/?keywords=dewan%20singh%20parmar&origin=GLOBAL_SEARCH_HEADER")
da = []
data = bs4.BeautifulSoup(response.text,'html.parser')
read=data.findAll('div',{'class':'search-typeahead-v2 search-global-typeahead__typeahead ember-view'})
for a in read:
    print(a)
   
#print(read)