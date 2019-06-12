class Cidade(db.Model):
    
    __tablename__ = "cidade"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    latitudeELongitude = db.Column(db.String(45), nullable=False)
    


