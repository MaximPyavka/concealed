#!/usr/bin/python3

import requests
from lxml import html
from time import sleep
import json
session = requests.Session()

with open('data/dumpey') as dump:
    dumped = dump.read()

ids = []

raw_dump = html.fromstring(dumped)

print('Preparing IDS...')

for i in raw_dump.xpath('//h5/a[@class="orange"]/@href'):
    if i not in ids:
        ids.append(i)

print(f'{len(ids)} IDS ready!')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'application/json', 'X-Requested-With': 'XMLHttpRequest',
           'Content-Type': 'application/json'}

rows = []
for num, i in enumerate(ids[:1]):
    print(f'Parsing {i} - [{num + 1}/{len(ids)}]')
    shit = i.split('=')[-1]
    raw = session.post(
        'https://www.eonetwork.org/_vti_bin/eowcfservices/EOServicesForForm.svc/GetMemberProfileInformationByExternalId',
        data=f'"{shit}"',
        headers=headers).json()

    raw = json.loads(raw)
    print(raw)
    # user = dict(json.loads(raw)['data']) # Not sure it is the best solution to exclude EvenInfo key, please take a look.
    # for key in list(user):
    #     if key == 'EventInfo':
    #         del user[key]
    #rows.append(raw)

    sleep(1)

for k,v in raw.items():
    print(f'{k}--->{v}')

# Add logic to write CSV file, please.

