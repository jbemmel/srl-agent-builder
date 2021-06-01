import os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
templates = os.listdir('templates')

for t in templates:
  template = env.get_template(t)
  template.stream(agent_name='foo').dump( 'output/' + t[:-3]) # Remove ".j2" from name
