"""
Yalg - yet another life game

Copyright (C) 2025  Klinkesorn Nguyen An Hoa

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

Author contactable at k<dot>nguyen<dot>an<dot>hoa<at>gmail<dot>com
"""

class Store():
    """
    State store
    SET: object.attribute = data (any type)
    GET: object.attribute

    - Each storage slot (attribute) will become stale after N GET ops
    - N set on init (default -1) so objects don't expire
    - If objects do expire, stale count is reset on writing to the attribute
    """
    def __init__(self, stale_count=-1):
        object.__setattr__(self, 'store_stale_threshold', stale_count)

    def __getattribute__(self, key):
        # this is to prevent inf recursion as
        # we're overriding __getattribute__
        if key in dir(object):
            return object.__getattribute__(self, key)

        if key == 'store_stale_threshold': raise AttributeError

        k = object.__getattribute__(self, key)['key']
        c = object.__getattribute__(self, key)['stale_count']
        sc = object.__getattribute__(self, 'store_stale_threshold')

        # decrease stale count on read
        object.__setattr__(self, key, {'key': k, 'stale_count': c - 1})

        # reset object value when object is stale
        if object.__getattribute__(self, key)['stale_count'] == 0:
            object.__setattr__(self, key, {'key': [], 'stale_count': sc})

        return object.__getattribute__(self, key)['key']

    def __getattr__(self, key):
        if key == 'store_stale_threshold': raise AttributeError

        sc = object.__getattribute__(self, 'store_stale_threshold')
        object.__setattr__(self, key, {'key': [], 'stale_count': sc})
        return object.__getattribute__(self, key)['key']

    def __setattr__(self, key, val):
        """
        implement safe store attr setter
        replacement assignment only
        writing to store resets stale count
        """
        if key == 'store_stale_threshold': raise AttributeError

        sc = object.__getattribute__(self, 'store_stale_threshold')
        object.__setattr__(self, key, {'key': val, 'stale_count': sc})
