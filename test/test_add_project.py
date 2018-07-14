# -*- coding: utf-8 -*-
#import pytest
#from data.groups import test_data
from model.project import Project
#import time
import string
import random


def test_add_project(appl, db):
    project=Project(_name="testname99" + "".join([random.choice(string.digits) for i in range(7)]))
    #old_list = appl.project.get_project_list()
    old_list = db.get_project_list()
    appl.project.create(project)
    #new_list = appl.project.get_project_list()
    new_list = db.get_project_list()
    old_list.append(project)
    assert old_list == new_list
    #assert sorted(old_list, key=appl.sorted_by_id) == sorted(new_list, key=appl.sorted_by_id)

