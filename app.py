from flask import Flask, render_template
from routes.doctores import doctores_bp
from routes.pacientes import pacientes_bp
from routes.citas import citas_bp
from routes.facturacion import facturacion_bp
from routes.medicamento import medicamentos_bp

app = Flask(__name__)

app.register_blueprint(doctores_bp)
app.register_blueprint(pacientes_bp)
app.register_blueprint(citas_bp)
app.register_blueprint(facturacion_bp)
app.register_blueprint(medicamentos_bp)

@app.route('/')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)