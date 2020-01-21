#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:26:12 2020

@author: necidcanedo
"""

import requests
import json

server = 'localhost:5000'

def registrar_paciente(cliente):
    response = requests.post('http://' + server + '/pacientes', json = cliente)
    dic = json.loads(response.text)
    return dic["id_paciente"]
    
