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
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, nullable=False)

    attr_lvl = Column(Integer) # your level
    attr_str = Column(Integer) # strength
    attr_dex = Column(Integer) # dexterity
    attr_con = Column(Integer) # constitution
    attr_int = Column(Integer) # intelligence
    attr_wis = Column(Integer) # wisdom
    attr_cha = Column(Integer) # charisma

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def get_lvl(self):
        return int(self.attr_lvl) if self.attr_lvl is not None else 0

    def get_str(self):
        return int(self.attr_str) if self.attr_str is not None else 0
    def set_str(self, val):
        if val is not None:
            self.attr_str = int(val)
        return True

    def get_dex(self):
        return int(self.attr_dex) if self.attr_dex is not None else 0
    def get_con(self):
        return int(self.attr_con) if self.attr_con is not None else 0
    def get_int(self):
        return int(self.attr_int) if self.attr_int is not None else 0
    def get_wis(self):
        return int(self.attr_wis) if self.attr_wis is not None else 0
    def get_cha(self):
        return int(self.attr_cha) if self.attr_cha is not None else 0

    @classmethod
    def find(cls, dbsession, **kwargs):
        username = kwargs.get('username')
        return dbsession.query(User).filter_by(username=username).first()

    def save(self, dbsession):
        dbsession.add(self)
        dbsession.commit()

    # items = relationship("Item", back_populates="user")
