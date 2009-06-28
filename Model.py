#!/usr/bin/python
###########################################################################
# NAME: OpenProc: Model Class
# DESC: This class is used to store the basic description of an
#       OpenProc model.
#       It includes arrays of other classes that store the model data
#       and functions to import and export the model data to/from a file.
#
#
###########################################################################
# Copyright 2009 Graham Jones
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#---------------------------------------------------------------------------
import sys
import os
from xml.sax import make_parser, handler
import xml
import re

from Node import Node
from Link import Link

class Model(handler.ContentHandler):
    """The Model class stores the OpenProc model data (nodes, links,
    constants, data arrays etc.
    It provides a parser to initialise the model from an XML file, and to
    write the model back to an XML file.
    """
    def __init__(self,fname):
        self.debug = True
        if (self.debug): print "Model.__init__() - fname=%s\n" % fname

        self.Nodes = []
        self.Links = []


        self.inModel = False
        self.inNode  = False
        self.inLink  = False
        self.inConst = False
        self.inVector = False
        self.in2dArray = False
        
        
        if(fname != None):
            self.readXML(fname)
        else:
            if (self.debug): print "No filename given - creating empty model\n"


        for node in self.Nodes:
            node.toString()

#        self.writeXML(fname)

    def readXML(self,fname):
        """Load an XML file describing a model into memory"""
        self.params = {}
        if (self.debug): print "Model.__readXML() - fname=%s\n" % fname

        if (not os.path.exists(fname)):
            print "Error - File %s does not exist." % filename
            return
        try:
            parser = make_parser()
            parser.setContentHandler(self)
            parser.parse(fname)
            self.fname = fname
        except xml.sax._exceptions.SAXParseException:
            print "ErrorLoading %s" % fname


    def startElement(self,name,attrs):
        """Handle XML elements"""
        if (self.debug): print "startElement() -name=%s, atrrs=%s" %\
           (name,attrs.getNames())
        if name=="node":
            if (self.debug): print "Node.."
            self.inNode = True
            self.initParam(attrs)        
        if name=="link":
            if (self.debug): print "Link.."
            self.inLink = True
            self.initParam(attrs)
        self.eleName = name

    def initParam(self,attrs):
        if (self.debug): print "initParam - attrs=%s" % attrs.getNames()
        self.params = {}
        if attrs.getLength()>0:
            for name in attrs.getNames():
                self.params[name] = attrs.getValue(name)

        
    def characters(self,content):
        """Process the characters stored in an XML element"""
        if (self.debug): print "characters() - content=%s" % content
        if self.inNode or self.inLink:
            if (self.debug): print "setting parameter %s to %s." %\
                (self.eleName,content)
            self.params[self.eleName] = content

    def endElement(self,name):
        """Handle finding the end of an XML element"""
        if (self.debug): print "endElement - name=%s" % name
        if (self.debug): print self.params
        if (self.inNode):
            node = Node(self.params)
            self.Nodes.append(node)
            self.inNode = False
        if (self.inLink):
            link = Link(self.params)
            self.Links.append(link)
            self.inLink = False

    def writeXML(self,fname):
        if (self.debug): print "Model.__writeXML() - fname=%s\n" % fname
        


if __name__ == "__main__":
    print "OpenProc Model.py module __main__ test code argc=%d." % len(sys.argv)
    if (len(sys.argv) > 1):
        fname = sys.argv[1]
    else:
        fname = None
    model = Model(fname)
    
        
    

        
