from flask import Flask, render_template,session,redirect,request
from usuarios_app import app
from usuarios_app.modelos.modelo_usuarios import Usuario

@app.route('/usuarios',methods=['GET'])
def mostrarUsuarios():
    listaDeUsuarios = Usuario.obtenerListaUsarios()
    return render_template('leer.html',listaDeUsuarios=listaDeUsuarios)

@app.route('/',methods=['GET'])
def paginaInicio():
    if 'confirmar' not in session:
        return render_template('agregar.html')
    return render_template('agregar.html')

@app.route('/usuarios/nuevo',methods=['POST'])
def agregarUsuario():
    nuevoUsuario = {
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"]
    }
    if nuevoUsuario['nombre']=='':
        return redirect('/')
    session['confirmar']=1
    resultado = Usuario.agregarUsuario(nuevoUsuario)
    return redirect('/usuarios')

@app.route('/usuarios/<id>',methods=['GET'])
def mostrarUsuario(id):
    usuarioaMostrar={
        "id" : id
    }
    resultado = Usuario.mostrarUsuario(usuarioaMostrar)
    return render_template("mostrar.html",usuario=resultado[0])

@app.route('/usuarios/<id>/editar', methods=['GET'])
def mostrarEditarUsuario(id):
    
    usuarioAEditar = {
        "id" : id
    }
    resultado = Usuario.mostrarUsuario(usuarioAEditar)
    return render_template("editar.html",usuario=resultado[0])

@app.route('/usuarios/<id>/editar', methods=['POST'])
def editarUsuario(id):
    usuarioaEditar ={
        "id" : id,
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"]
    }
    resultado = Usuario.editarUsuario(usuarioaEditar)
    return redirect('/usuarios')

@app.route('/usuarios/<id>/eliminar', methods=['POST'])
def eliminarUsuario(id):
    usuarioaEliminar={
        "id" : id
    }
    resultado = Usuario.eliminarUsuario(usuarioaEliminar)
    return redirect('/usuarios')
