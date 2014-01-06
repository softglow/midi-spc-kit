from __future__ import print_function, unicode_literals, division, absolute_import
import six
u = six.u

from collections import OrderedDict
from six.moves import configparser
import sys

def read (sources, section, encoding='UTF-8'):
    """Read config file(s) and return the merged general+section config.

    sources is either a string, or a list of such.  section is a string.
    All strings should be Unicode.  All files will be opened with the
    given encoding (Py3) or decoded from it (Py2), in strict error mode."""

    p = configparser.SafeConfigParser()
    if sys.version_info.major == 3 and sys.version_info.minor >= 2:
        ok = p.read(sources, encoding=encoding)
    else:
        ok = []
        if isinstance(sources, six.string_types):
            sources = [ sources ]
        for source in sources:
            fp = codecs.open(source, u('r'), encoding)
            try:
                p.readfp(fp, source)
                ok.append(source)
            except ValueError as e:
                # FIXME: find out if this is the best way to do this
                print(e)
                print(u("Exception occured in config file: {0}").format(source))
            fp.close()
    if not ok:
        raise ValueError(u("No configuration files could be read."))

    d = OrderedDict()
    for s in [u('general'), section]:
        for k, v in p.section(s):
            d[k] = v
    return d
