from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


#Definir el formulario de registro de productos

class NuevoProducto(FlaskForm):
    name = StringField("Nombre del producto")
    precio = StringField("Precio del producto")
    submit = SubmitField("Registrar Producto")
    
    
    
    