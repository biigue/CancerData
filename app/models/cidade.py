class CidadeObj(db.Model):
    def __init__(self):
        self.idCidade = None
        self.nome = None
        self.latitude = None
        self.longitude = None
        self.Estado_idEstado = None

    def get_idCidade(self):
        return self.idCidade

    def set_idCidade(self, idCidade) :
        self.idCidade = idCidade

    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome) :
        self.nome = nome

    def get_latitude(self):
        return self.latitude
    
    def set_latitude(self, latitude) :
        self.latitude = latitude

    def get_longitude(self):
        return self.longitude
    
    def set_longitude(self, longitude) :
        self.longitude = longitude

    def get_Estado_idEstado(self):
        return self.Estado_idEstado
    
    def set_Estado_idEstado(self, Estado_idEstado) :
        self.Estado_idEstado = Estado_idEstado





