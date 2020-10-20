# -*- coding: utf-8 -*-
"""
@author: Camila Fernanda Guzmán Lara, camila.guzman.l@ug.uchile.cl
         Esteban Andrés Flores Gutiérrez, esteban.flores@ug.uchile.cl

                   *     *  * P R O B L E M A   C *  *     *


"""

#######################################################
"""###########Funcionamiento del programa"""###########
#######################################################
"""####################################################

En este problema se implementa el metodod de Euler con el metodo de 
Runge-Kutta de cuarto orden (RK4).
Esta vez es para resolver el Modelo 2 que es un sistema de ecuaciones 
diferenciales de dos variables.
El metodo de Euler es el mismo implementado en el caso anterior. 
No cambia su estructura.
El metodo RK4 es similar a los anterior, pero este tiene cuatro pasos 
intermedios.

Ahora se deben entregar dos condiciones iniciales.


Los argumentos de las funciones son:
    
    X_I: El primer valor del intervalo en el que queremos resolver nuestra 
    ecuacion diferencial, en nuestro caso es x0=0[meses]
    
    X_F: Cota superior del intervalo de interes. En nuestro caso queremos 
    obtener para 20 años, como la unidad corresponde a mes -> xf=20*12[meses].
    
    h: El valor del paso entre x_n y x_n+1. Lo definimos como 
    x_(n+1)-x_n=h, en nuestro caso definiremos el step dentro de una 
    lista: deltat=[1,0.1, 0.01, 0.005]. Resolveremos la ecuacion del 
    Modelo 1 con ambos metodos con todos estos valores.
    
    X_00: Todo problema de valor inicial requiere de condiciones iniciales. 
    En este problema, al resolver para Te y He, y al ser una EDO de primer 
    orden, requiere una doble condicion, que en este caso es 
    Te(0)=1 y He(0)=-1. Ambas condiciones las entregamos en formato de array. 
    
    func: Como ambos metodos estan desarrollados para una EDO de la forma 
    y'(t,x)=f(Te,t), debemos especificar nuestra funcion a resolver que 
    corresponde a la mostrada en el Modelo 2 del enunciado de la tarea.
    En este caso es un array de dos funciones. 
    
    
    
"""##########################################################################


import math as mt
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import numpy as np
import time


def RK4(X_I, X_F, h, X_00, F):
    anos=X_F  #Cota superior en el tiempo
    num=int(anos/h) #Cantidad de iteraciones
    delta_t = h #Pasos
    X_N=X_00  #Primer paso
   
    
    #Creamos las variables entre cada paso.
    K_1=F(X_N) 
    
    K_2=K_1
    K_3=K_1
    K_4=K_1
    t = X_I
    
    #Se crean las listas donde se guardan los valores
    #Obtenidos para ambos ejes
    
    tfinal=[]
    X_Nfinal=[]
    for i in range(num+1):
        tfinal.append(0.)
        X_Nfinal.append(0.)
   
    
    con=0
    




    while (t < anos):
        
        #Calculamos los pasos intermedios 
        #Para obtener el valor de la siguiente posicion en 'y'
        
        #F devuelve un array con dos valores. En la posicion 0 esta Te,
        #en la posicion 1 esta Hw.
        
        K_1 = F(X_N)*delta_t  #Primera pendiente
        K_2 = F(X_N + 0.5*K_1)*delta_t #Pendiente intermedia
        K_3 = F(X_N + 0.5*K_2)*delta_t #Pendiente intermedia
        K_4 = F(X_N + K_3)*delta_t #Pendiente en el final
	
        final= X_N + (K_1 + 2.*K_2 + 2.*K_3 + K_4)/6. #RK4
        X_N= final
        #X_N es un array que contiene el valor de Te y Hw
        
        #Agregamos los valores en sus respectivas listas
        t=t+delta_t
        tfinal[con]=t
        X_Nfinal[con]=X_N 
        
        con=con+1 #Avanzamos al siguiente paso y se repite el ciclo
        #print("Metodo RK4")
        #print("Mes: "+str(t)+"; Con step de: "+ str(delta_t))
    

    """********** I M P O R T A N T E **********    
    Finalmente se devuelve una tupla con el tiempo y los valores del
    tiempo, que es una lista. Mientras que X_Nfinal es una lista que contiene 
    dos array. Uno con los valores de Te en la posicion 0 y Hw en la
    posicion 1:
        
    (tfinal, [Te, Hw])"""
    
    return (tfinal, X_Nfinal)


