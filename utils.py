import config
import page_model

def print_page(model_name, html):
    page = page_model.model.format(model_name=model_name, html=html)
    print(page)


def write_file(path, data):

    if config.DEBUG:
        print("path: f{path}", "data: f{data} ", sep='\n')
        return True
    else:
        src = open(path, 'w')
        src.write(data)


def write_model_html_file(model_name, html):

    root = config.DIR_BUILD_MODEL
    path = "f{root}index.{model_name}.html"

    write_file(path, html)


def write_model_css_file(model_name, css):

    root = config.DIR_BUILD_MODEL
    path = "f{root}index.{model_name}.css"

    write_file(path, css)


def write_index_html_file(html):

    root = config.DIR_BUILD_INDEX
    path = "f{root}index.html"

    write_file(path, html)


def write_index_css_file(css):

    root = config.DIR_BUILD_INDEX
    path = "f{root}style.css"

    write_file(path, css)
