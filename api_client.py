#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:26:12 2020

@author: necidcanedo
"""

import requests
import json
import numpy as np

server = 'localhost:5000'

def registrar_paciente(cliente):
    response = requests.post('http://' + server + '/pacientes', json = cliente)
    dic = json.loads(response.text) ## Leer Body de la respuesta como texto y interpretar como JSON
    return dic["id_paciente"]
    
def leer_paciente(cedula):
     response = requests.get('http://' + server + '/pacientes?cedula={}'.format(cedula))
     return json.loads(response.text)

def analizar_senal(id_paciente, senal):
    senal_bytes = senal.tobytes()
    response = requests.post('http://' + server + '/analisis/{}'.format(id_paciente), 
                             data=senal_bytes,
                             headers={'Content-Type': 'application/octet-stream'},
                             stream=True)
    buffer = response.raw.read()
    out = np.frombuffer(buffer, dtype=np.float)
    return out