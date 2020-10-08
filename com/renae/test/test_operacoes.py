def mul(x,y):
	return x*y

def test_valor():
	assert mul(5,5) == 25

def test_negativo():
	assert mul(2,-2) == -4

def test_zero():
	assert mul(0,0) == 0