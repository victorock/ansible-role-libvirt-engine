# (c) 2018, Victor da Costa <victorockeiro@gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from xmltodict import unparse as JSONXMLEncoder
from ansible.module_utils._text import to_bytes, to_text

def to_xml(a, *args, **kw):
    return badgerfish_to_xml(a, *args, **kw)

def badgerfish_to_xml(a, *args, **kw):
    '''Convert the JSON value to XML'''
    return to_text( JSONXMLEncoder( a, pretty=True, attr_prefix='@', cdata_key='$' ) )

class FilterModule(object):
    """Filters for libvirt"""

    filter_map = {
        'to_xml': to_xml,
        'badgerfish_to_xml': badgerfish_to_xml
    }

    def filters(self):
        return self.filter_map
