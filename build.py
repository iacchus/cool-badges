#!/usr/bin/env python

#from os.path import isfile

import utils
#from utils import write_model_html_file
#from utils import write_model_css_file
#from utils import write_index_html_file
#from utils import write_index_css_file

import generate_html
import generate_css

#from models_html import MODEL_REGISTRY as html_model_registry
#from models_css import MODEL_REGISTRY as css_model_registry


#if not isfile('.badge-build-root'):
#    print('Needs to be at root directory to build.')
#    exit(1)

utils.write_index_html_file(html=generate_html.all_html)
utils.write_index_css_file(css=generate_css.all_css)

for model_name, model_html in generate_html.model_html.items():
    utils.write_model_html_file(model_name, model_html)

for model_name, model_css in generate_css.model_css.items():
    utils.write_model_css_file(model_name, model_css)
