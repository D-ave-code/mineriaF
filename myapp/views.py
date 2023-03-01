from django.shortcuts import render
from django.http import HttpResponse
from pickle import load
import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from django.http import JsonResponse
from keras.models import load_model
import numpy as np
import urllib.request
import cv2
import tensorflow as tf
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Paciente, Sintomas, Lesion
import openai
import base64
import io
from PIL import Image, ImageTk
from tkinter import Tk, Label
import str



def home(request):

  return render(request, "formulario.html")

# Create your views here.
@method_decorator(csrf_exempt)
def busquedaPaciente(request):
  if request.method == 'POST':
    #if request.content_type == 'application/json':
      #data = request.POST.get('title')
      try:
        pacientes = Paciente.objects.get(cedula=request.POST.get('cedula'))
        pacientesSintomas = Sintomas.objects.get(cedula=request.POST.get('cedula'))
        lesiones = Lesion.objects.get(cedula=request.POST.get('cedula'))
        
      except Paciente.DoesNotExist:
        return JsonResponse({"error": "Paciente not found"}, status=404)

      pajson = ({"nombre":pacientes.nombre, "apellidos":pacientes.apellidos,"cedula":pacientes.cedula})
      #openai.api_key = "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"
      #response = openai.Completion.create(model="text-davinci-003", prompt="dame informacion sobre la enfermedad de " +pacientes.enfermedad, temperature=0, max_tokens=250)
      
      
      return render(request, "pacientes.html", {"pacientes": pacientes,"sintomas":pacientesSintomas,"lesiones":lesiones})
      return JsonResponse({'msg': "paciente encontradpo" , "data": pajson})
    #return JsonResponse({'msg': "paciente encontradpo" , "data": pajson})        
  return JsonResponse({'error': 'Bad request'}, status=400)



  #pacientes = Paciente.objects.get(cedula="17458965587")



def pac(request):

  pacientes = Paciente.objects.all()
  
  return render(request, "pacientes.html", {"pacientes": pacientes})

def chao(request):
  path_img ='https://laboratorio.lister.com.mx/wp-content/uploads/2020/05/enfermedad-Kawasaki.jpg'
  
  req = urllib.request.urlopen(path_img)
  arr = np.asarray(bytearray(req.read()),dtype=np.uint8)
  img = cv2.imdecode(arr, -1)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  img = cv2.resize(img, (320,320))
  img_tensor = np.array([img])
  d = str(predict(img_tensor))
  responseData = {
        'id': 4,
        'name': "cris",
        'diagnostico' : d
    }
  return JsonResponse(responseData)
  # probar
  unidades_datos = np.array([[4,38.1,6,0,0,0,0,0,0,0
      ,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0]])

  unidades = pd.DataFrame(unidades_datos, columns=["lesion_id","temperatura","edad","dolor_cabeza","conjuntivitis","malestar_General","ganglios_hinchados","tos","moqueo","dolor_garganta","diarrea","vomito","nauseas","infec_oid","convulsion","comezon","perdida_apetito","dolor_tragar","hinchazon","hinchazon_boca","dolor_abdominal","escalofrio","perdida_gusto","dolor_dentadura","cara","torso","cabeza","extremidades_superiores","extremidades_inferiores","genitales","manos","boca","pies"
 ])
  
  # fin
  pacientes_nuevos = pd.read_csv('myapp\Test.csv', engine='python', delimiter=';')
  modelo_cargado = load(open('myapp\Modelopiel.sav', 'rb'))

  prediccion_nuevos = modelo_cargado.predict(unidades_datos)
  responseData = {
        'id': 4,
        'name': "cris",
        'diagnostico' : [d,prediccion_nuevos[0]]
    }

  return JsonResponse(responseData)
  return HttpResponse(predict(img_tensor))
