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
