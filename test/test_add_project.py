# -*- coding: utf-8 -*-
#import pytest
#from data.groups import test_data
from model.project import Project
import time


def test_add_project(appl, db):

    time.sleep(10)






#    group=json_groups                                           #json_groups - fixture for test generator usage
    #old_group_list = appl.group.get_group_list()    #takes a list from ui
#    old_group_list = db.get_group_list()
    #print("old_group_list1 lenth = "+str(len(old_group_list1)))
#    appl.group.create(group)
   # assert len(old_group_list) + 1 == appl.group.count()        #is need only for uimatches (as heshing)
#    new_group_list = db.get_group_list()
#    old_group_list.append(group)
#    assert old_group_list == new_group_list
#    if check_ui:
#        def clean(group):
#            return Group(_id=group.id, _name=appl.clear_dobble_space(group.name.strip()))
#        new_group_list_ui = appl.group.get_group_list()
#        assert sorted(map(clean, new_group_list), key=appl.sorted_by_id) == sorted(new_group_list_ui, key=appl.sorted_by_id)