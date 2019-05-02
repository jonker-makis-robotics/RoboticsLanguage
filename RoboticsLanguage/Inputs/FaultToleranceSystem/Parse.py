#
#   This is the Robotics Language compiler
#
#   Parse.py: Parses the  language
#
#   Created on: 08 March, 2019
#       Author: Gabriel Lopes
#      Licence: license
#    Copyright: copyright
#
import sys
import yaml
from lxml import etree
from RoboticsLanguage.Tools import DictionaryToXML
from RoboticsLanguage.Base import Utilities


def parse(text, parameters):
  Utilities.logger.info("Parsing Fault Tolerance system language...")

  # parse JSON into dictionary
  text_dictionary = yaml.safe_load(text)

  # convert dictionary to xml string
  text_xml = DictionaryToXML.dicttoxml(text_dictionary, namespace='fts')

  try:
    # create XML object from xml string
    code = etree.fromstring(text_xml)

  except etree.XMLSyntaxError as error:
    Utilities.logErrors(Utilities.formatLxmlErrorMessage(error, text = text),parameters)
    sys.exit(1)

  # Force output to be Fault Tolerace system
  parameters['globals']['output'] = 'FaultToleranceSystem'

  return code, parameters
