from db import db,BaseModel

class UserModel(BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String,unique=True,nullable=False,server_default="default@example.com")
    password = db.Column(db.String(256), nullable=False)
