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

#model = """
#/* {icon_name} */
#
#.{title}-badge {{}}
#.{title}-left {{
#  color: #{hex_color_left};
#  background-color: #{hex_bgcolor_left};
#}}
#.{title}-right {{
#  color: #{hex_color_right};
#  background-color: #{hex_bgcolor_right};
#}}
#
#"""

# let's get our badge models and register them locally
for key, value in models_css.__dict__.items():
    if key.startswith('model_'):
        model_name = key.split('_', maxsplit=1)[1]
        MODEL_REGISTRY.update({model_name: value})

with open('simple-icons.json', 'r') as data:
    icon_data = json.load(data)

#print(icon_data)

#our_items = list()
#our_data = dict()
our_css = str()
#print(MODEL_REGISTRY)

for model_name, model_str in MODEL_REGISTRY.items():

    our_css += "".join([model_str.format(hex_color_left=item['hex'],
                               hex_bgcolor_left='rgba(255, 255, 255, 0.9)',
                               hex_color_right='rgba(255, 255, 255, 0.9)',
                               hex_bgcolor_right=item['hex'],
                               icon_name=item['title'],
                               title=item['title'].lower())
                       for item in icon_data['icons']
                       if item['title'].lower() in software])


#for item in icon_data['icons']:
#    #print(item)
#    if item['title'].lower() in software:
#        #our_data.update({item['title'].lower(): (item['title'], item['hex'],)})
#        #our_items.append(item)
#        our_css += model.format(hex_color_left=item['hex'],
#                               hex_bgcolor_left='rgba(255, 255, 255, 0.9)',
#                               hex_color_right='rgba(255, 255, 255, 0.9)',
#                               hex_bgcolor_right=item['hex'],
#                               icon_name=item['title'],
#                               title=item['title'].lower())

print(our_css)


