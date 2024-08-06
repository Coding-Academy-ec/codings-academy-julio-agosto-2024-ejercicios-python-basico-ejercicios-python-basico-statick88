from programa import imprimir_datos_personales
from io import StringIO
import sys

def test_imprimir_datos_personales(capsys):
    nombre = "Jonathan Visconti"
    edad = 31
    estatura = 1.65
    imprimir_datos_personales(nombre, edad, estatura)
    captured = capsys.readouterr()
    assert captured.out == "Nombre: Jonathan Visconti\nEdad: 31\nEstatura: 1.65\n"