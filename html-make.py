#!/usr/bin/env python3

import json

import models

MODEL_REGISTRY = dict()

software = ['android', 'apache', 'archlinux', 'ardour', 'asciinema',
            'awesomewm', 'coffeescript', 'concourse', 'css3', 'c',
            'debian', 'duolingo', 'firefox', 'flask', 'freebsd', 'gimp',
            'github', 'gnuicecat', 'gnu', 'html5', 'imgur', 'inkscape',
            'jupyter', 'krita', 'last-dot-fm', 'latex', 'linux', 'lmms',
            'mozilla', 'musescore', 'mysql', 'obsstudio', 'openbsd',
            'opensourceinitiative', 'openssl', 'php', 'pypi', 'python',
            'reddit', 'repl-dot-it', 'rust', 'sega', 'simpleicons',
            'soundcloud', 'sqlite', 'stylus', 'tor', 'tunein', 'twitch',
            'ubuntu', 'unity', 'vim', 'wechat', 'wikipedia', 'wordpress',
            'x-dot-org']

#model_a = """
#<!--
#
#{icon_name}
#
#-->
#<div class="box">
#  <div class="badge {title}-badge">
#    <div class="left {title}-left"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/{title}.svg" /></div>
#    <div class="right {title}-right">{title}</div>
#  </div>
#</div>
#
#"""

# let's get our badge models and register them locally
for key, value in models.__dict__.items():
    if key.startswith('model_'):
        #model_name = "".join(key.split('_', maxsplit=1)[1])
        model_name = key.split('_', maxsplit=1)[1]

        MODEL_REGISTRY.update({model_name: value})

with open('simple-icons.json', 'r') as data:
    icon_data = json.load(data)

our_html = str()

print(MODEL_REGISTRY)
for model_name, model_str in MODEL_REGISTRY.items():
    our_html += "".join([model_str.format(icon_name=item['title'],
                                         title=item['title'].lower())
                       for item in icon_data['icons']
                       if item['title'].lower() in software])



#for item in icon_data['icons']:
#
#    if item['title'].lower() in software:
# 
#        our_html += model_a.format(icon_name=item['title'],
#                               title=item['title'].lower())

print(our_html)

