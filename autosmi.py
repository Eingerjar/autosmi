import requests
import json
iDatas=(4169,4462)

def crawl_idata(idata):
    r = requests.post('https://www.anissia.net/anitime/cap', data=({'i': idata}))
    print(r.status_code)
    print(r.text[1:-1])
for idata in iDatas:
    crawl_idata(idata)