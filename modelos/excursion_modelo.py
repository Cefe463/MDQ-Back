from sqlalchemy import Column, ForeignKey, Integer, String, Text,Table
from sqlalchemy.orm import declarative_base, relationship
from app import app, db  

# defino las tablas
class Excursion(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.Text())
    dias=db.Column(db.Text())
    horario=db.Column(db.Text())
    precio=db.Column(db.Integer)
    maps=db.Column(db.Text())
    info=db.Column(db.Text())
    gps=db.Column(db.Text())
    foto=db.Column(db.Text())
    
    def __init__(self,nombre,dias,horario,precio,maps,info,gps,foto):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.dias=dias
        self.horario=horario
        self.precio=precio
        self.maps=maps
        self.info=info
        self.gps=gps
        self.foto=foto

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
    