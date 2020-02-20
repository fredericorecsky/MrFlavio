#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader

import yaml
import sys, getopt
import pprint

def main():
    inputfile = ''    
    
    try:
        opts, args = getopt.getopt(sys.argv[1:],"p", ["pipeline="])
    except getopt.GetoptError:
        help()
    for opt, arg in opts:
        if opt == '--pipeline':
            inputfile = arg
    
    if inputfile:
        print ( f'Hello World { inputfile }')
        parse_pipeline( inputfile )
    else:
        help()

def help():
    print ('load_pipeline.py --pipeline <yaml pipeline file>')
    sys.exit(2)

def parse_pipeline(pipeline_yml):
    with open( pipeline_yml, "r") as file:
        pipeline = yaml.load(file, Loader=yaml.FullLoader)
        pp = pprint.PrettyPrinter( indent=4 )

        pp.pprint( pipeline )
        # file.seek(0)
        # template_pipeline = file.readlines()

        # file_loader = FileSystemLoader( './' )
        # env = Environment( loader=file_loader)

if __name__ == "__main__":
    main()






    # from jinja2 import Environment, FileSystemLoader
    # import yaml

    # test_value = 'teste'

    # pipeline_file = './examples/pipeline.yml'
    # with open( pipeline_file, "r") as file:

    #     pipeline = yaml.load(file, Loader=yaml.FullLoader)

    #     file.seek(0)
    #     template_pipeline = file.readlines()

    #     file_loader = FileSystemLoader( './' )
    #     env = Environment( loader=file_loader )

    #     # foreach "from" get the namespace from storage
    #     pipeline['from'][0] = test_value
    #     print(pipeline['from'][0])

    #     template = env.get_template( pipeline_file )
    #     c = template.render( pipeline=pipeline )
    #     print(c)
