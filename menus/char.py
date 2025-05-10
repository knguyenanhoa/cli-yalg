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
def char(NAVSTACK, STATE):
    """
    This is the index for this menu
    """
    actions = [
        ('char', 'stats'),
    ]

    action, STATE = navigable_menus.create(
        actions + [
            ('main_menu', 'back'),
            ('main_menu', 'back_to_main')
        ],
        header='> char',
        STATE=STATE
    )
    return action, NAVSTACK, STATE

@navigable_menus.nav_stack
def stats(NAVSTACK, STATE):
    char = STATE.curr_user

    content = """
    Username: {username} (Lv. {lvl})

    STR: {str:03} (Physical power)
    DEX: {dex:03} (Agility, reflexes)
    CON: {con:03} (Endurance)
    INT: {int:03} (Logic, memory, knowledge)
    WIS: {wis:03} (Perception, insight)
    CHA: {cha:03} (Social skills)
    """.format(
        username=char.username,
        lvl=char.get_lvl(),
        str=char.get_str(),
        dex=char.get_dex(),
        con=char.get_con(),
        int=char.get_int(),
        wis=char.get_wis(),
        cha=char.get_cha(),
    )

    action, STATE = navigable_menus.create(
        [
            ('char', 'set_str'),
            ('main_menu', 'back'),
            ('main_menu', 'back_to_main')
        ],
        header='> char > stats',
        STATE=STATE,
        after_content=content
    )
    return action, NAVSTACK, STATE

@navigable_menus.nav_stack
def set_str(NAVSTACK, STATE):
    navigable_menus.make_header('> char > stats > set str')
    char = STATE.curr_user

    new_str = input("""
    Current STR: {str:03} (Physical power)
    New STR?
    """.format(
        str=char.get_str(),
    ))

    char.set_str(int(new_str))
    char.save(STATE._dbsession)

    return ('main_menu', 'back'), NAVSTACK, STATE
