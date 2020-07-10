import re

import config
import page_model

def indent(spaces, text):

    indentation = ' ' * spaces

    return "".join([indentation + line
                    for line in text.splitlines(keepends=True)])

def print_page(html, model_name='all'):

    html = indent(4, html)
    page = page_model.model.format(model_name=model_name, html=html)

    print(page)

def generate_page(html, model_name='all'):

    html = indent(4, html)
    page = page_model.model.format(model_name=model_name, html=html)

    return page

def write_file(path, data):

    if config.DEBUG:

        if not config.SHOW_DATA:
            data = '(n/a)'

        print(f"path: {path}", f"data: {data}", sep='\n', end='\n\n')

        return True

    else:

        print(f"writing {path}")
        src = open(path, 'w')
        src.write(data)


def write_model_html_file(model_name, html):

    root = config.DIR_BUILD_MODEL
    path = f"{root}index.{model_name}.html"
    page = generate_page(model_name, html)

    write_file(path, page)


def write_model_css_file(model_name, css):

    root = config.DIR_BUILD_MODEL
    path = f"{root}style.{model_name}.css"

    write_file(path, css)


def write_index_html_file(html):

    root = config.DIR_BUILD_INDEX
    path = f"{root}index.html"
    page = generate_page(html)

    write_file(path, page)


def write_index_css_file(css):

    root = config.DIR_BUILD_INDEX
    path = f"{root}style.css"

    write_file(path, css)

def title_to_filename(name_str):

    our_str = name_str.lower()
    our_str = re.sub('\+', 'plus', our_str)     # \+
    our_str = re.sub('^\.', 'dot-', our_str)     # ^\.
    our_str = re.sub('\.$', '-dot', our_str)     # \.$
    our_str = re.sub('\.', '-dot-', our_str)    # \. 
    our_str = re.sub('^&', 'and-', our_str)      # ^&
    our_str = re.sub('&$', '-and', our_str)      # &$
    our_str = re.sub('&', '-and-', our_str)     # &
    our_str = re.sub('à|á|â|ã|ä', 'a', our_str) # à|á|â|ã|ä
    our_str = re.sub("[!:’']", '', our_str)    # [ !:'']
    our_str = re.sub('\s', '', our_str)    # [ !:'']
    our_str = re.sub('ç|č|ć', 'c', our_str)     # ç|č|ć
    our_str = re.sub('è|é|ê|ë', 'e', our_str)   # è|é|ê|ë
    our_str = re.sub('ì|í|î|ï', 'i', our_str)   # ì|í|î|ï
    our_str = re.sub('ñ|ň|ń', 'n', our_str)     # ñ|ň|ń
    our_str = re.sub('ò|ó|ô|õ|ö', 'o', our_str) # ò|ó|ô|õ|ö
    our_str = re.sub('š|ś', 's', our_str)       # š|ś
    our_str = re.sub('ù|ú|û|ü', 'u', our_str)   # ù|ú|û|ü
    our_str = re.sub('ý|ÿ', 'y', our_str)       # ù|ú|û|ü
    our_str = re.sub('ž|ź', 'z', our_str)       # ž|ź

    return our_str

