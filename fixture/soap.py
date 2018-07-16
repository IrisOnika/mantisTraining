
from suds.client import Client
from suds import WebFault
from model.project import Project

class soapHelper:

    def __init__(self, App):
        self.app = App

    def get_users_projects(self, username, password):
        list = []
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
    #    client.service.mc_login(username, password)
    #    client.factory.create('ProjectData')
        client.service.mc_projects_get_user_accessible(username, password)



        try:
            client.service.mc_projects_get_user_accessible(username, password)
            for row in client.service.mc_projects_get_user_accessible(username, password):
                (id, name, status, inheritGlobal, viewState, description) = row
                list.append(Project(_id=str(id),
                                    _name=name,
                                    _status=status.id,
                                    _inheritGlobal=inheritGlobal,
                                    _viewState=viewState.id,
                                    _description=description))
        except WebFault as e:
            return e
        return list