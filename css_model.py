CSS_ORIGINAL = 'style.css'

with open(CSS_ORIGINAL, 'r') as original:
    model = original.read()

model += """

{css}
"""
