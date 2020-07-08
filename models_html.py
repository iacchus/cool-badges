
#for key, value in self.items():
#    if key.startswith('model_'):
#        model_name = key.split('_', maxsplit=1)[1]
#        MODEL_REGISTRY.update({model_name: value})

model_a = """
<!--

{icon_name}

-->
<div class="box">
  <div class="badge {title}-badge">
    <div class="left {title}-left"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/{title}.svg" /></div>
    <div class="right {title}-right">{title}</div>
  </div>
</div>

"""

# let's get our badge models and register them
self = locals()
MODEL_REGISTRY = {"_".join(key.split('_')[1:]): value
                  for key, value in self.items() if key.startswith('model_')}
