from flask import Blueprint, render_template, request, redirect
from bson.objectid import ObjectId
from database import db

medicamentos_bp = Blueprint('medicamentos', __name__)

# Lista de medicamentos
@medicamentos_bp.route('/medicamentos/')
def medicamentos():
    todos_meds = list(db.medicamentos.find())
    return render_template('medicamento.html', medicamentos=todos_meds)

# Formulario
@medicamentos_bp.route('/medicamentos/formulario')
def formulario_medicamentos():
    return render_template('frommedicamento.html')

# Agregar medicamento
@medicamentos_bp.route('/medicamentos/agregar', methods=['POST'])
def agregar_medicamento():
    datos = {
        "nombre": request.form.get('nombre'),
        "componente": request.form.get('componente'),
        "precio": float(request.form.get('precio')),
        "stock": int(request.form.get('stock'))
    }

    db.medicamentos.insert_one(datos)
    return redirect('/medicamentos/')

# Editar medicamento
@medicamentos_bp.route('/medicamentos/editar/<id>', methods=['POST'])
def editar_medicamento(id):
    filtro = {"_id": ObjectId(id)}

    nuevos_valores = {
        "$set": {
            "nombre": request.form.get('nombre'),
            "componente": request.form.get('componente'),
            "precio": float(request.form.get('precio')),
            "stock": int(request.form.get('stock'))
        }
    }

    db.medicamentos.update_one(filtro, nuevos_valores)
    return redirect('/medicamentos/')

# Eliminar medicamento
@medicamentos_bp.route('/medicamentos/eliminar/<id>')
def eliminar_medicamento(id):
    db.medicamentos.delete_one({"_id": ObjectId(id)})
    return redirect('/medicamentos/')