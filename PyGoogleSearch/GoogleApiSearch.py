__author__ = 'arshad'
from googleapiclient.discovery import build
import pprint


GOOGLE_API_KEY = 'AIzaSyA8IMsMe4EFl3mx5mAdHrhnWCQ_QWQ--8A'
googlurl = 'https://www.googleapis.com/customsearch/v1?parameters'
key=GOOGLE_API_KEY
CX = '016585465265343173652:e1cwh2kay9i'

my_api_key = GOOGLE_API_KEY
my_cse_id = CX

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'arsh2k7 pythonanywhere', my_api_key, my_cse_id, num=10)
for result in results:
    pprint.pprint(result)