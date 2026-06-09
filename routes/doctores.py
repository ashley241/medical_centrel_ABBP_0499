from flask import Blueprint, render_template, request, redirect, url_for
from database import db
from bson.objectid import ObjectId

doctores_bp = Blueprint('doctores', __name__)

DOCTORES_REALES = [
    {"nombre": "Sofía Castro", "especialidad": "Psiquiatra", "edad": "36", "horario": "4:00 PM - 9:00 PM", "dias": "Miércoles y Viernes", "telefono": "614-666-3322"},
    {"nombre": "Ricardo Luna", "especialidad": "Endocrinólogo", "edad": "42", "horario": "12:00 PM - 5:00 PM", "dias": "Martes y Miércoles", "telefono": "614-111-9988"},
    {"nombre": "Patricia Vega", "especialidad": "Odontóloga", "edad": "34", "horario": "8:00 AM - 4:00 PM", "dias": "Lunes a Sábado", "telefono": "614-777-5544"},
    {"nombre": "Fernando Torres", "especialidad": "Neurólogo", "edad": "44", "horario": "9:00 AM - 2:00 PM", "dias": "Lunes a Jueves", "telefono": "614-234-8899"},
    {"nombre": "Claudia Rivas", "especialidad": "Oncóloga", "edad": "48", "horario": "8:00 AM - 12:00 PM", "dias": "Lunes, Miércoles y Viernes", "telefono": "614-567-3344"},
    {"nombre": "Sergio Perea", "especialidad": "Urólogo", "edad": "39", "horario": "4:00 PM - 8:00 PM", "dias": "Martes y Jueves", "telefono": "614-111-2233"},
    {"nombre": "Isabel Luján", "especialidad": "Reumatóloga", "edad": "35", "horario": "11:00 AM - 4:00 PM", "dias": "Lunes a Viernes", "telefono": "614-999-8877"},
    {"nombre": "Manuel Quiroz", "especialidad": "Anestesiólogo", "edad": "52", "horario": "6:00 AM - 12:00 PM", "dias": "Lunes a Sábado", "telefono": "614-444-5566"},
    {"nombre": "Hugo Martínez", "especialidad": "Pediatra", "edad": "47", "horario": "7:00 AM - 11:00 AM", "dias": "Lunes a Viernes", "telefono": "614-123-4567"}
]

# 1. LEER REGISTROS
@doctores_bp.route('/doctores/')
def ver_doctores():
    if db.doctores.count_documents({}) == 0:
        db.doctores.insert_many(DOCTORES_REALES)
    lista_doctores = list(db.doctores.find())
    return render_template('doctores.html', doctores=lista_doctores)

# 2. AGREGAR REGISTROS
@doctores_bp.route('/doctores/agregar', methods=['POST'])
def agregar_doctor():
    if request.method == 'POST':
        nuevo_doc = {
            "nombre": request.form['nombre'],
            "especialidad": request.form['especialidad'],
            "edad": request.form['edad'],
            "horario": request.form['horario'],
            "dias": request.form['dias'],
            "telefono": request.form['telefono']
        }
        db.doctores.insert_one(nuevo_doc)
    return redirect(url_for('doctores.ver_doctores'))

# 3. ACTUALIZAR / EDITAR REGISTROS
@doctores_bp.route('/doctores/editar/<id>', methods=['POST'])
def editar_doctor(id):
    if request.method == 'POST':
        datos_actualizados = {
            "nombre": request.form['nombre'],
            "especialidad": request.form['especialidad'],
            "edad": request.form['edad'],
            "horario": request.form['horario'],
            "dias": request.form['dias'],
            "telefono": request.form['telefono']
        }
        db.doctores.update_one({"_id": ObjectId(id)}, {"$set": datos_actualizados})
    return redirect(url_for('doctores.ver_doctores'))

# 4. ELIMINAR REGISTROS
@doctores_bp.route('/doctores/eliminar/<id>')
def eliminar_doctor(id):
    db.doctores.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('doctores.ver_doctores'))