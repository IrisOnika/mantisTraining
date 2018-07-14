class Project():

    def __init__(self,  _name=None, _status=None, _inheritGlobal=None, _viewState=None, _description=None, _id=None):
        self.name=_name
        self.status = _status
        self.inheritGlobal = _inheritGlobal
        self.viewState = _viewState
        self.description = _description
        self.id = _id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.name, self.status, self.inheritGlobal, self.viewState, self.description)

    def __eq__(self, other):
        return (self.id == other.id or self.id == None or other.id == None) and self.name == other.name