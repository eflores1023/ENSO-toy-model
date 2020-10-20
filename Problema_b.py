# -*- coding: utf-8 -*-
"""
@author: Camila Fernanda Guzmán Lara, camila.guzman.l@ug.uchile.cl
         Esteban Andrés Flores Gutiérrez, esteban.flores@ug.uchile.cl

                   *     *  * P R O B L E M A   B *  *     *


"""

#######################################################
"""###########Funcionamiento del programa"""###########
#######################################################
"""####################################################
Tanto el metodo de Euler como el Metodo de Heun (con retardo) son funciones 
dentro del programa que reciben cuatro parametros:
    
    x0: El primer valor del intervalo en el que queremos resolver nuestra 
    ecuacion diferencial, en nuestro caso es x0=0(meses)
    
    xf: Cota superior del intervalo de interes. En nuestro caso queremos 
    obtener para 20 años, como la unidad corresponde a mes -> xf=20*12(meses)
    
    step: El valor del paso entre x_n y x_n+1. Lo definimos como 
    x_(n+1)-x_n=step, en nuestro caso definiremos el step dentro de una lista:
    deltat=[1,0.1, 0.01, 0.005]. Resolveremos la ecuacion del Modelo 1 con 
    ambos metodos con todos estos valores 'step'.
    
    seed: Todo problema de valor inicial requiere de condiciones iniciales. 
    En este problema, al resolver para Te, y al ser una EDO de primer orden, 
    requiere una condicion, que en este caso es Te(0)=1.
    
 
Se implementan estas nuevas funciones porque esta vez se resolvera el 
Modelo 1, pero el valor del retardo es distinto de cero, esta vez delta es 
igual a cinco.
    
A diferencia del programa del Problema_a, esta vez no debemos entregar el 
parametro 'func' a evaluar, dado que esta la definiremos dentro del mismo 
programa. Se ha desarrollado asi netamente por comodidad y no existe una 
razon profunda.

Por lo tanto, todas las constantes se definiran dentro de cada funcion. 
Incluso el retardo que existe en el Modelo 1 que identificamos como la 
variable tipo float 'delta'.

En resumen, los metodos de Euler y de Heun estan resueltos para nuestra 
funcion especifica del Modelo 1 y no para una funcion cualquiera. 
Esto es irrelevante porque en la tarea solo debemos resolver dicha ecuacion.

*****A      C O  N   S    I     D      E       R          A      R*****

En la funcion 'def solution(x)' se usa el modulo numpy para evaluar todos los 
valores de un arange sin necesidad de usar un for. Numpy no se usa para 
calcular los metodos numericos y no es esencial en el proceso.
Sin embargo se debe tener en cuenta para que quien corra este programa tenga 
instalada la libreria y evitar algun tipo de error.

Ademas se incluyen modulos importados desde matplotlib para graficar.
"""###################################################


import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import numpy as np

def Euler_retard(x0, xf, step, seed):
        #Se definen las constantes
        R1=0.1
        Cew1=0.27
        gamma1=1
        alf1=0.612
        
        deltt=5. #Retardo dentro del argumento de la EDO.
        
        paso=step       #Almacenamos las variables entregadas  en la funcion
        
        retardo=int(deltt/paso)  
        #La variable 'retardo' es importante. Con esto sabemos 
        #Cuantos indices se deben devolver para obtener los valores 
    #De Te de hace cinco meses. Es decir retardo=5meses en unidades de indice
        #Esto se define asi porque se entregan distintos pasos 
        #Implicando que cinco meses corresponden a una distinta cantidad de
        #indices, dependiendo de la cantidad de pasos
        
        initiale=x0
        finale=xf
        semi=seed
        list_x=[] #Creamos las listas donde almacenar los valores en cada eje
        list_y=[]
        list_x.append(initiale) #Agregamos los valores iniciales.
        list_y.append(semi)
        c=0  #Contador para ir recorriendo las listas
        while(initiale<finale):
            
            if(c*paso<=deltt): #Para los primeros cinco meses el Te(t-delta)=1
                k=R1*list_y[c]-Cew1*gamma1*alf1 #Valor de la funcion a evaluar.
                vari=list_y[c]+k*paso              #Metodo de Euler
                list_y.append(vari)    #Agregamos el valor de y a la lista
                initiale=initiale+paso      #Avanzamos en el tiempo 
                list_x.append(initiale)     #Agregamos el valor de x
                c=c+1 #Agregamos al contador y volvemos a iterar
                
            elif(c*paso>deltt): 
        #En este caso Te(t-delta)!=0, corresponde al valor de hace cinco meses
        #Que ya ha sido almacenado en la lista.
                
                k=R1*list_y[c]-Cew1*gamma1*alf1*list_y[c-retardo]    
                #Valor de la funcion a evaluar, 
                #esta vez con retardo.
                
                vari=list_y[c]+k*paso
                list_y.append(vari)
                initiale=initiale+paso
                list_x.append(initiale)
                c=c+1 #Agregamos al contador y volvemos a iterar
                
            
        list_Values=[list_x,list_y]
        return list_Values

