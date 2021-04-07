#!/usr/bin/env python3
__author__      = "Joy Ghosh"
__Ver__         = "V 1.0"
__copyright__   = "Copyright 2021, SYSTEM00 SECURITY"
from colorama import Fore, Back, Style
import requests
from bs4 import BeautifulSoup
import random
import argparse
try:
  parser = argparse.ArgumentParser()
  parser.add_argument("-q", "--query", help="Your Query example: -q 'Query' ", type=str)
  args = parser.parse_args()
  qe='https://exploits.shodan.io/?q='+args.query+'&p=1'
  qe1='https://exploits.shodan.io/?q='+args.query+'&p=2'
except TypeError:
  print("No Query Detected type -h to see all flags")
except:
  exit()
A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36")
Agent = A[random.randrange(len(A))]
headers = {'user-agent': Agent}
def result(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    search = soup.find_all('div',class_="result")
    for h in search:
        link=h.a.get('href')
        title=h.a.get_text()
        print(Fore.RED,link,' ',Fore.GREEN,title,Fore.WHITE)
try:
    result(qe)
    result(qe1)
except KeyboardInterrupt:
  print("CTRL+C Detected Stoping")
except:
  exit()
