import math


class FormasGeometricas:
  def __init__(self, nome):
    self.nome = nome
  
  def area(self):
    pass
  
  def perimetro(self):
    pass


class Quadrado(FormasGeometricas):
  def __init__(self, lado):
    super().__init__("Quadrado")
    self.lado = lado
  
  def area(self):
    return self.lado ** 2
  
  def perimetro(self):
    return 4 * self.lado
  
  def diagonal(self):
    return math.sqrt(2) * self.lado
  
  def to_string(self):
    return "{} de lado {}, área {}, perímetro {} e diagonal {}".format(
      self.nome, self.lado, self.area(), self.perimetro(), self.diagonal()
    )


class Retangulo(FormasGeometricas):
  def __init__(self, base, altura):
    super().__init__("Retângulo")
    self.base = base
    self.altura = altura
  
  def area(self):
    return self.base * self.altura
  
  def perimetro(self):
    return 2 * (self.base + self.altura)
  
  def diagonal(self):
    return math.sqrt((self.base ** 2) + (self.altura ** 2))
  
  def to_string(self):
    return "{} de base {}, altura {}, área {}, perímetro {} e diagonal {}".format(
      self.nome, self.base, self.altura, self.area(), self.perimetro(), self.diagonal()
    )


class Circulo(FormasGeometricas):
  def __init__(self, raio):
    super().__init__("Círculo")
    self.raio = raio
  
  def area(self):
    return math.pi * (self.raio ** 2)
  
  def perimetro(self):
    return 2 * math.pi * self.raio
  
  def diametro(self):
    return 2 * self.raio
  
  def to_string(self):
    return "{} de raio {}, área {}, perímetro {}, e diâmetro {}".format(
      self.nome, self.raio, self.area(), self.perimetro(), self.diametro()
    )


class Triangulo(FormasGeometricas):
  def __init__(self, lado1, lado2, lado3):
    super().__init__("Triângulo")
    self.lado1 = lado1
    self.lado2 = lado2
    self.lado3 = lado3
  
  def area(self):
    p = self.perimetro() / 2
    return math.sqrt(p * (p - self.lado1) * (p - self.lado2) * (p - self.lado3))
  
  def perimetro(self):
    return self.lado1 + self.lado2 + self.lado3
  
  def to_string(self):
    return "{} de lados {}, {}, {} área {} e perímetro {}".format(
      self.nome, self.lado1, self.lado2, self.lado3, self.area(), self.perimetro()
    )


class Trapezio(FormasGeometricas):
  def __init__(self, base_maior, base_menor, altura, lado1, lado2):
    super().__init__("Trapézio")
    self.base_maior = base_maior
    self.base_menor = base_menor
    self.altura = altura
    self.lado1 = lado1
    self.lado2 = lado2
    
  def area(self):
    return ((self.base_maior + self.base_menor) * self.altura) / 2
    
  def perimetro(self):
    return None