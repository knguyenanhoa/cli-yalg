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
import char_model

@navigable_menus.nav_stack
def login(NAVSTACK, STATE):
    navigable_menus.make_header('main > login')

    if STATE.logged_in == True:
        return main_menu.back(NAVSTACK, STATE)

    username = input('Who are you?: ')
    if username == '':
        return main_menu.back(NAVSTACK, STATE)

    char = char_model.Base(username=username)

    cur = STATE._dbconn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )
    result = cur.fetchone()
    if result != None:
        STATE.char
        print(result)
        exit()
        STATE.logged_in = True

    return main_menu.back(NAVSTACK, STATE)
