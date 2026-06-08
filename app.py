from flask import Flask
from routes.index import index_bp
from routes.doctores import doctores_bp
from routes.pacientes import pacientes_bp
from routes.citas import citas_bp
from routes.ventas import ventas_bp
from routes.facturacion import facturacion_bp

app = Flask(__name__)

# Registrar los blueprints con la carpeta en minúsculas
app.register_blueprint(index_bp)
app.register_blueprint(doctores_bp)
app.register_blueprint(pacientes_bp)
app.register_blueprint(citas_bp)
app.register_blueprint(ventas_bp)
app.register_blueprint(facturacion_bp)

if __name__ == "__main__":
    app.run(debug=True)