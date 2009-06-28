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

class Node:
    def __init__(self,params):
        """Initialises a node from a dictionary containing the parameters
        provided by the user.
        """
        self.params = params


    def toString(self):
        print self.params