cnn = load_model('myapp\modelo.h5')
cnn.load_weights('myapp\pesos.h5')
def predict(img,cedu):
  
  arreglo = cnn.predict(img)
  resultado = arreglo [0]
  respuesta = np.argmax(resultado)
  arr_sorted = np.sort(resultado)[::-1]
  arregloPrediccion = np.array([0, 0, 0])
  i=0
  while i<3:
    for j in range(0,6):
      if arr_sorted[i] == resultado[j]:
        arregloPrediccion[i] = j+1    
    i += 1
  temp = list()
  try:
    les = Lesion.objects.get(cedula= cedu)
  except: 
    les = None
  for i in range(0,3):  
    
    if arregloPrediccion[i]==1:
        temp.append('Costras') 
    if arregloPrediccion[i]==2:
         temp.append('Papula')

    if arregloPrediccion[i]==3:
         temp.append('Vesicula')

    if arregloPrediccion[i]==4:
         temp.append('Leucoplacia')

    if arregloPrediccion[i]==5:
         temp.append('Dermatofitosis')

    if arregloPrediccion[i]==6:
         temp.append('Maculopapular')

  if les is None:
    lnew = Lesion(
    cedula = cedu,
    tipo1= temp[0],
    tipo2= temp[1],
    tipo3= temp[2]
     )
    lnew.save()
  else:
    les.tipo1= temp[0]
    les.tipo2= temp[1]
    les.tipo3= temp[2]
    les.save()

  if respuesta == 0:
    print ('Costras')
    lesion = '1'
  elif respuesta == 1:
    print ('Papula')
    lesion = '2'
  elif respuesta == 2:
    print ('Vesicula')
    lesion = '3'
  elif respuesta == 3:
    print ('Leucoplacia')
    lesion = '4'
  elif respuesta == 4:
    print ('Dermatofitosis')
    lesion = '5'
  elif respuesta == 5:
    print ('Maculopapular')
    lesion = '6'
  return (arregloPrediccion)

def convert(text):
  t=""
  if text==1:
    t = "SI"
  else:
    t = "NO"
  return t

