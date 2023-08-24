from . import productos
#el . es para que nos importe todo el modulo

from . import productos
from flask import render_template
from .forms import NuevoProducto

@productos.route('/crear')
def crear_producto():
    form=NuevoProducto()
    return render_template('new.html', form = form)
