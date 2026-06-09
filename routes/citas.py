from flask import Blueprint, render_template, request, redirect, url_for
from database import db
from bson.objectid import ObjectId

citas_bp = Blueprint('citas', __name__)

CITAS_REALES = [
    {"id_cita": "001", "fecha": "2026-03-10", "signos": "TA: 120/80, FC: 75, Temp: 36.5", "diagnostico": "Migraña", "tratamiento": "Paracetamol 500mg cada 8 horas"},
    {"id_cita": "002", "fecha": "2026-03-15", "signos": "TA: 110/70, FC: 80, Temp: 38.2", "diagnostico": "Gripe", "tratamiento": "Jarabe para la tos y agua"},
    {"id_cita": "004", "fecha": "2026-03-22", "signos": "TA: 115/75, FC: 68, Temp: 36.4", "diagnostico": "Dermatitis", "tratamiento": "Crema hidratante y Loratadina"},
    {"id_cita": "005", "fecha": "2026-03-25", "signos": "TA: 130/90, FC: 88, Temp: 37.0", "diagnostico": "Fatiga visual", "tratamiento": "Gotas lubricantes y lentes"},
    {"id_cita": "006", "fecha": "2026-03-28", "signos": "TA: 120/80, FC: 70, Temp: 36.6", "diagnostico": "Lumbalgia", "tratamiento": "Naproxeno 500mg"},
    {"id_cita": "007", "fecha": "2026-04-01", "signos": "TA: 110/70, FC: 74, Temp: 36.2", "diagnostico": "Anemia leve", "tratamiento": "Suplemento de hierro"},
    {"id_cita": "008", "fecha": "2026-04-03", "signos": "TA: 122/82, FC: 76, Temp: 37.5", "diagnostico": "Faringitis", "tratamiento": "Amoxicilina 500mg"},
    {"id_cita": "009", "fecha": "2026-04-05", "signos": "TA: 118/78, FC: 72, Temp: 36.6", "diagnostico": "Infección Viral", "tratamiento": "Antiviral cada 12 horas"},
    {"id_cita": "010", "fecha": "2026-04-10", "signos": "TA: 120/80, FC: 80, Temp: 36.8", "diagnostico": "Chequeo General", "tratamiento": "Vitaminas y descanso"}
]

# LEER
@citas_bp.route('/citas/')
def ver_citas():
    # Si no hay ninguna consulta guardada, mete las 9 reales automáticamente
    if db.citas.count_documents({}) == 0:
        db.citas.insert_many(CITAS_REALES)
    lista_citas = list(db.citas.find())
    return render_template('citas.html', citas=lista_citas)

# AGREGAR
@citas_bp.route('/citas/agregar', methods=['POST'])
def agregar_cita():
    if request.method == 'POST':
        nueva = {
            "id_cita": request.form['id_cita'],
            "fecha": request.form['fecha'],
            "signos": request.form['signos'],
            "diagnostico": request.form['diagnostico'],
            "tratamiento": request.form['tratamiento']
        }
        db.citas.insert_one(nueva)
    return redirect(url_for('citas.ver_citas'))

# EDITAR
@citas_bp.route('/citas/editar/<id>', methods=['POST'])
def editar_cita(id):
    if request.method == 'POST':
        actualizado = {
            "id_cita": request.form['id_cita'],
            "fecha": request.form['fecha'],
            "signos": request.form['signos'],
            "diagnostico": request.form['diagnostico'],
            "tratamiento": request.form['tratamiento']
        }
        db.citas.update_one({"_id": ObjectId(id)}, {"$set": actualizado})
    return redirect(url_for('citas.ver_citas'))

# ELIMINAR
@citas_bp.route('/citas/eliminar/<id>')
def eliminar_cita(id):
    db.citas.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('citas.ver_citas'))