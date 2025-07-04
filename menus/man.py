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

from components import navigable_menus
from menus import main_menu

@navigable_menus.nav_stack
def man(NAVSTACK, STATE):
    navigable_menus.make_header('> man')
    print(' ')
    print('Navigation is vim-like')
    print('UP:  k       DOWN:   j      LEFT: h      RIGHT: l')
    print('TOP: K, gg   BOTTOM: J, G')
    print(' ')
    print('SELECT: o, <CR>')
    print('BACK:   q')
    print('EXIT:   <Esc> (works on most screens)')
    print('        if all else fails, Ctrl + C')
    print('-----------------------------------------------')
    print('Press any key to return')

    navigable_menus.getch()
    return ('main_menu', 'back'), NAVSTACK, STATE
