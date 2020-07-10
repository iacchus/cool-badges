#!/usr/bin/env python3

import json

import page_model
import models_html

import utils

import config


with open('simple-icons.json', 'r') as data:
    icon_data = json.load(data)

all_html = str()
model_html = dict()

# iterate reversed, so the new models are on top
for model_name, model_str in reversed(models_html.MODEL_REGISTRY.items()):

    #model_renderized = str()
    model_renderized = f"<h2>model {model_name}</h2>"

    #for item in config.SOFTWARE: #icon_data['icons']:
    for item in icon_data['icons']:

        icon_name = item['title']
        uri = utils.title_to_filename(item['title'])

        if uri in config.SOFTWARE:

            with open(f'{config.DIR_ICONS}{uri}.svg', 'r') as fd:
                svg = fd.read()

            model_renderized += model_str.format(icon_name=icon_name,
                                                title=uri,
                                                svg=svg)

    model_html.update({model_name: model_renderized})

    all_html += model_html[model_name]

