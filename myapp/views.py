from django.shortcuts import render
from django.http import HttpResponse
from pickle import load
import json
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from django.http import JsonResponse
from keras.models import load_model
import numpy as np
import urllib.request
import cv2
import tensorflow as tf
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Paciente, Sintomas
import openai


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
      except Paciente.DoesNotExist:
        return JsonResponse({"error": "Paciente not found"}, status=404)

      pajson = ({"nombre":pacientes.nombre, "apellidos":pacientes.apellidos,"cedula":pacientes.cedula})
      #openai.api_key = "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"
      #response = openai.Completion.create(model="text-davinci-003", prompt="dame informacion sobre la enfermedad de " +pacientes.enfermedad, temperature=0, max_tokens=250)
      
      
      return render(request, "pacientes.html", {"pacientes": pacientes,"sintomas":pacientesSintomas})
      return JsonResponse({'msg': "paciente encontradpo" , "data": pajson})
    #return JsonResponse({'msg': "paciente encontradpo" , "data": pajson})        
  return JsonResponse({'error': 'Bad request'}, status=400)



  #pacientes = Paciente.objects.get(cedula="17458965587")



def pac(request):

  pacientes = Paciente.objects.all()
  
  return render(request, "pacientes.html", {"pacientes": pacientes})

def chao(request):
  path_img ='https://laboratorio.lister.com.mx/wp-content/uploads/2020/05/enfermedad-Kawasaki.jpg'
  
  req=urllib.request.urlopen(path_img)
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

