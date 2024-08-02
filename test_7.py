from programa import area_circulo
import math

def test_area_circulo():
    assert round(area_circulo(1), 2) == round(math.pi, 2)
    assert round(area_circulo(2), 2) == round(4 * math.pi, 2)
