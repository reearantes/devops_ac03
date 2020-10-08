def media_movel(d1,d2,d3,d4,d5,d6,d7):
	return (d1+d2+d3+d4+d5+d6+d7)/7
def test_valor():
	assert media_movel(1400,1400,2800,1414,714,1421,721) == 1410, "media movel da semana" 
def test_zero():
	assert media_movel(0,0,0,0,0,0,0) == 0, "media movel zero"
