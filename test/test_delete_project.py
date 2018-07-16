from model.project import Project
import random
import string



def test_delete_project(appl, db):
    if appl.project.count()==0:
        appl.project.create(Project(_name="testname49" + "".join([random.choice(string.digits) for i in range(7)])))
    #old_list = db.get_project_list()
    old_list = appl.soap.get_users_projects("administrator", "root")
    project = random.choice(old_list)
    appl.project.delete_project_by_id(project.id)
    #new_list = db.get_project_list()
    new_list = appl.soap.get_users_projects("administrator", "root")
    old_list.remove(project)
    assert old_list == new_list