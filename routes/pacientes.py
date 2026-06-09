from flask import Blueprint, render_template, request, redirect, url_for
from database import db
from bson.objectid import ObjectId

pacientes_bp = Blueprint('pacientes', __name__)

PACIENTES_REALES = [
    {"nombre": "Sofía Castro", "edad": "36", "sangre": "A+", "sintomas": "Fiebre y tos"},
    {"nombre": "Patricia Vega", "edad": "34", "sangre": "O-", "sintomas": "Picazón en la piel"},
    {"nombre": "Claudia Rivas", "edad": "48", "sangre": "B+", "sintomas": "Dolor de espalda"},
    {"nombre": "Isabel Luján", "edad": "35", "sangre": "A+", "sintomas": "Dolor de garganta"},
    {"nombre": "Hugo Martínez", "edad": "47", "sangre": "O-", "sintomas": "Revisión general"}
]

# LEER
@pacientes_bp.route('/pacientes/')
def ver_pacientes():
    # Eliminamos cualquier intento previo vacío para evitar conflictos de bases de datos
    if db.pacientes.count_documents({}) == 0:
        db.pacientes.insert_many(PACIENTES_REALES)
        
    lista_pacientes = list(db.pacientes.find())
    return render_template('pacientes.html', pacientes=lista_pacientes)

# AGREGAR
@pacientes_bp.route('/pacientes/agregar', methods=['POST'])
def agregar_paciente():
    if request.method == 'POST':
        nuevo = {
            "nombre": request.form['nombre'],
            "edad": request.form['edad'],
            "sangre": request.form['sangre'],
            "sintomas": request.form['sintomas']
        }
        db.pacientes.insert_one(nuevo)
    return redirect(url_for('pacientes.ver_pacientes'))

# EDITAR
@pacientes_bp.route('/pacientes/editar/<id>', methods=['POST'])
def editar_paciente(id):
    if request.method == 'POST':
        actualizado = {
            "nombre": request.form['nombre'],
            "edad": request.form['edad'],
            "sangre": request.form['sangre'],
            "sintomas": request.form['sintomas']
        }
        db.pacientes.update_one({"_id": ObjectId(id)}, {"$set": actualizado})
    return redirect(url_for('pacientes.ver_pacientes'))

# ELIMINAR
@pacientes_bp.route('/pacientes/eliminar/<id>')
def eliminar_paciente(id):
    db.pacientes.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('pacientes.ver_pacientes'))