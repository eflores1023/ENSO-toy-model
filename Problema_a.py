# -*- coding: utf-8 -*-
"""
@author: Camila Fernanda Guzmán Lara, camila.guzman.l@ug.uchile.cl
         Esteban Andrés Flores Gutiérrez, esteban.flores@ug.uchile.cl


                   *     *  * P R O B L E M A   A *  *     *


"""
#######################################################
"""###########Funcionamiento del programa"""###########
#######################################################
"""####################################################
Tanto el metodo de Euler como el Metodo de Heun son funciones dentro del
programa que reciben cinco parametros:
    
    x0: El primer valor del intervalo en el que queremos resolver nuestra 
    ecuacion diferencial, en nuestro caso es x0=0[meses]
    
    xf: Cota superior del intervalo de interes. En nuestro caso queremos 
    obtener para 20 años, como la unidad corresponde a mes -> xf=20*12[meses].
    
    step: El valor del paso entre x_n y x_n+1. Lo definimos como
    x_(n+1)-x_n=step, en nuestro caso definiremos el step dentro de una lista: 
    deltat=[1,0.1, 0.01, 0.005]. Resolveremos la ecuacion del Modelo 1 con 
    ambos metodos con todos estos valores.
    
    seed: Todo problema de valor inicial requiere de condiciones iniciales. 
    En este problema, al resolver para Te, y al ser una EDO de priemr orden, 
    requiere una condicion, que en este caso es Te(0)=1.
    
    func: Como ambos metodos estan desarrollados para una EDO de la forma 
    y'(t,x)=f(Te,t), debemos especificar nuestra funcion a resolver que 
    corresponde a la mostrada en el Modelo 1 del enunciado de la tarea.
    
    

***** A      C O  N   S    I     D      E       R          A      R*****

En la funcion 'def solution(x)' se usa el modulo numpy para evaluar todos los
valores de un arange sin necesidad de usar un for. Numpy no se usa para 
calcular los metodos numericos y no es esencial en el proceso.
Sin embargo se debe tener en cuenta para que quien corra este programa 
tenga instalada la libreria y evitar algun tipo de error.

Ademas se incluyen modulos importados desde matplotlib para graficar.
"""##########################################################################

import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import numpy as np

def Euler(x0, xf, step, seed,func): #Las variables que recibe el programa 
                                    #explicadas en la parte superior.
        paso=step                  #Almacenamos las variables entregadas por 
                                    #comodidad.
        initiale=x0
        finale=xf
        semi=seed
        funce=func
        list_x=[]                   #Creamos las listas donde guardaremos
        list_y=[]                   #los valores para cada paso para Te.
        list_x.append(initiale)     #Almacenamos los valores iniciales.
        list_y.append(semi)
        c=0            #Cpntador para moverse entre las listas.
        while(initiale<finale):
            k=funce(list_y[c])      #Evaluamos nuestra funcion(Modelo 1)
            vari=list_y[c]+k*paso   #Este es el metodo de Euler.
            list_y.append(vari)     #Almacenamos la variable en y
            initiale=initiale+paso  #Pasamos al siguiente tiempo
            list_x.append(initiale) #Almacenamos nuestro tiempo
            c=c+1                   #Siguiente step, se repite el ciclo.
 
        list_values=[list_x,list_y]  #Luego de haber realizado todas las 
                                     #iteraciones, guardamos los valores de
                                     #x e y y los devolvemos en una lista que
                                     #contiene los valores obtenidos.
        return list_values

def Heun(x0, xf, step, seed,func): #El siguiente metodo es similar al Metodo 
                                   #de Euler.
         #Sin embargo, este metodo contiene un paso intermedio antes 
         #continuar con la siguiente iteracion. Esto nos permite 
         #obtener mayor precision al momento de resolver nuestra EDO.
    
        paso=step
        initiale=x0
        finale=xf
        semi=seed
        funce=func
        list_x=[] 
        list_y=[]
        list_x.append(initiale)
        list_y.append(semi)
        c=0
        while(initiale<finale):
            k0=funce(list_y[c])
            k1=list_y[c]+k0*paso #Hasta aca teniamos metodo de Euler
            k2=funce(k1)         #Sin embargo, k1 es solo el paso intermedio
                                 #Para luego evaluarlo en nuestra funcion.
            vari=list_y[c]+0.5*paso*(k0+k2) #Metodo de Heun
            list_y.append(vari)   #Almacenamos la variable y
            initiale=initiale+paso  #Continuamos con el siguiente paso
            list_x.append(initiale)  #Almacenamos nuestra variable x
            c=c+1                    #Siguiente step, reitera  el proceso.
        
        list_values=[list_x,list_y] #Entregamos las listas dentro de una lista
                                      #Igual que en el metodo anterior.
        return list_values
    
    
    
def f(x): #Esta es la parte derecha de la ecuacion del moedelo 1. 
          #Cada iteracion de ambos metodos evalua en esta funcion.
    #Primero se definen las constantes
    R=0.1
    Cew=0.27
    gamma=1
    alf=0.612
    tempp= R*x- Cew*gamma*alf*x
    return tempp #Devolvemos un float.
    
    
