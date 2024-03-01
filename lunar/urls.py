from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from django.urls import path

moon_data = [
    [0.78, 0.7, 0.61, 0.52, 0.42, 0.32, 0.23, 0.15, 0.08, 0.03, 0.01, 0.01, 0.03, 0.09, 0.17, 0.26, 0.37, 0.48, 0.59, 0.7, 0.79, 0.87, 0.93, 0.97, 0.99, 1.0, 0.98, 0.95, 0.91, 0.84, 0.77],
    [0.69, 0.6, 0.5, 0.4, 0.3, 0.21, 0.12, 0.06, 0.02, 0.0, 0.02, 0.06, 0.13, 0.22, 0.33, 0.43, 0.54, 0.64, 0.74, 0.82, 0.89, 0.94, 0.98, 1.0, 1.0, 0.98, 0.95, 0.9, 0.83],
    [0.75, 0.66, 0.57, 0.46, 0.36, 0.26, 0.16, 0.09, 0.03, 0.0, 0.01, 0.04, 0.1, 0.18, 0.28, 0.38, 0.48, 0.59, 0.68, 0.77, 0.84, 0.91, 0.95, 0.98, 1.0, 1.0, 0.97, 0.93, 0.88, 0.81, 0.72],
    [0.62, 0.52, 0.41, 0.3, 0.2, 0.11, 0.05, 0.01, 0.0, 0.02, 0.07, 0.14, 0.23, 0.32, 0.42, 0.52, 0.62, 0.71, 0.79, 0.86, 0.92, 0.96, 0.99, 1.0, 0.99, 0.96, 0.91, 0.84, 0.76, 0.66],
    [0.55, 0.44, 0.33, 0.23, 0.13, 0.06, 0.02, 0.0, 0.01, 0.05, 0.1, 0.18, 0.26, 0.36, 0.45, 0.55, 0.64, 0.73, 0.81, 0.88, 0.93, 0.97, 1.0, 1.0, 0.98, 0.93, 0.87, 0.79, 0.69, 0.58, 0.47],
    [0.36, 0.25, 0.16, 0.08, 0.03, 0.0, 0.0, 0.03, 0.07, 0.13, 0.21, 0.3, 0.39, 0.48, 0.57, 0.67, 0.75, 0.83, 0.9, 0.95, 0.99, 1.0, 0.99, 0.95, 0.89, 0.81, 0.71, 0.61, 0.49, 0.38],
    [0.27, 0.18, 0.1, 0.05, 0.01, 0.0, 0.01, 0.05, 0.1, 0.16, 0.24, 0.32, 0.41, 0.51, 0.6, 0.69, 0.78, 0.86, 0.93, 0.97, 1.0, 0.99, 0.97, 0.91, 0.83, 0.74, 0.63, 0.51, 0.4, 0.3, 0.2],
    [0.12, 0.06, 0.02, 0.0, 0.0, 0.02, 0.06, 0.11, 0.18, 0.26, 0.35, 0.44, 0.54, 0.64, 0.73, 0.82, 0.9, 0.95, 0.99, 1.0, 0.98, 0.93, 0.85, 0.76, 0.66, 0.54, 0.43, 0.33, 0.24, 0.16, 0.09],
    [0.04, 0.01, 0.0, 0.01, 0.03, 0.08, 0.13, 0.2, 0.29, 0.38, 0.48, 0.58, 0.68, 0.78, 0.86, 0.93, 0.98, 1.0, 0.99, 0.95, 0.88, 0.79, 0.69, 0.59, 0.48, 0.38, 0.28, 0.2, 0.13, 0.07],
    [0.03, 0.01, 0.0, 0.01, 0.04, 0.09, 0.15, 0.23, 0.32, 0.42, 0.52, 0.63, 0.74, 0.83, 0.91, 0.97, 1.0, 1.0, 0.96, 0.91, 0.83, 0.74, 0.64, 0.54, 0.43, 0.34, 0.25, 0.17, 0.11, 0.06, 0.02],
    [0.0, 0.0, 0.02, 0.06, 0.11, 0.18, 0.27, 0.37, 0.47, 0.58, 0.69, 0.79, 0.88, 0.95, 0.99, 1.0, 0.98, 0.94, 0.87, 0.79, 0.7, 0.6, 0.51, 0.41, 0.32, 0.24, 0.16, 0.1, 0.05, 0.02],
    [0.0, 0.01, 0.03, 0.08, 0.14, 0.23, 0.32, 0.43, 0.54, 0.65, 0.76, 0.85, 0.92, 0.97, 1.0, 0.99, 0.96, 0.92, 0.85, 0.77, 0.68, 0.59, 0.49, 0.4, 0.31, 0.23, 0.15, 0.09, 0.04, 0.01, 0.0]
]

def WaxingOrWanning(month,day): # day,month should start from 0
    if moon_data[month][day] in [0.0,1.0]:
        return 'neither'
    
    if day<len(moon_data[month])-1:
        for i in range(5):
            if moon_data[month][day+i]<moon_data[month][day+i+1]:
                return 'waxing'
            if moon_data[month][day+i]>moon_data[month][day+i+1]:
                return 'wanning'
            if day>0 and moon_data[month][day+i-1]<moon_data[month][day+i]:
                return 'waxing'
            if day>0 and moon_data[month][day+i-1]>moon_data[month][day+i]:
                return 'wanning'

    if day==len(moon_data[month])-1:
        for i in range(5):
            if moon_data[month][day-i-1]<moon_data[month][day-i]:
                return 'waxing'
            if moon_data[month][day-i-1]>moon_data[month][day-i]:
                return 'wanning'
            



@api_view(['GET'])
def getData(request,pk1,pk2):
    return Response({'illumination':moon_data[pk1][pk2],'phase':WaxingOrWanning(pk1,pk2)})

urlpatterns = [
    path('<int:pk1>/<int:pk2>/', getData, name='illumination-wax-wan'),
]

