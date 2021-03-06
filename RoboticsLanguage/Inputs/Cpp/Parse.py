#
#   This is the Robotics Language compiler
#
#   Parameters.py: Definition of the parameters for this package
#
#   Created on: 19 September, 2018
#       Author: Gabriel Lopes
#      Licence: license
#    Copyright: copyright
#
from lxml import etree

def parse(text, parameters):

  code = etree.Element("cpp")

  code.text = text

  return code, parameters
