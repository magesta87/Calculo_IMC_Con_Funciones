#Funcion IMC (indice de masa corporal)

def inDatosP(respuesta):
 
  if respuesta == 's' or respuesta == 'si':

      peso = float(input('Igrese su peso: '))
      
      
  return peso


def inDatosA(respuesta):
  if respuesta == 's' or respuesta == 'si':

    altura = float(input('Ingrese su altura: '))

  return altura    

def IMC(peso, altura):
  imc = peso / altura ** 2
  return float(imc)  

def Comprobacion(imc):
  
  if imc < 18.5:
    return "Por debajo del peso"
  elif imc > 18.5 or imc <= 24.9:
    return "Saludable" 
  elif imc >= 25.0 or imc <= 29.9:
    return "Con sobrepeso"
  elif imc >= 30.0 or imc <= 39.9:
    return "Obeso"
  elif imc > 40:
    return "Obesidad extrema o de alto riesgo"



    

respuesta = input('Desea conocer su IMC (si o no): ')
if respuesta == 's' or respuesta == 'si':
  
  print(Comprobacion(IMC(inDatosP(respuesta), inDatosA(respuesta))))
else:
  print("Hasta luego.")  





