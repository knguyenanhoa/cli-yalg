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


import sys, os, copy, logging, atexit

# THESE ARE USED, DO NOT REMOVE
# maybe implement an autoloader here....
from menus import *
from models import *
from components import navigable_menus, store
import db

def route(action, NAVSTACK, STATE):
    action, NAVSTACK, STATE = getattr(
        globals()[action[0]],
        action[1]
    )(NAVSTACK, STATE)
    return action, NAVSTACK, STATE

def init(debug=False):
    if not debug:
        def switch_screen(name='MAIN'):
            screens = {
                "ALT": "\x1b[?1049h",
                "MAIN": "\x1b[?1049l"
            }
            sys.stdout.write(screens[name])
            sys.stdout.flush()

        atexit.register(switch_screen, 'MAIN')
        switch_screen('ALT')

    # setup folder struct
    try:
        os.mkdir("./data")
        os.mkdir("./logs")
    except:
        pass

    # check dependencies
    try:
        import requests
    except:
        print('dependencies not satisfied')

    # logs
    logging.basicConfig(
        filename='./logs/development.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

if __name__ == '__main__':
    init(debug=True)
    with db.dbconn() as dbsession:
        os.system('clear')
        navigable_menus.make_header('welcome to yalg. initializing...')

        NAVSTACK = [('main_menu', 'main')]
        STATE = store.Store()
        STATE._dbsession = dbsession
        STATE.curr_user = None

        os.system('clear')
        action, NAVSTACK, STATE = main_menu.main(NAVSTACK, STATE)

        while True:
            action, NAVSTACK, STATE = route(action, NAVSTACK, STATE)
