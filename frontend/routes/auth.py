# routes/auth.py
# Rutas de autenticación, panel principal, edición y eliminación de usuario

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from auth_user import User
from CRUD.usuarios import actualizar_usuario, eliminar_usuario
from CRUD.roles import obtener_roles
from db import SessionLocal
from models import CatAltaUsuario, CatUnidadAcademica, CatRol

bp = Blueprint('auth', __name__)

@bp.route('/')
@login_required
def index():
    session = SessionLocal()
    try:
        usuario = session.query(CatAltaUsuario).filter_by(Usuario=current_user.username).first()
        if not usuario:
            flash('No se pudo identificar al usuario.')
            return redirect(url_for('auth.logout'))
        unidad = session.query(CatUnidadAcademica).filter_by(Id_Unidad_Academica=usuario.Id_Unidad_Academica).first()
        rol = session.query(CatRol).filter_by(Id_Rol=usuario.Id_Rol).first()
        if rol.Nombre == 'Administrador':
            usuarios = session.query(CatAltaUsuario).filter_by(Id_Unidad_Academica=unidad.Id_Unidad_Academica).all()
            return render_template('panel_admin.html', unidad={'nombre': unidad.Nombre, 'sigla': unidad.Sigla}, usuarios=usuarios)
        elif rol.Nombre == 'Operador':
            return render_template('panel_operador.html', unidad={'nombre': unidad.Nombre, 'sigla': unidad.Sigla})
        else:
            flash('Rol no autorizado.')
            return redirect(url_for('auth.logout'))
    finally:
        session.close()

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form['username']
        password = request.form['password']
        from app import get_db_connection
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT Id_Usuario, Usuario, Contraseña, Id_Estatus FROM [Base_pruebas].[dbo].[Cat_Alta_Usuario] WHERE Usuario = ? OR Email = ?", (username_or_email, username_or_email))
            user_data = cursor.fetchone()
        except Exception as e:
            flash('Ocurrió un error al consultar la base de datos. Intenta nuevamente.')
            return render_template('login.html')
        finally:
            if conn:
                conn.close()
        if user_data:
            if user_data[3] == 3:
                flash('El usuario fue eliminado. Debe registrarse nuevamente.')
                return render_template('login.html')
            if user_data[2] == password:
                user = User(user_data[0], user_data[1])
                login_user(user)
                return redirect(url_for('auth.index'))
            else:
                flash('Contraseña Incorrecta. Intenta nuevamente.')
                return render_template('login.html')
        else:
            flash('Usuario o Correo no encontrado. Reintenta Nuevamente o Regístrate.')
            return render_template('login.html')
    return render_template('login.html')

@bp.route('/editar_usuario/<int:id_usuario>', methods=['GET', 'POST'])
@login_required
def editar_usuario(id_usuario):
    session = SessionLocal()
    try:
        usuario = session.query(CatAltaUsuario).filter_by(Id_Usuario=id_usuario).first()
        if not usuario:
            flash('Usuario no encontrado.')
            return redirect(url_for('auth.index'))
        if request.method == 'POST':
            usuario_nombre = request.form['usuario']
            email = request.form['email']
            id_rol = int(request.form['rol'])
            id_estatus = int(request.form['estatus'])
            actualizado = actualizar_usuario(id_usuario, Usuario=usuario_nombre, Email=email, Id_Rol=id_rol, Id_Estatus=id_estatus)
            if actualizado:
                flash('Usuario actualizado correctamente.')
            return redirect(url_for('auth.index'))
        roles = obtener_roles()
        return render_template('editar_usuario.html', usuario=usuario, roles=roles)
    finally:
        session.close()

@bp.route('/eliminar_usuario/<int:id_usuario>', methods=['POST'])
@login_required
def eliminar_usuario_route(id_usuario):
    if eliminar_usuario(id_usuario):
        flash('Usuario eliminado correctamente.')
    else:
        flash('No se pudo eliminar el usuario.')
    return redirect(url_for('auth.index'))

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión Cerrada.')
    return redirect(url_for('auth.login'))
