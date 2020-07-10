
#for key, value in self.items():
#    if key.startswith('model_'):
#        model_name = key.split('_', maxsplit=1)[1]
#        MODEL_REGISTRY.update({model_name: value})

model_a = """
<!--

{icon_name}

-->
<div class="badge badge-{model} {title}-{model}-badge">
  <div class="left left-{model} {title}-{model}-left">{svg}</div>
  <div class="right right-{model} {title}-{model}-right">{title}</div>
</div>
"""

model_b = """
<!--

{icon_name}

-->
<div class="badge badge-{model} {title}-{model}-badge">
  <div class="left left-{model} {title}-{model}-left">{svg}</div>
  <div class="right right-{model} {title}-{model}-right">{icon_name}</div>
</div>
"""

model_c = model_b

# let's get our badge models and register them
self = locals()
MODEL_REGISTRY = {"_".join(key.split('_')[1:]): value
                  for key, value in self.items() if key.startswith('model_')}
