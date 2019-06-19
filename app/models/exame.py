class ExameObj():
    def __init__(self, tipo):
        self.idExames = None
        self.tipoDeCancer = tipo
        self.TipoDeExame_idTipoDeExame = None
        self.totalDeExames = None
        self.Estado_idEstado = None
        self.Ano_idAno = None
            
    def get_idExames(self):
        return self.idExames

    def set_idExames(self, idExames) :
        self.idExames = idExames

    def get_tipoDeCancer(self):
        return self.tipoDeCancer
    
    def set_tipoDeCancer(self, tipoDeCancer) :
        self.tipoDeCancer = tipoDeCancer

    def get_TipoDeExame_idTipoDeExame(self):
        return self.TipoDeExame_idTipoDeExame
    
    def set_TipoDeExame_idTipoDeExame(self, TipoDeExame_idTipoDeExame) :
        self.TipoDeExame_idTipoDeExame = TipoDeExame_idTipoDeExame

    def get_totalDeExames(self):
        return self.totalDeExames
    
    def set_totalDeExames(self, totalDeExames) :
        self.totalDeExames = totalDeExames

    def get_Estado_idEstado(self):
        return self.Estado_idEstado
    
    def set_Estado_idEstado(self, Estado_idEstado) :
        self.Estado_idEstado = Estado_idEstado

    def get_Ano_idAno(self):
        return self.Ano_idAno
    
    def set_Ano_idAno(self, Ano_idAno) :
        self.Ano_idAno = Ano_idAno

