'''Do a Google search and return results'''

from googlesearch import search
 
QUERY = "Python blogs"
 
# Change tld to "co.uk" or whatever, num=amount of results to get
for RESULTS in search(QUERY, tld="co.uk", num=10, stop=10, pause=2):
    print(RESULTS+'\n')