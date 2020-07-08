
model_a = """
/* {icon_name} */

.{title}-badge {{}}
.{title}-left {{
  color: #{hex_color_left};
  background-color: #{hex_bgcolor_left};
}}
.{title}-right {{
  color: #{hex_color_right};
  background-color: #{hex_bgcolor_right};
}}

"""

# let's get our badge models and register them
self = locals()
MODEL_REGISTRY = {"_".join(key.split('_')[1:]): value
                  for key, value in self.items() if key.startswith('model_')}
