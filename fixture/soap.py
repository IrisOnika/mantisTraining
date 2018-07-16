
from suds.client import Client
from suds import WebFault
from model.project import Project

class soapHelper:

    def __init__(self, App):
        self.app = App

    def get_users_projects(self, username, password):
        list = []
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")

        try:
            client.service.mc_projects_get_user_accessible(username, password)
            for row in client.service.mc_projects_get_user_accessible(username, password):
                (ProjectData) = row
                list.append(Project(_id=str(ProjectData['id']),
                                    _name=ProjectData['name'],
                                    _status=ProjectData['status']['id'],
                                    _viewState=ProjectData['view_state']['id'],
                                    _description=ProjectData['description']))
        except WebFault as e:
            return e
        return list