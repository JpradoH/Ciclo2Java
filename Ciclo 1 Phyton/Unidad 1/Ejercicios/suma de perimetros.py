#calcular el perimetro y el area de un cuadrado donde uno de sus lados(L)es 38m
#no usar la 'm' para identificar metros ya que python lo toma de otra forma

L = 38 #define un lado del cuadrado
A = L * L #define el area del cuadrado
P = L + L + L + L #define el perimetro del cuadrado
#funcion str permite contatenar letras con numeros
print('El area del cuadraro:'+str(A))
#para concatenar infomracion tambien se puede usar la coma sin usar +str
print('El area del perimetreo:',P,'m2')
