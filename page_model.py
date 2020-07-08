HTML_ORIGINAL = 'base-index.html'

CSS_INJECTION_TAG = '<!--CSS-GOES-HERE-->'
HTML_INJECTION_TAG = '<!--HTML-GOES-HERE-->'
CSS_STR = (5*' ' + '<link href="style.{model_name}.css" '
               'rel="stylesheet" type="text/css" />')
HTML_STR = "{html}"

with open(HTML_ORIGINAL, 'r') as original:
    pre_model = original.read()

pre_model = pre_model.replace(CSS_INJECTION_TAG, CSS_STR)
model = pre_model.replace(HTML_INJECTION_TAG, HTML_STR)
