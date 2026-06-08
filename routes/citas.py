from flask import Blueprint, render_template, request, redirect
from database import db

citas_bp = Blueprint('citas', __name__, url_prefix='/citas')

# Ver lista de citas
@citas_bp.route('/')
def ver_citas():
    lista_citas = list(db.citas.find())
    return render_template('citas.html', citas=lista_citas)

# Abrir el formulario para agendar cita
@citas_bp.route('/nuevo')
def nueva_cita():
    return render_template('fromcitas.html')

# Guardar la cita enviada desde fromcitas.html
@citas_bp.route('/guardar', methods=['POST'])
def guardar_cita():
    if request.method == 'POST':
        nueva_ci = {
            "paciente": request.form.get('paciente'),
            "doctor": request.form.get('doctor'),
            "fecha": request.form.get('fecha'),
            "hora": request.form.get('hora')
        }
        db.citas.insert_one(nueva_ci)
        return redirect('/citas/')