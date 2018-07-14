from model.project import Project
import random
import string



def test_delete_project(appl, db):
    if appl.project.count()==0:
        appl.project.create(Project(_name="testname49" + "".join([random.choice(string.digits) for i in range(7)])))
    old_list = db.get_project_list()
    project = random.choice(old_list)
    appl.project.delete_project_by_id(project.id)
    new_list = db.get_project_list()
    old_list.remove(project)
    assert old_list == new_list
    #if check_ui:
    #    def clean(group):
    #        return Group(_id=group.id, _name=appl.clear_dobble_space(group.name.strip()))
    #    new_group_list_ui = appl.group.get_group_list()
    #    assert sorted(map(clean, new_group_list), key=appl.sorted_by_id) == sorted(new_group_list_ui, key=appl.sorted_by_id)