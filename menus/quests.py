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
def quests(NAVSTACK, STATE):
    char = STATE.curr_user

    quest_list = [
        ('quests', 'chores'),
        ('quests', 'study')
    ]

    content = """
    Choose from the quests above
    """

    action, STATE = navigable_menus.create(
        quest_list + [
            ('main_menu', 'back'),
            ('main_menu', 'back_to_main')
        ],
        header='> quests',
        STATE=STATE,
        after_content=content
    )
    return action, NAVSTACK, STATE

@navigable_menus.nav_stack
def chores(NAVSTACK, STATE):
    char = STATE.curr_user

    content = """
    Do any chores 5 times
    """

    action, STATE = navigable_menus.create(
        [
            ('main_menu', 'back'),
            ('main_menu', 'back_to_main')
        ],
        header='> quests > chores',
        STATE=STATE,
        after_content=content
    )
    return action, NAVSTACK, STATE

@navigable_menus.nav_stack
def study(NAVSTACK, STATE):
    char = STATE.curr_user

    content = """
    Do any study 5 times
    """

    action, STATE = navigable_menus.create(
        [
            ('main_menu', 'back'),
            ('main_menu', 'back_to_main')
        ],
        header='> quests > study',
        STATE=STATE,
        after_content=content
    )
    return action, NAVSTACK, STATE
