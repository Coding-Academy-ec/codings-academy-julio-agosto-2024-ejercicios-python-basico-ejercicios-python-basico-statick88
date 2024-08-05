import math
from programa import area_circulo

def test_area_circulo():
    # Test case 1: radius = 0
    assert area_circulo(0) == 0

    # Test case 2: radius = 1
    assert area_circulo(1) == math.pi

    # Test case 3: radius = 2.5
    assert area_circulo(2.5) == math.pi * 2.5 ** 2

    # Test case 4: radius = -3
    assert area_circulo(-3) == math.pi * (-3) ** 2

    # Test case 5: radius = 10
    assert area_circulo(10) == math.pi * 10 ** 2

test_area_circulo()