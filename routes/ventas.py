from flask import Blueprint, render_template, request, redirect
from database import db

ventas_bp = Blueprint('ventas', __name__, url_prefix='/ventas')

# Ver historial de ventas
@ventas_bp.route('/')
def ver_ventas():
    lista_ventas = list(db.ventas.find())
    return render_template('ventas.html', ventas=lista_ventas)

# Abrir el formulario para vender/cobrar
@ventas_bp.route('/nuevo')
def nueva_venta():
    return render_template('fromventas.html')

# Guardar la venta enviada desde fromventas.html
@ventas_bp.route('/guardar', methods=['POST'])
def guardar_venta():
    if request.method == 'POST':
        nueva_ven = {
            "producto": request.form.get('producto'),
            "cantidad": request.form.get('cantidad'),
            "total": request.form.get('total')
        }
        db.ventas.insert_one(nueva_ven)
        return redirect('/ventas/')