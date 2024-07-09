from flask import  jsonify,request  # del modulo flask importar los métodos jsonify,request

from app import app, db, ma
from modelos.excursion_modelo import *

class ExcursionSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','dias','horario','precio','maps','info','gps','foto')

excursion_schema=ExcursionSchema() # El objeto excursion_schema es para traer una excursion
excursiones_schema=ExcursionSchema(many=True)  # El objeto excursiones_schema es para traer multiples registros de excuirsion

# se crean los endpoint o rutas (json)

@app.route('/excursiones',methods=['GET'])
def get_Excursiones():
    all_excursiones=Excursion.query.all()         # el metodo query.all() lo hereda de db.Model
    result=excursiones_schema.dump(all_excursiones)  # el metodo dump() lo hereda de ma.schema y
                                              # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla

@app.route('/excursiones/<id>',methods=['GET'])
def get_excursion(id):
    excursion=Excursion.query.get(id)
    return excursion_schema.jsonify(excursion)   # retorna el JSON de una excursión recibido como parametro

@app.route('/excursiones/<id>',methods=['DELETE'])
def delete_excursion(id):
    excursion=Excursion.query.get(id)
    db.session.delete(excursion)
    db.session.commit()
    return excursion_schema.jsonify(excursion)   # me devuelve un json con el registro eliminado

@app.route('/excursiones', methods=['POST']) # crea ruta o endpoint
def create_excursion():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    dias=request.json['dias']
    horario=request.json['horario']
    precio=request.json['precio']
    maps=request.json['maps']
    info=request.json['info']
    gps=request.json['gps']
    foto=request.json['foto']
    new_excursion=Excursion(nombre,dias,horario,precio,maps,info,gps,foto)
    db.session.add(new_excursion)
    db.session.commit()
    return excursion_schema.jsonify(new_excursion)

@app.route('/excursiones/<id>' ,methods=['PUT'])
def update_excursion(id):
    excursion=Excursion.query.get(id)
    excursion.nombre=request.json['nombre']
    excursion.dias=request.json['dias']
    excursion.horario=request.json['horario']
    excursion.precio=request.json['precio']
    excursion.maps=request.json['maps']
    excursion.info=request.json['info']
    excursion.gps=request.json['gps']
    excursion.foto=request.json['foto']
    

    db.session.commit()
    return excursion_schema.jsonify(excursion)

@app.route('/')
def bienvenida():
    return "Bienvenidos al backend"   # retorna el JSON de un usuario recibido como parametro