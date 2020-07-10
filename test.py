import json
import config
import utils

sft = config.SOFTWARE

print(sft)

with open('simple-icons.json', 'r') as fd:
    a = json.load(fd)

for item in a['icons']:
    uri = utils.title_to_filename(item['title'])
    tt = item['title']
    print(uri, tt, uri in sft)
