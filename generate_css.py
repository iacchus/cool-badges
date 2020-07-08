#!/usr/bin/env python3

import json

import models_css

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

all_css = str()
model_css = dict()

for model_name, model_str in models_css.MODEL_REGISTRY.items():

    model_css.update({model_name:
                      "".join([model_str.format(hex_color_left=item['hex'],
                               hex_bgcolor_left='rgba(255, 255, 255, 0.9)',
                               hex_color_right='rgba(255, 255, 255, 0.9)',
                               hex_bgcolor_right=item['hex'],
                               icon_name=item['title'],
                               title=item['title'].lower())
                       for item in icon_data['icons']
                       if item['title'].lower() in software])})
    all_css += model_css[model_name]

