from flask import Blueprint, render_template, request, redirect
from database import db

pacientes_bp = Blueprint('pacientes', __name__, url_prefix='/pacientes')

# Ver lista de pacientes
@pacientes_bp.route('/')
def ver_pacientes():
    lista_pacientes = list(db.pacientes.find())
    return render_template('pacientes.html', pacientes=lista_pacientes)

# Abrir el formulario para registrar uno nuevo
@pacientes_bp.route('/nuevo')
def nuevo_paciente():
    return render_template('frompacientes.html')

# Guardar los datos enviados desde frompacientes.html
@pacientes_bp.route('/guardar', methods=['POST'])
def guardar_paciente():
    if request.method == 'POST':
        nuevo_pac = {
            "nombre": request.form.get('nombre'),
            "edad": request.form.get('edad'),
            "telefono": request.form.get('telefono'),
            "sintomas": request.form.get('sintomas')
        }
        db.pacientes.insert_one(nuevo_pac)
        return redirect('/pacientes/')