def solution(x):    #Esta funcion entrega la solucion analitica
                    #de nuestro problema
                    #La forma en que se obtiene, se explica en el documento 
                    #de la tarea.
    
    #Primero se definen las constantes
    R=0.1
    Cew=0.27
    gamma=1
    alf=0.612
    pot=R-alf*gamma*Cew
    y=np.exp(pot*x)
    return y



#####################VARIABLES USADAS EN AMBOS METODOS

va=20.*12. #Este valor representa los 20 años. Sera nuestra xf en ambos.
deltat=[1,0.1, 0.01, 0.005] #En la tarea se pide evaluar para distintos paso.
                            #Estos se almacenan en la lista deltat. 

iv=1. #Initial value. Valor inicial que corresponde a Te(0)=1. Es nuestro seed.

x_real=np.linspace(0,va,2000)   #Esteblecemos 2000 puntos equiespaciados entre 
                                #0 y 240.
y_real=solution(x_real)         #Evaluamos x_real en la funcion analitica.

#####################


#####################

"""METODO DE     E U L E R"""

aprox=[]   #Aqui almacenaremos los valores para 'x' e 'y' para distintos step.

for j in range(len(deltat)):
    eu=Euler(0.0, va ,deltat[j],iv,f) 
    aprox.append(eu)
    
"""I M  P   O    R     T      A       N        T         E

En cada posicion de aprox se almacena una lista con dos listas, de forma que:
    aprox=[[lista_x0,lista_y0],[lista_x1,lista_y1],..., [lista_x3,lista_y3]]]
    Es importante entender que tienen cada una para graficar.

"""


fig, ax = plt.subplots()#Creamos la figura

for m in range(len(aprox)):   #Graficar resultados para distintos steps.
                              #A cada uno le entregamos un label.
    if(m==0):    
        ax.plot(aprox[m][0],aprox[m][1], label="$\Delta t=1$")
    elif(m==1):
        ax.plot(aprox[m][0],aprox[m][1], label="$\Delta t=0.1$")
    elif(m==2):
        ax.plot(aprox[m][0],aprox[m][1], label="$\Delta t=0.01$") 
    elif(m==3):
        ax.plot(aprox[m][0],aprox[m][1], label="$\Delta t=0.005$")    
    
ax.plot(x_real,y_real,'c' ,label="Real")
    
    
plt.legend(handler_map={ax: HandlerLine2D(numpoints=4)})   #Creamos el label.

ax.set_xlabel('t')               #Establecemos titulo a los ejes.
ax.set_ylabel('Te')
fig.suptitle('Metodo de Euler', fontsize=12)   #Titulo de la figura
fig.savefig('Euler_method.png')   #Se guarda la figura en el path actual.
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
    eu=Heun(0.0, va ,deltat[j],iv,f) 
    aprox1.append(eu)


####Repetimos el proceso para graficar del metodo anterior.
plt.legend(handler_map={ax: HandlerLine2D(numpoints=4)})
for m in range(len(aprox)):
    if(m==0):    
        ax1.plot(aprox1[m][0],aprox1[m][1], label="$\Delta t=1$")
    elif(m==1):
        ax1.plot(aprox1[m][0],aprox1[m][1], label="$\Delta t=0.1$")
    elif(m==2):
        ax1.plot(aprox1[m][0],aprox1[m][1], label="$\Delta t=0.01$") 
    elif(m==3):
        ax1.plot(aprox1[m][0],aprox1[m][1], label="$\Delta t=0.005$") 
        
ax1.plot(x_real,y_real,'m' ,label="Real")
        

plt.legend(handler_map={ax1: HandlerLine2D(numpoints=4)})

ax1.set_xlabel('t')
ax1.set_ylabel('Te')
fig1.suptitle('Metodo de Heun', fontsize=12)
fig1.savefig('Heun_method.png')
plt.show()


############################################

#Comparamos ambos metodos para deltat=0.005

fig2, ax2= plt.subplots()

ax2.plot(aprox[3][0],aprox[3][1], label="Euler")
ax2.plot(aprox1[3][0],aprox1[3][1], label="Heun") 
ax2.plot(x_real,y_real,'c' ,label="Real")
plt.legend(handler_map={ax2: HandlerLine2D(numpoints=4)})

ax2.set_xlabel('t')
ax2.set_ylabel('Te')
fig2.suptitle('Euler vs Heun. Step=0.005', fontsize=12)
fig2.savefig('Versus_st05.png')
plt.show()


############################################

#Comparamos ambos metodos para deltat=1

fig3, ax3= plt.subplots()

ax3.plot(aprox[0][0],aprox[0][1],label="Euler")
ax3.plot(aprox1[0][0],aprox1[0][1],'k' ,label="Heun")
ax3.plot(x_real,y_real,'c' ,label="Real") 
plt.legend(handler_map={ax2: HandlerLine2D(numpoints=4)})

ax3.set_xlabel('t')
ax3.set_ylabel('Te')
fig3.suptitle('Euler vs Heun. Step=1', fontsize=12)
fig3.savefig('Versus_st1.png')
plt.show()
