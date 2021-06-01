#!/usr/bin/env python3
# coding=utf-8

import os
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

env = Environment(loader=FileSystemLoader('templates'))
templates = os.listdir('templates')

Path('output').mkdir(parents=True, exist_ok=True)

for t in templates:
  template = env.get_template(t)
  template.stream(agent_name='foo').dump( 'output/' + t[:-3]) # Remove ".j2" from name
