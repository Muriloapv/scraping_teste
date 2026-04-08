from app import db 

class Item( db.Model):
   id          = db.column(db.integer, primary_key=true)
   name        = db.column(db.string(100), nullable=false)
   description = db.column(db.string(200), nullable=true)
