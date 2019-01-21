#! /usr/bin/env python
"""Send HTTP messages
"""

import sys
import os
import optparse
import coloredlogs
import logging
import json
from os import listdir
from os.path import isfile, join
import json
import dicttoxml
from cryptography.fernet import Fernet
import requests

def main():
    """Main entry point.
    """
    parser = optparse.OptionParser()

    parser.add_option('-v', '--verbose',
                      action="store_true", dest="verbose",
                      help="Show debug logs", default=False)

    options, args = parser.parse_args()

    logger = logging.getLogger()
    
    coloredlogs.install(level='DEBUG' if options.verbose else 'INFO')

    logger.info('Starting sender...')
    logger.debug(options)

    url_to_post = os.environ['POST_URL']

    dir_path = '/work'
    key = 'AQZKgmen1zFKjyi0_IYvGb46P2F5ieNxm3qkHwzn4pg='

    json_files = [f for f in listdir(dir_path) if f.endswith('.json')]

    logger.debug(json_files)

    for file in json_files:
        with open(dir_path + '/' + file, 'r') as f:
            json_data = json.load(f)
            xml = dicttoxml.dicttoxml(json_data)
            logger.debug(xml)
            
            logger.debug(key)
            cipher_suite = Fernet(key)
            cipher_text = cipher_suite.encrypt(xml)
            logger.debug(cipher_text)
            r = requests.post(url_to_post, data=cipher_text)
            logger.info(r.status_code)

if __name__ == "__main__":
    sys.exit(main())
