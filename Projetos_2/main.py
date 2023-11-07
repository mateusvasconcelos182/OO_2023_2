from some_module import formas_geometricas
from unidecode import unidecode

tipo = input('informe uma forma geometrica bidimensional: ')
tipo = unidecode(tipo).lower()

if tipo == 'quadrado':
  lados = input('Informe o sua largura: ')
  
  forma = formas_geometricas.Quadrado(float(lados))
  print(f'sua área é: {forma.area()}')
  print(f'seu perimetro é: {forma.perimetro()}')
elif tipo == 'triangulo':
  lado1 = input('Informe seu lado 1:')
  lado2 = input('Informe seu lado 2:')
  lado3 = input('Informe seu lado 3:')

  forma = formas_geometricas.Triangulo(float(lado1), float(lado2), float(lado3))

  print(f'sua área é: {forma.area()}')
  print(f'seu perimetro é: {forma.perimetro()}')
elif tipo == 'circulo':
  raio = input('Informe seu raio: ')
  forma = formas_geometricas.Circulo(float(raio))
  
  print(f'sua área é: {forma.area()}')
  print(f'seu perimetro é: {forma.perimetro()}')
elif tipo == 'retangulo':
  base = input('Qual a sua base: ')
  altura = input('Qual a sua altura: ')
  
  forma = formas_geometricas.Retangulo(float(base), float(altura))
  
  print(f'sua área é: {forma.area()}')
  print(f'seu perimetro é: {forma.perimetro()}')
elif tipo == 'trapezio':
  base_maior = input('informe a base maior: ')
  base_menor = input('informe a base menor: ')
  altura = input('informe a altura: ')
  lado1 = input('informe o lado 1: ')
  lado2 = input('informe o lado 2: ')
  
  forma = formas_geometricas.Trapezio(float(base_maior), float(base_menor), float(altura), float(lado1), float(lado2))
  
  print(f'sua área é: {forma.area()}')