def Heun_retard(x0, xf, step, seed):
    
        #Definimos las constantes.
        R1=0.1
        Cew1=0.27
        gamma1=1
        alf1=0.612
        deltt=5.
        
        #Almacenamos las variables entregadas como argumentos
        paso=step  
        retardo=int(deltt/paso) #Analoga a 'retardo' de Euler_retard.
        initiale=x0
        finale=xf
        semi=seed
        list_x=[] #Se crean las listas para almacenar los valores en cada eje.
        list_y=[]
        list_x.append(initiale)  #Almacenamos las condiciones iniciales.
        list_y.append(semi)
        c=0  #Contador que iterara sobre las listas
        while(initiale<finale):
            
            if(c*paso<=deltt):
                k0=R1*list_y[c]-Cew1*gamma1*alf1  #Definimos nuestra lista
                k1=list_y[c]+k0*paso #Hasta aca es el metodo de Euler
                #Paso intermedio para el metodo de Heun.
                k2=R1*k1-Cew1*gamma1*alf1
                
                
                vari=list_y[c]+0.5*paso*(k0+k2) #Metodo de Heun de dos pasos.
                list_y.append(vari) #Almacenamos las variables.
                initiale=initiale+paso #Cambiamos al siguiente tiempo.
                list_x.append(initiale)  #Agregamos el tiempo a la lista
                c=c+1 #Sumamos al contador y volvemos a iterar.
            elif(c*paso>deltt):
                #Evaluamos en la funcion
                k0=R1*list_y[c]-Cew1*gamma1*alf1*list_y[c-retardo] 
                
                k1=list_y[c]+k0*paso #Paso intermedio. Es un metodo de Euler.
                #Evaluamos en la funcion para k1
                k2=R1*k1-Cew1*gamma1*alf1*list_y[c-retardo]  
                vari=list_y[c]+0.5*paso*(k0+k2) #Metodo de Heun
                list_y.append(vari)        #Metodo de Heun de dos pasos.
                initiale=initiale+paso    #Cambiamos al siguiente tiempo.
                list_x.append(initiale)   
                #Sumamos al contador y volvemos a iterar.
                c=c+1
                
        list_Values=[list_x,list_y]
        return list_Values


#####################VARIABLES USADAS EN AMBOS METODOS

va=20.*12.#Este valor representa los 20 años. Sera nuestra xf en ambos metodos.
deltat=[1,0.1, 0.01, 0.005] #En la tarea se pide evaluar para distintos paso.
                            #Estos se almacenan en la lista deltat. 

#Initial value. Valor inicial que corresponde a Te(0)=1. Es nuestro seed.
iv=1. 


#####################

"""METODO DE     E U L E R"""

aprox=[]   #Aqui almacenaremos los valores para 'x' e 'y' para distintos step.

for j in range(len(deltat)):
    eu=Euler_retard(0.0, va ,deltat[j],iv) 
    aprox.append(eu)
    
