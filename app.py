import os
from flask import Flask, jsonify, request, render_template
# jsonify devuelve en formato JSON la informacion
# request dice por q metodo estoy haciendo la peticion
# render_template : crea una salida en html del archivo q yo le diga
from flask_script import Manager # generar los comando para q corra la app
from flask_migrate import Migrate, MigrateCommand # libreria para q genera los comandos para hacer las migraciones (script de las tablas) y crearlas en el gestor de BBDD
from flask_cors import CORS #protege la app y evita el error de cors al ejecutar un fetch
from models import db, Contact #comunar la app con el gestor de migraciones 

app = Flask(__name__) # atributo obligatorio
app.url_map.strict_slashes = False # permite cargar los metodos con o sin slash
app.config['DEBUG'] = True # para ver los errores de la app
app.config['ENV'] = 'development' # entorno de la app o se puede usar 'production' cuando ya se publique
# para desarrollo usando sqlite
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, "db.sqlite3") # para decir q tipo de BBDD va a ser (sqlite)
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # muestra los tracking de la BBDD

# para produccion usando MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Javiera123$@localhost/testapi' #'mysql+pymysql://user:password@servidor/basededatos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db.init_app(app)

Migrate(app, db)
CORS(app) #para proteger la app

manager = Manager(app)
manager.add_command ('db', MigrateCommand) # init (carpeta de migraciones la primera vez), migrate (crea las migraciones), upgrade (envia las migraciones a la BBDD)

@app.route('/') #por defecto es method: ['GET']
def root():
    return render_template('index.html')

@app.route('/api/test', methods=['GET', 'POST']) # GET obtiene los elementos q yo defina. POST para crear nuevos elementos
@app.route('/api/test/<int:id>', methods=['GET', 'PUT', 'DELETE']) # parametros q tengo q decir q elementos quiero obtener, actualizar o eliminar
def test(id = None):
    if request.method == 'GET':
        return jsonify({'msg': 'method GET'}), 200 # dara un mensaje de ok (200) al momento q se haga la peticion
    if request.method == 'POST':
        return jsonify({'msg': 'method POST'}), 200
    if request.method == 'PUT':
        return jsonify({'msg': 'method PUT'}), 200
    if request.method == 'DELETE':
        return jsonify({'msg': 'method DELETE'}), 200

@app.route('/api/test/<int:id>/category/<int:cat_id>', methods=['GET', 'POST'])
def test2(id, cat_id):
    if request.method == 'GET':
        return jsonify({'valores': {'id': id, 'cat_id': cat_id}}), 200
    if request.method == 'POST':
        return jsonify({'valores': {'id': id, 'cat_id': cat_id}}), 200

@app.route("/api/contacts", methods=["GET", "POST"])
@app.route("/api/contacts/<int:id>", methods=["GET", "PUT", "DELETE"]) # parametros q tengo q decir q elementos quiero obtener, actualizar o eliminar
def contacts(id = None):
    if request.method == "GET": #valida si viene o no con parametro
        if id is not None: 
            contact = Contact.query.get(id) # saco el contacto segun el id
            if contact:
                return jsonify(contacts.serialize()), 200
            else:
                return jsonify({"msg": "Not Found"}), 404

        else:
            contacts = Contact.query.all() # da los registros de la tabla contacts de la BD
            contacts = list(map(lambda contact: contact.serialize(), contacts))
            return jsonify(contacts), 200

    if request.method == "POST":
        pass
    if request.method == "PUT":
        pass
    if request.method == "DELETE":
        pass

if __name__ == '__main__':
    manager.run()
