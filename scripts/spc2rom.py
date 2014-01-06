#!/usr/bin/env python
# vim: fileencoding=utf8

# spc2rom: import NSPC track to unheadered game ROM
# Copyright (C) 2014 softglow <https://github.com/softglow>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.  You may not use any
# earlier or later version of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function, unicode_literals, division, absolute_import
import six

# stdlib
import argparse
import os
import sys

# local
from midi_spc import *


def main (args=None, argv0='spc2rom.py'):
    pass

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:], sys.argv[0]))

