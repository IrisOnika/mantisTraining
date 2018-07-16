# -*- coding: utf-8 -*-
from model.project import Project
#import time
import string
import random


def test_add_project(appl, db):
    project=Project(_name="testname99" + "".join([random.choice(string.digits) for i in range(7)]))
    #old_list = appl.project.get_project_list()                         #get projects list from ui
    #old_list = db.get_project_list()                                   #get projects list from db
    old_list = appl.soap.get_users_projects("administrator", "root")
    appl.project.create(project)
    #new_list = appl.project.get_project_list()                         #get projects list from ui
    #new_list = db.get_project_list()                                   #get projects list from db
    new_list = appl.soap.get_users_projects("administrator", "root")
    old_list.append(project)
    #assert old_list == new_list
    assert sorted(old_list, key=appl.sorted_by_id) == sorted(new_list, key=appl.sorted_by_id)       #is actual for ui and soap tests

