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
import os, logging
from contextlib import contextmanager
from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

DB_PATH = 'data/yalg.db'
engine = create_engine(f"sqlite:///{DB_PATH}")
Session = sessionmaker(bind=engine)

def initialize_database():
    if not os.path.exists(os.path.dirname(DB_PATH)):
        os.makedirs(os.path.dirname(DB_PATH))

    BaseModel.metadata.create_all(engine)
    session = Session()

    # Seed db
    # user
    if not session.query(User).filter_by(username='admin').first():
        admin = User(
            username='admin',
            email='admin@yagl.com',
            lvl=1,
            str=10,
            dex=10,
            int=10
        )
        session.add(admin)
        session.commit()

    session.close()


@contextmanager
def dbconn():
    initialize_database()
    session = Session()

    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logging.error(f"dbconn: Session error - {e}")
        raise
    finally:
        session.close()
