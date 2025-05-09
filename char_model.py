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

import logging
from components import store

class CharModel():
    state = store.Store()

    def __init__(self, dbconn=None):
        if dbconn is None:
            logging.error('unable to connect to db')
            return None

        self.state.name = 'ignoi'
        self.state.lvl = 10
        self.state.stats = {
            "str": 100,
            "dex": 50,
            "int": 200,
        }

    def name(self): return self.state.name
    def lvl(self): return self.state.lvl
    def stats(self): return self.state.stats
