from app import db        

class Estado(db.Model):
    __tablename__ = "estados"

    idEstado = db.Column("idEstado", db.Integer, primary_key=True, nullable=False)
    nome = db.Column("nome", Text)
    sigla = db.Column("sigla", Text, nullable=False)

    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = email

    def __repr__(self):
        return '<Estado %r>' % self.nome

class TipoDeExame(db.Model):
    __tablename__ = "tiposDeExames"

    idTipoDeExame = db.Column("idTipoDeExame", db.Integer, primary_key=True, nullable=False)
    tipoDeExame = db.Column("tipoDeExame", db.Text)

    def __init__(self, TipoDeExame):
        self.tipoDeExame = TipoDeExame

    def __repr__(self):
        return '<TipoDeExame %r>' % self.tipoDeExame
    
class Ano(db.Model):
    __tablename__ = "anos"

    idAno = db.Column("idAno", db.Integer, primary_key=True, nullable=False)
    ano = db.Column("ano", db.Integer, nullable=True)

    def __init__(self, ano):
        self.ano = ano

    def __repr__(self):
        return '<Ano %r>' % self.ano

class Exame(db.Model):
    __tablename__ = "exames"

    idExames = db.Column("idExames", db.Integer, primary_key=True, nullable=False)
    totalDeExames = db.Column("totalDeExames", db.Integer, nullable= False)
    tipoDeCancer = db.Column("tipoDeCancer", db.String(254), nullable= False)
    Estado_idEstado = db.Column("Estado_idEstado", db.Integer, nullable= False, ForeignKey(Estado.idEstado))
    TipoDeExame_idTipoDeExame=  db.Column("TipoDeExame_idTipoDeExame", db.Integer, nullable= False, ForeignKey(TipoDeExame.idTipoDeExame))
    Ano_idAno = db.Column("Ano_idAno", db.Integer, nullable= False, ForeignKey(Ano.idAno))

    def __init__(self, totalDeExames,tipoDeCancer,Estado_idEstado,TipoDeExame_idTipoDeExame,Ano_idAno):
        self.totalDeExames = totalDeExames
        self.tipoDeCancer = tipoDeCancer
        self.Estado_idEstado = Estado_idEstado
        self.TipoDeExame_idTipoDeExame = TipoDeExame_idTipoDeExame
        self.Ano_idAno = Ano_idAno

    def __repr__(self):
        return '<Exame %r>' % self.tipoDeCancer


class Mortalidade(db.Model):
    __tablename__ = "mortalidades"

    idMortalidade = db.Column("idMortalidade", db.Integer, primary_key=True, nullable=False)
    numeroDeCasos = db.Column("numeroDeCasos", db.Integer, nullable= False)
    tipoDeCancer = db.Column("tipoDeCancer", db.String(254), nullable= False)
    raca = db.Column("raca", db.String(254), nullable= False)
    FaixaEtaria = db.Column("FaixaEtaria", db.String(254), nullable= False)
    Ano_idAno = db.Column("Ano_idAno", db.Integer, nullable= False, ForeignKey(Ano.idAno))

     def __init__(self, numeroDeCasos,tipoDeCancer,raca,FaixaEtaria,Ano_idAno):
        self.totalDeExames = totalDeExames
        self.numeroDeCasos =  numeroDeCasos
        self.tipoDeCancer = tipoDeCancer
        self.raca = raca
        self.FaixaEtaria = FaixaEtaria
        self.Ano_idAno = Ano_idAno

    def __repr__(self):
        return '<Mortalidade %r>' % self.tipoDeCancer

class MamografosPorUF(db.Model):
    __tablename__ = "mamografosPorUF"

    idMamografosPorUF = db.Column("idMamografosPorUF", db.Integer, primary_key=True, nullable=False)
    quantidadeSUS = db.Column("quantidadeSUS", db.Integer, nullable= False)
    quantidadeNaoSUS = db.Column("quantidadeSUS", db.Integer, nullable= False)
    Estado_idEstado = db.Column("Estado_idEstado", db.Integer, nullable= False, ForeignKey(Estado.idEstado))

    def __init__(self, quantidadeSUS, quantidadeNaoSUS, Estado_idEstado):
        self.quantidadeSUS = quantidadeSUS
        self.quantidadeNaoSUS = quantidadeNaoSUS
        self.Estado_idEstado = Estado_idEstado

    def __repr__(self):
        return '<MamografosPorUF %r>' % self.quantidadeSUS

    

class Cidade(db.Model):
    __tablename__ = "cidades"

    idCidade = db.Column("idCidade", db.Integer, primary_key=True, nullable=False)
    nome = db.Column("nome", db.String(254), nullable= False)
    latitude = db.Column("latitude", db.String(254), nullable= False)
    longitude = db.Column("longitude", db.String(254), nullable= False)
    Estado_idEstado = db.Column("Estado_idEstado", db.Integer, nullable= False, ForeignKey(Estado.idEstado))

    def __init__(self, nome, latitude,longitude, Estado_idEstado):
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude
        self.Estado_idEstado = Estado_idEstado

    def __repr__(self):
        return '<Cidade %r>' % self.nome
    

class RazaoDeExames(db.Model):
    __tablename__ = "razaoDeExames"

    idRazaoDeExames = db.Column("idRazaoDeExames", db.Integer, primary_key=True, nullable=False)
    nota = db.Column("longitude", db.Float, nullable= False)
    data = db.Column("data", db.String(254), nullable=False)
    TipoDeExame_idTipoDeExame=  db.Column("TipoDeExame_idTipoDeExame", db.Integer, nullable= False, ForeignKey(TipoDeExame.idTipoDeExame))
    Cidade_idCidade = db.Column("Cidade_idCidade", db.Integer, nullable= False, ForeignKey(Cidade.Cidade_idCidade))

     def __init__(self, nota, data, TipoDeExame_idTipoDeExame, Cidade_idCidade):
        self.nota = nota
        self.data = data
        self.TipoDeExame_idTipoDeExame = TipoDeExame_idTipoDeExame
        self.Cidade_idCidade = Cidade_idCidade

    def __repr__(self):
        return '<Razao de Exames %r>' % self.nota