"""I M  P   O    R     T      A       N        T         E

En cada posicion de aprox se almacena una lista con dos listas, de forma que:
    aprox=[[lista_x0,lista_y0],[lista_x1,lista_y1],..., [lista_x3,lista_y3]]]
    Es importante entender que tienen cada una para graficar.

"""


fig, ax = plt.subplots()#Creamos la figura

#Aqui graficamos los resultados obtenidos para distintos steps.
for m in range(len(aprox)):   
                              #A cada uno le entregamos un label.
    if(m==0):    
        ax.plot(aprox[m][0],aprox[m][1], label="$\Delta t=1$")
    elif(m==1):
        ax.plot(aprox[m][0],aprox[m][1], label="$\Delta t=0.1$")
    elif(m==2):
        ax.plot(aprox[m][0],aprox[m][1], label="$\Delta t=0.01$") 
    elif(m==3):
        ax.plot(aprox[m][0],aprox[m][1], label="$\Delta t=0.005$")    

    
    
plt.legend(handler_map={ax: HandlerLine2D(numpoints=4)})   #Creamos el label.

ax.set_xlabel('t')               #Establecemos titulo a los ejes.
ax.set_ylabel('Te')
fig.suptitle('Metodo de Euler con retardo', fontsize=12)  #Titulo de la figura
#Se guarda la figura en la carpeta en el PATH correspondiente.
fig.savefig('Euler_method_retard.png')   
plt.show()

""""""""""""""""""""""""""""""""""""""""""""""""


"""METODO DE        H E U N

Repetimos el mismo proceso del metodo de Euler, ahora para el metodo de Heun.
Entregamos distintos valores para el step, los que se encuentran en deltat. 
Almacenados cada resultado en aprox1=[]. 
Analogamente: 
aprox1=[[lista_x0,lista_y0],[lista_x1,lista_y1],..., [lista_x3,lista_y3]]].
"""
 




fig1, ax1= plt.subplots()
aprox1=[]
for j in range(len(deltat)):
    eu=Heun_retard(0.0, va ,deltat[j],iv) 
    aprox1.append(eu)


####Repetimos el proceso para graficar del metodo anterior.

for m in range(len(aprox)):
    if(m==0):    
        ax1.plot(aprox1[m][0],aprox1[m][1], label="$\Delta t=1$")
    elif(m==1):
        ax1.plot(aprox1[m][0],aprox1[m][1], label="$\Delta t=0.1$")
    elif(m==2):
        ax1.plot(aprox1[m][0],aprox1[m][1], label="$\Delta t=0.01$") 
    elif(m==3):
        ax1.plot(aprox1[m][0],aprox1[m][1], label="$\Delta t=0.005$") 
        
        

plt.legend(handler_map={ax1: HandlerLine2D(numpoints=4)})

ax1.set_xlabel('t')
ax1.set_ylabel('Te')
fig1.suptitle('Metodo de Heun con retardo', fontsize=12)
fig1.savefig('Heun_method_retard.png')
plt.show()


#############################################
#Comparamos ambos metodos para deltat=0.005

fig2, ax2= plt.subplots()

ax2.plot(aprox[3][0],aprox[3][1], label="Euler")
ax2.plot(aprox1[3][0],aprox1[3][1], label="Heun") 
plt.legend(handler_map={ax2: HandlerLine2D(numpoints=4)})

ax2.set_xlabel('t')
ax2.set_ylabel('Te')
fig2.suptitle('Euler vs Heun. Step=0.005, con retardo.', fontsize=12)
fig2.savefig('Versus_RETARD_st05.png')
plt.show()

############################################

#Comparamos ambos metodos para deltat=1

fig3, ax3= plt.subplots()

ax3.plot(aprox[0][0],aprox[0][1], label="Euler")
ax3.plot(aprox1[0][0],aprox1[0][1],'k' ,label="Heun") 
plt.legend(handler_map={ax2: HandlerLine2D(numpoints=4)})

ax3.set_xlabel('t')
ax3.set_ylabel('Te')
fig3.suptitle('Euler vs Heun. Step=1, con retardo.', fontsize=12)
fig3.savefig('Versus_RETARD_st1.png')
plt.show()