@method_decorator(csrf_exempt)
def formulario(request):
  if request.method == 'POST':
    if request.content_type == 'application/json':
  
        msg = ""
        data = json.loads(request.body)
        # Decodifica la cadena de base64 a sus bytes originales
        decoded_bytes = base64.b64decode(data['image'])

        # Crea un objeto BytesIO a partir de los bytes decodificados
        image_file = io.BytesIO(decoded_bytes)

        # Crea una imagen PIL a partir del objetpytho BytesIO
        img2 =Image.open(image_file)
        #img1 = img2.rotate(270)
        img1 = img2
        img1.save("static/"+data['cedula']+".jpg")

        img = img1.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        d = (predict(img_array,data['cedula']))
        #return JsonResponse({'msg': "valio" , "diagnostico": "data"})
        modelo_cargado = load(open('myapp\ModeloPielFinalBosques.sav', 'rb'))
        unidades_datos = np.array([[d[0],data['temperatura'],data['edad'],data['dolorCabeza'],data['conjuntivitis']
        ,data['malestarGeneral'],data['gangliosHinchados'],data['tos'],data['moqueo'],data['dolorGarganta'],data['diarrea'],data['vomito'],data['nauseas']
        ,data['comezon'],data['perdidaApetito'],data['dolorTragar'],data['hinchazon'],data['hinchazonBoca'],data['dolorAbdominal'],data['escalofrio'],data['perdidaGusto']
        ,data['dolorDentadura'],data['cara'],data['torso'],data['cabeza'],data['extremidadesSuperiores'],data['extremidadesInferiores'],data['genitales'],data['manos'],data['boca'],data['pies']]])
        #conserved = unidades_datos[0,:3]
        #mixed = np.random.permutation(unidades_datos[0,3:])
        #mixed1 = np.random.permutation(unidades_datos[0,3:])
        #print(mixed)
        #print(mixed1)
         
        unidades = pd.DataFrame(unidades_datos, columns=["lesion_id","temperatura","edad","dolor_cabeza","conjuntivitis","malestar_general","ganglios_hinchados","tos","moqueo","dolor_garganta","diarrea"
        ,"vomito","nauseas","comezon","perdida_apetito","dolor_tragar","hinchazon","hinchazon_boca","dolor_abdominal","escalofrio","perdida_gusto","dolor_dentadura"
        ,"cara","torso","cabeza","extremidades_superiores","extremidades_inferiores","genitales","manos","boca","pies"
        ])
       
        msg = "prediccion correcta"
        prediccion_nuevos = modelo_cargado.predict(unidades)   
        #prediccion_nuevos1 = modelo_cargado.predict(np.array([np.concatenate((conserved, mixed))]))   
        #prediccion_nuevos2 = modelo_cargado.predict(np.array([np.concatenate((conserved, mixed1))]))   
         
        #print(prediccion_nuevos)
        #print(prediccion_nuevos1)
        #print(prediccion_nuevos2)
        
        try:
          pac = Paciente.objects.get(cedula=data['cedula'])
          pacSintomas = Sintomas.objects.get(cedula=data['cedula'])
        except Paciente.DoesNotExist:
          print("creando datos")
          pac = None
          pacSintomas = None
        
        if pac is None:
          pacNew = Paciente(
          nombre = data['nombre'],
          apellidos=data['apellido'],
          cedula=data['cedula'],
          enfermedad=prediccion_nuevos[0],
          tipo_lesion=d,#aui toca poner el id que retorna el modelo de imagenes
          edad=data['edad']
          )
          pacNew.save()
        else:
          pac.nombre = data['nombre']
          pac.apellidos=data['apellido']
          pac.enfermedad=prediccion_nuevos[0]
          pac.tipo_lesion=d#aui toca poner el id que retorna el modelo de imagenes
          pac.edad=data['edad']
          pac.save()  
        
        if pacSintomas is None:
          pacS = Sintomas(
          cedula = data['cedula'],
          lesion_id = d,
          temperatura = data['temperatura'],
          edad = data['edad'],
          dolor_cabeza = convert(data['dolorCabeza']),
          conjuntivitis = convert(data['conjuntivitis']),
          malestar_general = convert(data['malestarGeneral']),
          ganglios_hinchados = convert(data['gangliosHinchados']),
          tos = convert(data['tos']),
          moqueo = convert(data['moqueo']),
          dolor_garganta = convert(data['dolorGarganta']),
          diarrea = convert(data['diarrea']),
          vomito = convert(data['vomito']),
          nauseas = convert(data['nauseas']),
          comezon = convert(data['comezon']),
          perdida_apetito = convert(data['perdidaApetito']),
          dolor_tragar = convert(data['dolorTragar']),
          hinchazon = convert(data['hinchazon']),
          hinchazon_boca = convert(data['hinchazonBoca']),
          dolor_abdominal = convert(data['dolorAbdominal']),
          escalofrio = convert(data['escalofrio']),
          perdida_gusto = convert(data['perdidaGusto']),
          dolor_dentadura = convert(data['dolorDentadura']),
          cara = convert(data['cara']),
          torso = convert(data['torso']),
          cabeza = convert(data['cabeza']),
          extremidades_superiores = convert(data['extremidadesSuperiores']),
          extremidades_inferiores = convert(data['extremidadesInferiores']),
          genitales = convert(data['genitales']),
          manos = convert(data['manos']),
          boca = convert(data['boca']),
          pies = convert(data['pies'])
          )
          pacS.save()
        else:
          pacSintomas.cedula = data['cedula']
          pacSintomas.lesion_id = d
          pacSintomas.temperatura = data['temperatura']
          pacSintomas.edad = data['edad']
          pacSintomas.dolor_cabeza = convert(data['dolorCabeza'])
          pacSintomas.conjuntivitis = convert(data['conjuntivitis'])
          pacSintomas.malestar_general = convert(data['malestarGeneral'])
          pacSintomas.ganglios_hinchados = convert(data['gangliosHinchados'])
          pacSintomas.tos = convert(data['tos'])
          pacSintomas.moqueo = convert(data['moqueo'])
          pacSintomas.dolor_garganta = convert(data['dolorGarganta'])
          pacSintomas.diarrea = convert(data['diarrea'])
          pacSintomas.vomito = convert(data['vomito'])
          pacSintomas.nauseas = convert(data['nauseas'])
          pacSintomas.comezon = convert(data['comezon'])
          pacSintomas.perdida_apetito = convert(data['perdidaApetito'])
          pacSintomas.dolor_tragar = convert(data['dolorTragar'])
          pacSintomas.hinchazon = convert(data['hinchazon'])
          pacSintomas.hinchazon_boca = convert(data['hinchazonBoca'])
          pacSintomas.dolor_abdominal = convert(data['dolorAbdominal'])
          pacSintomas.escalofrio = convert(data['escalofrio'])
          pacSintomas.perdida_gusto = convert(data['perdidaGusto'])
          pacSintomas.dolor_dentadura = convert(data['dolorDentadura'])
          pacSintomas.cara = convert(data['cara'])
          pacSintomas.torso = convert(data['torso'])
          pacSintomas.cabeza = convert(data['cabeza'])
          pacSintomas.extremidades_superiores = convert(data['extremidadesSuperiores'])
          pacSintomas.extremidades_inferiores = convert(data['extremidadesInferiores'])
          pacSintomas.genitales = convert(data['genitales'])
          pacSintomas.manos = convert(data['manos'])
          pacSintomas.boca = convert(data['boca'])
          pacSintomas.pies = convert(data['pies'])
          pacSintomas.save()
    #return JsonResponse({'msg': msg })
    return JsonResponse({'msg': "valio" , "diagnostico": data})
  return JsonResponse({'error': 'Bad request'}, status=400)