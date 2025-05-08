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

import sys, time, os, copy

from components import navigable_menus
from menus import main_menu

@navigable_menus.nav_stack
def char(NAVSTACK, STATE):
    categories = [
        ('char', 'stats'),
    ]

    action, STATE = navigable_menus.create(
        categories + [
            ('main_menu', 'back'),
            ('main_menu', 'back_to_main')
        ], header='char > index', STATE=STATE
    )
    return action, NAVSTACK, STATE

@navigable_menus.nav_stack
def stats(NAVSTACK, STATE):
    content = """
    Name: {name}

    Str: {str}
    Dex: {dex}
    Int: {int}
    """.format(
        name='test',
        str=50,
        dex=100,
        int=200,
    )

    action, STATE = navigable_menus.create(
        [
            ('main_menu', 'back'),
            ('main_menu', 'back_to_main')
        ],
        header='char > stats',
        STATE=STATE,
        after_content=content
    )
    return action, NAVSTACK, STATE
