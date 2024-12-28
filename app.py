from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api
from db_config import db
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import UserModel

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
api = Api(app)


# Página principal
@app.route('/')
def home():
    return render_template('index.html')


# Página de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        # Crear un nuevo usuario
        new_user = UserModel(email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('home'))  # Redirigir a la página principal después del registro

    return render_template('register.html')


# Página de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']  # Captura el email del formulario
        password = request.form['password']  # Captura la contraseña del formulario

        # Consulta usando 'Email' con mayúscula
        user = UserModel.query.filter_by(Email=email).first()

        if user:
            # Verifica si el hash de la contraseña coincide
            if check_password_hash(user.PasswordHash, password):
                return f"Bienvenido, {email}."
            else:
                return "Contraseña incorrecta.", 401
        else:
            return "Usuario no encontrado.", 404

    return render_template('login.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crear las tablas si no existen
    app.run(debug=True)