def Euler(X_I, X_F, h, X_00, F):
    #Este metodo es igual a los metodos de Euler presentados anteriormente
    
    anos=X_F       #Cota superior
    num=int(anos/h)  #Cantidad de puntos a guardar
    delta_t = h     #Paso
    X_N=X_00
    t = X_I     
    K_1=F(X_N)
    tfinal=[]   #Listas donde guardaremos los valores de tiempo
    X_Nfinal=[]  #Lista que tendran los array con las soluciones.
    for i in range(num+1):   #Llenamos las lista de ceros 
                             #Y luego los reemplazaremos con los valores
        tfinal.append(0.)
        X_Nfinal.append(0.)
        
        
    con=0
        
    while (t < anos):
       
        #F devuelve un array con dos valores. En la posicion 0 esta Te,
        #en la posicion 1 esta Hw.
        
        K_1 = F(X_N)*delta_t #Calculamos la pendiente
        K_2 = F(X_N + 0.5*K_1)*delta_t #Metodo de Euler
        #K_3 = F(X_N - K_1+2*K_2)*delta_t
        final= X_N + (K_1+K_2)/2.
        X_N= final
	
        
        
        tfinal[con]=t  #Almacenados la variable temporal
        X_Nfinal[con]=final  #Se almacenan las variables 
        t=t+delta_t
        con=con+1 #avanzamos al siguiente paso y se repite el ciclo
    
        #print("Metodo de Euler")
        #print("Mes: "+str(t)+"; Con step de: "+ str(delta_t))
    
    return (tfinal, X_Nfinal)

"""********** I M P O R T A N T E **********    
    Finalmente se devuelve una tupla con el tiempo y los valores del
    tiempo, que es una lista. Mientras que X_Nfinal es una lista que contiene 
    dos array. Uno con los valores de Te en la posicion 0 y Hw en la
    posicion 1:
        
    (tfinal, [Te, Hw])"""
        
        

def ENSO(x):
     
    
    #Se define el modelo 2 que consta de dos ecuaciones. 
    #Se establecen los valores de las constantes
    r_c=0.1
    r_g=0.1
    Cew1=0.27
    gamma_1=1.
    gamma_2=0.164
    alpha= 0.612
  
  
  
    aux=np.zeros(2)
    aux[0]=r_g*x[0]+gamma_2*Cew1*x[1] #dTe/dt
    aux[1]=-r_c*x[1]-alpha*x[0]      #dHw/dt
  
  
    #Se retorma un array.
      
    return aux

def TH(lista_var):
    #Esta funcion se usa para extraer y separar los valores de Te y Hw
    #Basicamente para graficar
    
    Teg=[]
    Heg=[]
    
    for j in range(len(lista_var)):
        
        Teg.append(lista_var[j][0])
        Heg.append(lista_var[j][1])
    return[Teg,Heg] 


start_time = time.time()
#####################VARIABLES USADAS EN AMBOS METODOS
iv=0.0 #Initial Value. Cota inferior
va=20.*12.  #Cota superior de la variable temporal
deltat=[1,0.1, 0.01, 0.005] #Valores para los pasos
p=np.zeros(2) #Condicion inicial
p[0]=1.
p[1]=-1.
#######################################################

"""M e t o d o   d e    E  U  L  E  R"""

###Variamos el paso
var0=Euler(iv, va ,deltat[0],p,ENSO) 
var1=Euler(iv, va ,deltat[1],p,ENSO) 
var2=Euler(iv, va ,deltat[2],p,ENSO) 
var3=Euler(iv, va ,deltat[3],p,ENSO) 

"""Extramos las variables Te y He y las separamos en distintas listas."""
Te0=TH(var0[1][0:len(var0[1])-1])
Hw0=Te0[1]
Te0=Te0[0]

Te1=TH(var1[1])
Hw1=Te1[1]
Te1=Te1[0]


Te2=TH(var2[1])
Hw2=Te2[1]
Te2=Te2[0]


Te3=TH(var3[1])
Hw3=Te3[1]
Te3=Te3[0]




####Creamos las figuras para el metodo de Euler.

fig1, ax1= plt.subplots()

ax1.plot(var0[0][0:len(var0[1])-1],Te0, label="$\Delta t=1$")
ax1.plot(var1[0],Te1, label="$\Delta t=0.1$")
ax1.plot(var2[0],Te2, label="$\Delta t=0.01$")
ax1.plot(var3[0],Te3, label="$\Delta t=0.005$")
plt.legend(handler_map={ax1: HandlerLine2D(numpoints=4)})

ax1.set_xlabel('t')
ax1.set_ylabel('Te')
fig1.suptitle('Te: Metodo de Euler dos variables', fontsize=12)
fig1.savefig('Euler-2-variables-Te.png')

plt.show()


fig2, ax2= plt.subplots()

