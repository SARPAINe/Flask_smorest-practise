from db import db,BaseModel


class StoreModel(BaseModel):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic",cascade="all, delete")
    # here store is the name of the property in ItemModel table
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")