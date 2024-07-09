from sqlalchemy import Column, ForeignKey, Integer, String, Text,Table
from sqlalchemy.orm import declarative_base, relationship
from app import app, db  

# defino las tablas
class Usuario(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    usuario=db.Column(db.Text())
    nombre=db.Column(db.Text())
    apellido=db.Column(db.Text())
    clave=db.Column(db.Integer)
    email=db.Column(db.Text())
    tipo=db.Column(db.Text())
    fecha=db.Column(db.Text())
        
    def __init__(self,usuario,nombre,apellido,clave,email,tipo,fecha):   #crea el  constructor de la clase
        self.usuario=usuario   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.nombre=nombre
        self.apellido=apellido
        self.clave=clave
        self.email=email
        self.tipo=tipo
        self.fecha=fecha
        
with app.app_context():
    db.create_all()  # aqui crea todas las tablas que no encuentre creadas
    