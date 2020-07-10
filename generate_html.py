#!/usr/bin/env python3

import json

import page_model
import models_html

import config


with open('simple-icons.json', 'r') as data:
    icon_data = json.load(data)

all_html = str()
model_html = dict()

for model_name, model_str in models_html.MODEL_REGISTRY.items():

    model_renderized = str()

    for item in config.SOFTWARE: #icon_data['icons']:

        filename = item.lower()

        with open(f'{config.DIR_ICONS}{filename}.svg', 'r') as fd:
            svg = fd.read()

        model_renderized += model_str.format(icon_name=item,
                                            title=item,
                                            svg=svg)

    model_html.update({model_name: model_renderized})

    all_html += model_html[model_name]

