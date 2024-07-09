from flask import  jsonify,request  # del modulo flask importar los métodos jsonify,request

from app import app, db, ma
from modelos.usuario_modelo import *

class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('id','usuario','nombre','apellido','clave','email','tipo','fecha')

usuarios_schema_schema=UsuarioSchema() # El objeto usuarios_schema_schema es para traer una usuario
usuarios_schema=UsuarioSchema(many=True)  # El objeto usuarios_schema es para traer multiples registros de excuirsion

# se crean los endpoint o rutas (json)

@app.route('/usuarios',methods=['GET'])
def get_Usuarios():
    all_usuarios=Usuario.query.all()         # el metodo query.all() lo hereda de db.Model
    result=usuarios_schema.dump(all_usuarios)  # el metodo dump() lo hereda de ma.schema y
                                              # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla

@app.route('/usuarios/<id>',methods=['GET'])
def get_usuario(id):
    usuario=Usuario.query.get(id)
    return usuarios_schema_schema.jsonify(usuario)   # retorna el JSON de una excursión recibido como parametro

@app.route('/usuarios/<id>',methods=['DELETE'])
def delete_usuario(id):
    usuario=Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return usuarios_schema_schema.jsonify(usuario)   # me devuelve un json con el registro eliminado

@app.route('/usuarios', methods=['POST']) # crea ruta o endpoint
def create_usuario():
    #print(request.json)  # request.json contiene el json que envio el cliente
    usuario=request.json['usuario']
    nombre=request.json['nombre']
    apellido=request.json['apellido']
    clave=request.json['clave']
    email=request.json['email']
    tipo=request.json['tipo']
    fecha=request.json['fecha']
    new_usuario=Usuario(usuario,nombre,apellido,clave,email,tipo,fecha)
    db.session.add(new_usuario)
    db.session.commit()
    return usuarios_schema_schema.jsonify(new_usuario)

@app.route('/usuarios/<id>' ,methods=['PUT'])
def update_usuario(id):
    usuario=Usuario.query.get(id)
    usuario.usuario=request.json['usuario']
    usuario.nombre=request.json['nombre']
    usuario.apellido=request.json['apellido']
    usuario.clave=request.json['clave']
    usuario.email=request.json['email']
    usuario.tipo=request.json['tipo']
    usuario.fecha=request.json['fecha']
    db.session.commit()
    return usuarios_schema_schema.jsonify(usuario)
