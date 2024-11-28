from getDataFormJson import teaList as teaListMethod 
Green, Black, White=teaListMethod()

print([tea['name'] for tea in teaListMethod()[0]])