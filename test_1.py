from programa import imprimir_nombre
from io import StringIO
import sys

def test_imprimir_nombre(capsys):
    imprimir_nombre()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Diego Saavedra"
