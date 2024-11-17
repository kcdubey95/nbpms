from extensions import db



class Add_Deal(db.Model):
    __tablename__ = 'gfgfg'
    #colume name
    id = db.Column(db.Integer, primary_key=True)
    mobile_no = db.Column(db.String(10), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=True, unique=True)
    fname = db.Column(db.String(80), nullable=True, unique=False)

    @property
    def data(self):
        return {
            'id': self.id,
            'mobile_no': self.mobile_no,
            'email': self.email,
            'fname': self.fname
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
