#!/usr/bin/env python
import os
import configparser

if __name__ == '__main__':
    repo_dir = os.path.dirname(os.path.realpath(__file__))

    # Load env variables from .env config file
    cp = configparser.SafeConfigParser()
    cp.read(os.path.join(repo_dir, ".env"))

    # Load the files variables into the environment
    for i in cp.items('stuff'):
        os.environ[i[0].upper()] = i[1]

    # Start the flask dev server
    from sampleslack import run_app
    run_app()
