class Cidade(db.Model):

    __tablename__ = "cidade"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    latitudeELongitude = db.Column(db.String(45), nullable=False)

    def __init__(self, id, nome, latitudeELongitude):
        self.id = id
        self.nome = nome
        self.latitudeELongitude = latitudeELongitude
    
    


