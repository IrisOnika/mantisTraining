from model.project import Project
import re

class projectHelper:
    def __init__(self, App):
        self.app = App

    # create progect method
    def create(self, Project):
        self.open_projects_page()
        self.app.click_button(value="Create New Project")
        self.set_project_fields(Project)
        self.app.click_button(value="Add Project")
        self.open_projects_page()
        self.projectListCache = None

    def open_projects_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/manage_proj_page.php") and len(wd.find_elements_by_name("manage_proj_create_page_token"))>0:
            return
        self.app.navigation.openMenu("Manage")
        self.app.navigation.openMenu("Manage Projects")

    # -''-
    def set_project_fields(self, Project):
        self.app.set_text_field("name", Project.name)
        if Project.status is not None:
            self.app.set_select_field("status", Project.status)
        if Project.viewState is not None:
            self.app.set_select_field("view_state", Project.viewState)
        self.app.set_text_field("description", Project.description)

    projectListCache = None

    def get_project_list(self):
        if self.projectListCache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.projectListCache = []
            project_table = wd.find_element_by_xpath("//table[tbody/tr/td/form/input[@value='Create New Project']]")
            for i in project_table.find_elements_by_css_selector("tr.row-1")+project_table.find_elements_by_css_selector("tr.row-2"):
                name = i.find_element_by_xpath("td/a").text
                link = i.find_element_by_xpath("td/a").get_attribute("href")
                all_d = re.findall(r'\d+', link)
                id = all_d[len(all_d)-1]
                self.projectListCache.append(Project(_name=name, _id=id))
        return list(self.projectListCache)

    def count(self):
        wd = self.app.wd
        self.open_projects_page()
        project_table = wd.find_element_by_xpath("//table[tbody/tr/td/form/input[@value='Create New Project']]")
        return len(project_table.find_elements_by_css_selector("tr.row-1")+project_table.find_elements_by_css_selector("tr.row-2"))


    def delete_project_by_id(self, id):
        self.open_projects_page()
        self.open_project_by_id(id)
        self.delete_project_acception()
        self.open_projects_page()
        self.groupListCache = None

    def open_project_by_id(self, id):
        wd = self.app.wd
        project_table = wd.find_element_by_xpath("//table[tbody/tr/td/form/input[@value='Create New Project']]")
        project_table.find_element_by_xpath("//td/a[@href='manage_proj_edit_page.php?project_id=" +id +"']").click()

    def delete_project_acception(self):
        self.app.click_button(value="Delete Project")
        self.app.click_button(value="Delete Project")



















#FROM ANOTHER PROJECT
    # edit group method
    def edit(self, Group, index):
        self.open_groups_page()
        self.select_group(index)           #self.select_first_group()
        self.app.click_button("edit")
        self.set_group_fields(Group)
        self.app.click_button("update")
        self.app.navigation.openMenu("groups")
        self.groupListCache = None

    def edit_by_id(self, Group, id):
        self.open_groups_page()
        self.select_group_by_id(id)           #self.select_first_group()
        self.app.click_button("edit")
        self.set_group_fields(Group)
        self.app.click_button("update")
        self.app.navigation.openMenu("groups")
        self.groupListCache = None

    # delete group method
    def delete(self, index):
        self.open_groups_page()
        self.select_group(index)           #self.select_first_group()
        self.app.click_button("delete")
        self.app.navigation.openMenu("groups")
        self.groupListCache = None

    def delete_group_by_id(self, id):
        self.open_projects_page()
        self.select_group_by_id(id)  # self.select_first_group()
        self.app.click_button("delete")
        self.app.navigation.openMenu("groups")
        self.groupListCache = None

    #-''-


    # -''-
    def select_first_group(self):
        self.select_group(0)

    def select_group(self, index):
        wd = self.app.wd
        if not wd.find_elements_by_name("selected[]")[index].is_selected():
            wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        if not wd.find_element_by_css_selector("input[value='%s']" % id).is_selected():
            wd.find_element_by_css_selector("input[value='%s']" % id).click()


