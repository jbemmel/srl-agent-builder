#!/usr/bin/env python3
# coding=utf-8

import os, sys, getopt, re
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def main(argv):
   agent_name = ''
   output_folder = 'output'
   try:
      opts, args = getopt.getopt(argv,"hn:o:",["name=","outputfolder="])
   except getopt.GetoptError:
      print( 'build_agent.py -n <agentname> -o <outputfolder>' )
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print( 'build_agent.py -n <agentname> -o <outputfolder>' )
         sys.exit()
      elif opt in ("-n", "--name"):
         agent_name = arg
      elif opt in ("-o", "--outputfolder"):
         output_folder = arg

   if (agent_name==""):
       print( 'Missing mandatory agent name' )
       sys.exit(3)

   print( f'Agent name: {agent_name}' )
   print( f'Output folder is {output_folder}' )

   env = Environment(loader=FileSystemLoader('templates'))
   templates = os.listdir('templates')

   Path(output_folder).mkdir(parents=True, exist_ok=True)

   for t in templates:
     template = env.get_template(t)
     ext = re.match("^.*(\..*)\.j2$",t)
     if ext:
       filename = agent_name + ext.groups()[0]
     else:
       filename = t[0:-3] # remove ".j2"
     template.stream(agent_name=agent_name).dump( output_folder + '/' + filename )

if __name__ == "__main__":
   main(sys.argv[1:])
