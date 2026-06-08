from flask import Blueprint, render_template, request, redirect
from database import db

facturacion_bp = Blueprint('facturacion', __name__, url_prefix='/facturacion')

# Ver lista de facturas
@facturacion_bp.route('/')
def ver_facturacion():
    lista_facturas = list(db.facturas.find())
    return render_template('facturacion.html', facturas=lista_facturas)

# Abrir el formulario de nueva factura
@facturacion_bp.route('/nuevo')
def nueva_factura():
    return render_template('fromfacturacion.html')

# Guardar la factura enviada desde fromfacturacion.html
@facturacion_bp.route('/guardar', methods=['POST'])
def guardar_factura():
    if request.method == 'POST':
        nueva_fac = {
            "rfc": request.form.get('rfc'),
            "cliente": request.form.get('cliente'),
            "monto": request.form.get('monto'),
            "concepto": request.form.get('concepto')
        }
        db.facturas.insert_one(nueva_fac)
        return redirect('/facturacion/')