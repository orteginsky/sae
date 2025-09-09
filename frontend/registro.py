from flask import Blueprint, render_template, request, redirect, url_for, flash

from db import SessionLocal
from models import CatUnidadAcademica, CatRol, CatAltaUsuario
from CRUD.usuarios import validar_usuario_existente

registro_bp = Blueprint('registro', __name__)

@registro_bp.route('/recuperar_usuario', methods=['GET', 'POST'])
def recuperar_usuario():
    if request.method == 'POST':
        email = request.form['email']
        # Aquí iría la lógica para buscar el usuario y enviar el correo
        flash('Si el correo está registrado, recibirás tu usuario próximamente.')
    return redirect(url_for('auth.login'))
    return render_template('recuperar_usuario.html')

@registro_bp.route('/recuperar_contrasena', methods=['GET', 'POST'])
def recuperar_contrasena():
    if request.method == 'POST':
        usuario_email = request.form['usuario_email']
        # Aquí iría la lógica para buscar la contraseña y enviar el correo
        flash('Si los datos coinciden, recibirás tu contraseña próximamente.')
    return redirect(url_for('auth.login'))
    return render_template('recuperar_contrasena.html')

@registro_bp.route('/alta_usuario', methods=['GET', 'POST'])
#@login_required  # Se comenta para permitir acceso sin usuario
def alta_usuario():
    session = SessionLocal()
    try:
        unidades = [
            {'nombre': u.Nombre, 'sigla': u.Sigla} for u in session.query(CatUnidadAcademica).all()
        ]
        roles = [r.Nombre for r in session.query(CatRol).all()]
    except Exception as e:
        flash(f'Error al cargar catálogos: {e}')
        unidades = []
        roles = []
    finally:
        session.close()
    if request.method == 'POST':
        unidad_input = request.form['unidad']
        rol_nombre = request.form['rol']
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        email = request.form['email']
        session = SessionLocal()
        try:
            # Validar formato de correo electrónico, Activar si es necesario.
            #if '@' not in email:
            #    flash('El correo electrónico no es válido. Debe contener un "@".')
            #    return render_template('alta_usuario.html', unidades=unidades, roles=roles)
            # Validar longitud mínima de contraseña
            if len(contrasena) < 8:
                flash('La contraseña debe tener al menos 8 caracteres.')
                return render_template('alta_usuario.html', unidades=unidades, roles=roles)
            # Buscar por sigla o nombre
            unidad = session.query(CatUnidadAcademica).filter(
                (CatUnidadAcademica.Nombre == unidad_input) | (CatUnidadAcademica.Sigla == unidad_input)
            ).first()
            if not unidad:
                flash('Unidad Académica no encontrada. Escribe el nombre completo o la sigla.')
                return render_template('alta_usuario.html', unidades=unidades, roles=roles)
            rol = session.query(CatRol).filter_by(Nombre=rol_nombre).first()
            if not rol:
                flash('Rol inválido.')
                return render_template('alta_usuario.html', unidades=unidades, roles=roles)
            # Validar usuario existente usando función centralizada
            if validar_usuario_existente(usuario):
                flash('El usuario ya está registrado. Intenta con otro nombre de usuario.')
                return render_template('alta_usuario.html', unidades=unidades, roles=roles)
            # Insertar usuario con ORM
            nuevo = CatAltaUsuario(
                Id_Unidad_Academica=unidad.Id_Unidad_Academica,
                Id_Rol=rol.Id_Rol,
                Usuario=usuario,
                Contraseña=contrasena,
                Email=email
            )
            session.add(nuevo)
            session.commit()
            flash('Usuario registrado exitosamente.')
            return redirect(url_for('registro.alta_usuario'))
        except Exception as e:
            flash(f'Error inesperado: {e}')
        finally:
            session.close()
    return render_template('alta_usuario.html', unidades=unidades, roles=roles)
