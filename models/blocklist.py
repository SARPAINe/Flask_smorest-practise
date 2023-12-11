from db import db


class BlockListModel(db.Model):
    __tablename__ ="blocklists"

    id=db.Column(db.Integer,primary_key=True)
    jwt_id=db.Column(db.String(36),index=True, nullable=False)
    created_at=db.Column(db.DateTime,nullable=False)



