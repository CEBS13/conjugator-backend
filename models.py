from app import db


class Verb(db.Model):
    __tablename__ = 'verb'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Integer)
    infinitif = db.Column(db.String(30))
    participe_passe = db.Column(db.String(30))
    fps_ip = db.Column(db.String(50), nullable=True)
    sps_ip = db.Column(db.String(50), nullable=True)
    tps_ip = db.Column(db.String(50), nullable=True)
    fpp_ip = db.Column(db.String(50), nullable=True)
    spp_ip = db.Column(db.String(50), nullable=True)
    tpp_ip = db.Column(db.String(50), nullable=True)
    fps_ii = db.Column(db.String(50), nullable=True)
    sps_ii = db.Column(db.String(50), nullable=True)
    tps_ii = db.Column(db.String(50), nullable=True)
    fpp_ii = db.Column(db.String(50), nullable=True)
    spp_ii = db.Column(db.String(50), nullable=True)
    tpp_ii = db.Column(db.String(50), nullable=True)
    
    def __repr__(self):
        return '<id {}>'.format(self.id)

    