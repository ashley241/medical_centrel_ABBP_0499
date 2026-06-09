from flask import Blueprint, render_template, request, redirect, url_for
from database import db
from bson.objectid import ObjectId

facturacion_bp = Blueprint('facturacion', __name__)

# Lista actualizada con los 6 registros totales (tus 4 anteriores + los 2 nuevos)
FACTURAS_REALES = [
    {"folio": "F-001", "concepto": "Consulta General Urgencias", "monto": "350.00"},
    {"folio": "F-002", "concepto": "Certificado Médico Escolar", "monto": "150.00"},
    {"folio": "F-003", "concepto": "Tratamiento Dental Básico", "monto": "500.00"},
    {"folio": "F-004", "concepto": "Radiografía de Tórax", "monto": "650.00"},
    {"folio": "F-005", "concepto": "Consulta General Urgencias", "monto": "350.00"},
    {"folio": "F-006", "concepto": "Tratamiento Dental Básico", "monto": "500.00"}
]

# LEER
@facturacion_bp.route('/facturacion/')
def ver_facturacion():
    if db.facturas.count_documents({}) == 0:
        db.facturas.insert_many(FACTURAS_REALES)
    lista_facturas = list(db.facturas.find())
    return render_template('facturacion.html', facturas=lista_facturas)

# AGREGAR
@facturacion_bp.route('/facturacion/agregar', methods=['POST'])
def agregar_factura():
    if request.method == 'POST':
        nueva = {
            "folio": request.form['folio'],
            "concepto": request.form['concepto'],
            "monto": request.form['monto']
        }
        db.facturas.insert_one(nueva)
    return redirect(url_for('facturacion.ver_facturacion'))

# EDITAR
@facturacion_bp.route('/facturacion/editar/<id>', methods=['POST'])
def editar_factura(id):
    if request.method == 'POST':
        actualizado = {
            "folio": request.form['folio'],
            "concepto": request.form['concepto'],
            "monto": request.form['monto']
        }
        db.facturas.update_one({"_id": ObjectId(id)}, {"$set": actualizado})
    return redirect(url_for('facturacion.ver_facturacion'))

# ELIMINAR
@facturacion_bp.route('/facturacion/eliminar/<id>')
def eliminar_factura(id):
    db.facturas.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('facturacion.ver_facturacion'))