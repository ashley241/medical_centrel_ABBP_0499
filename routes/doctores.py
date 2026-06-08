from flask import Blueprint, render_template, request, redirect
from database import db

doctores_bp = Blueprint('doctores', __name__, url_prefix='/doctores')

# RUTA 1: Ver la tabla con la lista de doctores (http://localhost:5000/doctores/)
@doctores_bp.route('/')
def ver_doctores():
    lista_doctores = list(db.doctores.find())
    return render_template('doctores.html', doctores=lista_doctores)

# RUTA 2: Abrir el formulario para escribir un nuevo doctor (http://localhost:5000/doctores/nuevo)
@doctores_bp.route('/nuevo')
def nuevo_doctor():
    return render_template('fromdoctores.html')

# RUTA 3: Recibir los datos del formulario y guardarlos en MongoDB
@doctores_bp.route('/guardar', methods=['POST'])
def guardar_doctor():
    if request.method == 'POST':
        nuevo_doc = {
            "nombre": request.form.get('nombre'),
            "especialidad": request.form.get('especialidad'),
            "telefono": request.form.get('telefono'),
            "correo": request.form.get('correo')
        }
        db.doctores.insert_one(nuevo_doc) # Lo guarda en MongoDB
        return redirect('/doctores/') # Te redirige a la tabla para ver el nuevo registro