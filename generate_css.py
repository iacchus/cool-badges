#!/usr/bin/env python3

import json

import css_base
import models_css

import config

import utils

with open('simple-icons.json', 'r') as data:
    icon_data = json.load(data)

all_css = str()
model_css = dict()

all_css += css_base.model

for model_name, model_str in reversed(models_css.MODEL_REGISTRY.items()):

    pre_model = str()

    for item in icon_data['icons']:

        icon_name = item['title']

        uri = utils.title_to_filename(item['title'])
        if uri in config.SOFTWARE:

            pre_model += model_str.format(hex_color_left=item['hex'],
                                   hex_bgcolor_left='rgba(255, 255, 255, 0.9)',
                                   hex_color_right='rgba(255, 255, 255, 0.9)',
                                   hex_bgcolor_right=item['hex'],
                                   icon_name=icon_name,
                                   title=uri, model=model_name)
    all_css += pre_model

    model_css.update({model_name: "{0}{1}".format(css_base, pre_model)})

