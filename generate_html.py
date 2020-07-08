#!/usr/bin/env python3

import json

import page_model
import css_model
import models_html


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


with open('simple-icons.json', 'r') as data:
    icon_data = json.load(data)

all_html = str()
model_html = dict()

for model_name, model_str in models_html.MODEL_REGISTRY.items():

    model_html.update({model_name:
                       "".join([model_str.format(icon_name=item['title'],
                                                 title=item['title'].lower())
                                for item in icon_data['icons']
                                if item['title'].lower() in software])})

    #print(page_model.model.format(model_name=model_name, html=all_html))

    all_html += model_html[model_name]

#print(page_model.model.format(model_name=model_name, html=all_html))

#print(all_html)

