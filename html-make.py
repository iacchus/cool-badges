#!/usr/bin/env python3

import json

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

model = """
/* {icon_name} */

.{title}-badge {{}}
.{title}-left {{
  color: #{hex_color_left};
  background-color: #{hex_bgcolor_left};
}}
.{title}-right {{
  color: #{hex_color_right};
  background-color: #{hex_bgcolor_right};
}}

"""

with open('simple-icons.json', 'r') as data:
    icon_data = json.load(data)

#print(icon_data)

#our_items = list()
our_data = dict()
our_css = str()

for item in icon_data['icons']:
    #print(item)
    if item['title'].lower() in software:
        #our_data.update({item['title'].lower(): (item['title'], item['hex'],)})
        #our_items.append(item)
        our_css += model.format(hex_color_left=item['hex'],
                               hex_bgcolor_left='rgba(255, 255, 255, 0.9)',
                               hex_color_right='rgba(255, 255, 255, 0.9)',
                               hex_bgcolor_right=item['hex'],
                               icon_name=item['title'],
                               title=item['title'].lower())

print(our_css)