def predict(img):
  
  model = 'myapp\modelo.h5'
  weights = 'myapp\pesos.h5'
  cnn = load_model(model)
  cnn.load_weights(weights)
  arreglo = cnn.predict(img)
  resultado = arreglo [0]
  respuesta = np.argmax(resultado)
  if respuesta == 0:
    print ('leucoplasia')
    lesion = '00'
  elif respuesta == 1:
    print ('vesicula')
    lesion = '01'
  elif respuesta == 2:
    print ('papula')
    lesion = '02'
  elif respuesta == 3:
    print ('eritema')
    lesion = '03'
  elif respuesta == 4:
    print ('maculopapular')
    lesion = 'maculopapular'
  elif respuesta == 5:
    print ('ampollas')
    lesion = '05'
  return lesion

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
        #return JsonResponse({'msg': msg , "diagnostico": data})
        modelo_cargado = load(open('myapp\Modelopiel.sav', 'rb'))
        unidades_datos = np.array([[data['lesionid'],data['temperatura'],data['edad'],data['dolorcabeza'],data['conjuntivitis']
        ,data['malestargeneral'],data['ganglioshinchados'],data['tos'],data['moqueo'],data['dolorgarganta'],data['diarrea'],data['vomito'],data['nauseas'],data['infecoid']
        ,data['convulsion'],data['comezon'],data['perdidaapetito'],data['dolortragar'],data['hinchazon'],data['hinchazonboca'],data['dolorabdominal'],data['escalofrio'],data['perdidagusto']
        ,data['dolordentadura'],data['cara'],data['torso'],data['cabeza'],data['extremidadessuperiores'],data['extremidadesinferiores'],data['genitales'],data['manos'],data['boca'],data['pies']]])
              
        unidades = pd.DataFrame(unidades_datos, columns=["lesion_id","temperatura","edad","dolor_cabeza","conjuntivitis","malestar_general","ganglios_hinchados","tos","moqueo","dolor_garganta","diarrea"
        ,"vomito","nauseas","infec_oid","convulsion","comezon","perdida_apetito","dolor_tragar","hinchazon","hinchazon_boca","dolor_abdominal","escalofrio","perdida_gusto","dolor_dentadura"
        ,"cara","torso","cabeza","extremidades_superiores","extremidades_inferiores","genitales","manos","boca","pies"
        ])
        

        msg = "prediccion correcta"
        prediccion_nuevos = modelo_cargado.predict(unidades)   
        try:
          pac = Paciente.objects.get(cedula=data['cedula'])
          pacSintomas = Sintomas.objects.get(cedula=data['cedula'])
        except Paciente.DoesNotExist:
          print("error")
          pac = None
          pacSintomas = None
        
        if pac is None:
          pacNew = Paciente(
          nombre = data['nombre'],
          apellidos="",
          cedula=data['cedula'],
          enfermedad=prediccion_nuevos[0],
          tipo_lesion=data['lesionid'],#aui toca poner el id que retorna el modelo de imagenes
          edad=data['edad']
          )
          pacNew.save()
        else:
          pac.enfermedad=prediccion_nuevos[0]
          pac.tipo_lesion=data['lesionid']#aui toca poner el id que retorna el modelo de imagenes
          pac.save()  
        
        if pacSintomas is None:
          pacS = Sintomas(
          cedula = data['cedula'],
          lesion_id = data['lesionid'],
          temperatura = data['temperatura'],
          edad = data['edad'],
          dolor_cabeza = convert(data['dolorcabeza']),
          conjuntivitis = convert(data['conjuntivitis']),
          malestar_general = convert(data['malestargeneral']),
          ganglios_hinchados = convert(data['ganglioshinchados']),
          tos = convert(data['tos']),
          moqueo = convert(data['moqueo']),
          dolor_garganta = convert(data['dolorgarganta']),
          diarrea = convert(data['diarrea']),
          vomito = convert(data['vomito']),
          nauseas = convert(data['nauseas']),
          infec_oid = convert(data['infecoid']),
          convulsion = convert(data['convulsion']),
          comezon = convert(data['comezon']),
          perdida_apetito = convert(data['perdidaapetito']),
          dolor_tragar = convert(data['dolortragar']),
          hinchazon = convert(data['hinchazon']),
          hinchazon_boca = convert(data['hinchazonboca']),
          dolor_abdominal = convert(data['dolorabdominal']),
          escalofrio = convert(data['escalofrio']),
          perdida_gusto = convert(data['perdidagusto']),
          dolor_dentadura = convert(data['dolordentadura']),
          cara = convert(data['cara']),
          torso = convert(data['torso']),
          cabeza = convert(data['cabeza']),
          extremidades_superiores = convert(data['extremidadessuperiores']),
          extremidades_inferiores = convert(data['extremidadesinferiores']),
          genitales = convert(data['genitales']),
          manos = convert(data['manos']),
          boca = convert(data['boca']),
          pies = convert(data['pies'])
          )
          pacS.save()
        else:
          pacSintomas.cedula = data['cedula']
          pacSintomas.lesion_id = data['lesionid']
          pacSintomas.temperatura = data['temperatura']
          pacSintomas.edad = data['edad']
          pacSintomas.dolor_cabeza = convert(data['dolorcabeza'])
          pacSintomas.conjuntivitis = convert(data['conjuntivitis'])
          pacSintomas.malestar_general = convert(data['malestargeneral'])
          pacSintomas.ganglios_hinchados = convert(data['ganglioshinchados'])
          pacSintomas.tos = convert(data['tos'])
          pacSintomas.moqueo = convert(data['moqueo'])
          pacSintomas.dolor_garganta = convert(data['dolorgarganta'])
          pacSintomas.diarrea = convert(data['diarrea'])
          pacSintomas.vomito = convert(data['vomito'])
          pacSintomas.nauseas = convert(data['nauseas'])
          pacSintomas.infec_oid = convert(data['infecoid'])
          pacSintomas.convulsion = convert(data['convulsion'])
          pacSintomas.comezon = convert(data['comezon'])
          pacSintomas.perdida_apetito = convert(data['perdidaapetito'])
          pacSintomas.dolor_tragar = convert(data['dolortragar'])
          pacSintomas.hinchazon = convert(data['hinchazon'])
          pacSintomas.hinchazon_boca = convert(data['hinchazonboca'])
          pacSintomas.dolor_abdominal = convert(data['dolorabdominal'])
          pacSintomas.escalofrio = convert(data['escalofrio'])
          pacSintomas.perdida_gusto = convert(data['perdidagusto'])
          pacSintomas.dolor_dentadura = convert(data['dolordentadura'])
          pacSintomas.cara = convert(data['cara'])
          pacSintomas.torso = convert(data['torso'])
          pacSintomas.cabeza = convert(data['cabeza'])
          pacSintomas.extremidades_superiores = convert(data['extremidadessuperiores'])
          pacSintomas.extremidades_inferiores = convert(data['extremidadesinferiores'])
          pacSintomas.genitales = convert(data['genitales'])
          pacSintomas.manos = convert(data['manos'])
          pacSintomas.boca = convert(data['boca'])
          pacSintomas.pies = convert(data['pies'])
          pacSintomas.save()
         

        responseData = {
        'diagnostico' : [prediccion_nuevos[0]]
        } 
    return JsonResponse({'msg': msg , "diagnostico": responseData, 'cedula': data['cedula']})
  return JsonResponse({'error': 'Bad request'}, status=400)