ax2.plot(var0[0][0:len(var0[1])-1],Hw0, label="$\Delta t=1$")
ax2.plot(var1[0],Hw1, label="$\Delta t=0.1$")
ax2.plot(var2[0],Hw2, label="$\Delta t=0.01$")
ax2.plot(var3[0],Hw3, label="$\Delta t=0.005$")
plt.legend(handler_map={ax2: HandlerLine2D(numpoints=4)})

ax2.set_xlabel('t')
ax2.set_ylabel('Te')
fig2.suptitle('Hw: Metodo de Euler dos variables', fontsize=12)
fig2.savefig('Euler-2-variables-Hw.png')

plt.show()

#################################################


"""R          K                C U A T R O"""#*****************************

##Se aplica el metodo para diferentes pasos.

var10=RK4(iv, va ,deltat[0],p,ENSO)
var11=RK4(iv, va ,deltat[1],p,ENSO) 
var12=RK4(iv, va ,deltat[2],p,ENSO) 
var13=RK4(iv, va ,deltat[3],p,ENSO) 


#Separamos las variables obtenidas para Te y Hw
Te10=TH(var10[1][0:len(var10[1])-1])
Hw10=Te10[1]
Te10=Te10[0]

Te11=TH(var11[1])
Hw11=Te11[1]
Te11=Te11[0]

Te12=TH(var12[1])
Hw12=Te12[1]
Te12=Te12[0]

Te13=TH(var13[1])
Hw13=Te13[1]
Te13=Te13[0]

##########################

####Creamos las figuras para el RK4. Primero para Te

fig3, ax3= plt.subplots()

ax3.plot(var10[0][0:len(var10[0])-1],Te10, label="$\Delta t=1$")
ax3.plot(var11[0],Te11, label="$\Delta t=0.1$")
ax3.plot(var12[0],Te12, label="$\Delta t=0.01$")
ax3.plot(var13[0],Te13, label="$\Delta t=0.005$")
plt.legend(handler_map={ax3: HandlerLine2D(numpoints=4)})

ax3.set_xlabel('t')
ax3.set_ylabel('Te')
fig3.suptitle('Te - Metodo RK4 dos variables', fontsize=12)
fig3.savefig('RK4-2-variables-Te.png')
plt.show()

#################

fig4, ax4= plt.subplots()

ax4.plot(var10[0][0:len(var10[0])-1],Hw10, label="$\Delta t=1$")
ax4.plot(var11[0],Hw11, label="$\Delta t=0.1$")
ax4.plot(var12[0],Hw12, label="$\Delta t=0.01$")
ax4.plot(var13[0],Hw13, label="$\Delta t=0.005$")
plt.legend(handler_map={ax4: HandlerLine2D(numpoints=4)})

ax4.set_xlabel('t')
ax4.set_ylabel('Te')
fig4.suptitle('Hw - Metodo RK4 dos variables', fontsize=12)
fig4.savefig('RK4-2-variables-Hw.png')
plt.show()

""""""""""""""""""""""""""


#Ahora se analizara el problema d. Y para ello se utilizaran los datos
#obtenidos mediante el metodo RK4 con deltat=0.005.
#Buscaremos los minimos en intervalos de t=[0,50]. Se guardaran,
#Para aasi establecer un periodo y se verificara con el valor real.


#print(int(50./deltat[3])) #Cuantos indices hay cada 50 meses
menores=[] #Aqui se alamacenan los valores minimos.
menoresy=[]
for i in range(0,48000, 10000):
    c=float('inf')
    d=0
    
    if(i!=40000):
        for j in range(i,i+10000):
            
            if(Te13[j]<c):
                
                c=Te13[j]
                d=var13[0][j]
        
        menores.append(d)
        menoresy.append(c)
        
    else:
        for j in range(i,i+8000):
            if(Te13[j]<c):
                c=Te13[j]
                d=var13[0][j]
        menores.append(d)
        menoresy.append(c)
        


#########Se calcula el periodo medio
print(menores)
print(menoresy)
periodos=np.zeros(4)
for i in range(1, len(menores)):
    resta=menores[i]-menores[i-1]
    periodos[i-1]=resta

sumas=np.sum(periodos)
sumas=sumas/4
print("El periodo numerico es: " + str(sumas))

############Ahora se calcula el periodo teorico, obtenido analiticamente.

r_c=0.1
r_g=0.1
Cew1=0.27
gamma_1=1.
gamma_2=0.164
alpha= 0.612

P=2*mt.pi*1/mt.sqrt(gamma_2*Cew1*alpha-((r_c+r_g)**2/4))
print("El valor teorico del periodo, es: "+ str(P))

print("--- %s seconds ---" % (time.time() - start_time))






