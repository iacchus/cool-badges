#from os.path import isfile

import utils
#from utils import write_model_html_file
#from utils import write_model_css_file
#from utils import write_index_html_file
#from utils import write_index_css_file

import generate_html


#if not isfile('.badge-build-root'):
#    print('Needs to be at root directory to build.')
#    exit(1)

utils.write_index_html_file(html=generate_html.all_html)
utils.write_index_css_file(css=generate_css.all_css)
