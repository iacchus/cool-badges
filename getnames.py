import json
import re

with open('simple-icons.json','r') as fl:
    frk = json.load(fl)

namelist = [item['title'] for item in frk['icons']]

names_str = "\n".join(namelist).lower()

our_str = re.sub('\+', 'plus', names_str)     # \+
our_str = re.sub('^\.', 'dot-', our_str)     # ^\.
our_str = re.sub('\.$', '-dot', our_str)     # \.$
our_str = re.sub('\.', '-dot-', our_str)    # \. 
our_str = re.sub('^&', 'and-', our_str)      # ^&
our_str = re.sub('&$', '-and', our_str)      # &$
our_str = re.sub('&', '-and-', our_str)     # &
our_str = re.sub('[ !:’\']', '', our_str)    # [ !:'']
our_str = re.sub('à|á|â|ã|ä', 'a', our_str) # à|á|â|ã|ä
our_str = re.sub('ç|č|ć', 'c', our_str)     # ç|č|ć
our_str = re.sub('è|é|ê|ë', 'e', our_str)   # è|é|ê|ë
our_str = re.sub('ì|í|î|ï', 'i', our_str)   # ì|í|î|ï
our_str = re.sub('ñ|ň|ń', 'n', our_str)     # ñ|ň|ń
our_str = re.sub('ò|ó|ô|õ|ö', 'o', our_str) # ò|ó|ô|õ|ö
our_str = re.sub('š|ś', 's', our_str)       # š|ś
our_str = re.sub('ù|ú|û|ü', 'u', our_str)   # ù|ú|û|ü
our_str = re.sub('ý|ÿ', 'y', our_str)       # ù|ú|û|ü
our_str = re.sub('ž|ź', 'z', our_str)       # ž|ź

#urilist = our_str.split('\n')


#print(names_str.lower())
print(our_str.lower())
#print(urilist)
