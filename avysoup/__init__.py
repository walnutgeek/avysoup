from typing import Any, Dict, List
from bs4 import BeautifulSoup
import avysoup.http as h
import json
import sys

def parse_index(u:str, requester = h.Requester())->List[Dict[str,Any]]:
    html_doc = requester[u]
    soup = BeautifulSoup(html_doc, 'html.parser')
    return [{ 
        "date" : tr.find(class_="date-display-single").text,
        "url" : h.urljoin(u, tr.find(class_="views-field-field-ob-loc-name").find("a")["href"])
    } for tr in soup.select("tbody > tr") ]

def update_case(case: Dict[str, Any], requester = h.Requester()):
    u = case['url']
    soup = BeautifulSoup(requester[u], 'html.parser')
    geo = soup.find(class_='geo')
    try:
        case['geo'] = { 
            'lat' : float(soup.find(class_='latitude').text),
            'long' : float(soup.find(class_='longitude').text) 
        }
    except AttributeError:
        print(f"{u} has no geo?", file=sys.stderr)
    


def main(requester = h.Requester())->int:
    index = parse_index('https://www.sierraavalanchecenter.org/incidents-archive', requester)
    for case in index:
        update_case(case, requester)
    print(json.dumps(index, indent=2))
    return 0 if index else -1