
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
import json
from flask import request

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = "Jackson"

        # example list of members
        self._members = [ {
        "id":self._generateId(),
        "first_name": "Jack",
        "last_name": self.last_name,
        "age": 21,
        "lucky_numbers": [3, 5, 13]
    },
    {
        "id":self._generateId(),
        "first_name": "Josie",
        "last_name": self.last_name,
        "age": 24,
        "lucky_numbers": [7, 21, 35]
    },
    {
        "id":self._generateId(),
        "first_name": "Jolene",
        "last_name": self.last_name,
        "age": 5,
        "lucky_numbers": [1,4,11,14]
    },]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        
        member['last_name'] = self.last_name
        member['id'] = self._generateId()
        
        self._members.append(member)
        # fill this method and update the return
        return None

    def delete_member(self, id):
        # fill this method and update the return
        for pos in range(len(self._members)):
            if self._members[pos]['id'] == int(id):
                self._members.pop(pos)
        return None

    def get_member(self, id):
        for memb in self._members:
            if memb['id'] == int(id):
                return memb
        
        return memb

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
