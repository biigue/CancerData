class RazaoDeExamesObj():
    def __init__(self):
        self.idRazaoDeExames = None
        self.nota = None
        self.data = None
        self.TipoDeExame_idTipoDeExame =  None
        self.Cidade_idCidade = None

    def get_idRazaoDeExames(self):
        return self.idRazaoDeExames

    def set_idRazaoDeExames(self, idRazaoDeExames) :
        self.idRazaoDeExames = idRazaoDeExames

    def get_nota(self):
        return self.nota
    
    def set_nota(self, nota) :
        self.nota = nota

    def get_data(self):
        return self.data
    
    def set_data(self, data) :
        self.data = data

    def get_TipoDeExame_idTipoDeExame(self):
        return self.TipoDeExame_idTipoDeExame
    
    def set_TipoDeExame_idTipoDeExame(self, TipoDeExame_idTipoDeExame) :
        self.TipoDeExame_idTipoDeExame= = TipoDeExame_idTipoDeExame

    def get_Cidade_idCidade(self):
        return self.Cidade_idCidade
    
    def set_Cidade_idCidade(self, Cidade_idCidade) :
        self.Cidade_idCidade = Cidade_idCidade

    