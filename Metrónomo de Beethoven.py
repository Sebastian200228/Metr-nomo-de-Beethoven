#Importación de las Librerias a utilizar.
from matplotlib.widgets import Slider,Button
import matplotlib.pyplot as plt
from scipy.special import factorial2
from numpy import sin, deg2rad
import numpy as np

#%matplotlib qt #Sirve para la visualización del Gráfico, mediante una ventana externa.

#Definición de las funciones a utilizar.
def f_ang (theta) : #Función correspondendiente a la ecuación 2 del 'Paper' - Función del Angulo θ¸.
    Sumatoria = np.array([(((factorial2((2 * n) - 1)) / (factorial2(2 * n))) * ((sin(deg2rad(theta) / 2)) ** (2 ** n))) ** 2 for n in range(1, 151)])
    return 1 + np.sum(Sumatoria)

def a_0 (g, theta, M, m, R, u, L, l) : #Función correspondendiente a la ecuación 5 del 'Paper' - Función de a_0.
    return (g / (f_ang(theta) ** 2)) * ((M / m) * R - ((u / m) / 2) * (l - L)) / ((M / m) * (R ** 2) + ((u / m) / 3) * ((L ** 2) + (l ** 2) - l * L))

def b_2 (M, m, R, L, l, u) : #Función correspondendiente a la ecuación 6 del 'Paper' - Función de b_2.
    return - ((1) / ((M / m) * (R ** 2) + ((u / m) / 3) * ((L ** 2) + (l ** 2) - (l * L))))

def Omega(g, r, theta, M, m, R, u, L, l) : #Función correspondendiente a la ecuación 4 del 'Paper' - Modelo transformado de Ω^2.
    return (( (a_0 (g, theta, M, m, R, u, L, l)) + ((b_2 (M, m, R, L, l, u)) / (f_ang(theta) ** 2)) * r * g) / ( 1 - ((r ** 2) * (b_2 (M, m, R, L, l, u)))))

def Actualizar(val): #Función para los cambios en los Slider, que modifican a la Gráfica.
    #Modifica la gráfica en el eje 'y', de acuerdo a los valores de la función Omega, tomando los valores de los Sliders.
    line.set_ydata(Omega(Gravedad.val, rs, Theta.val, Masa.val, masa.val, Radio.val, Varilla.val, Longitud.val, longitud.val))
    fig.canvas.draw_idle() #Grafica las modificaciones que se han realizado en la figura.

def Reiniciar(val): #Resetea los valores de los Sliders a sus valores iniciales.
    Gravedad.reset()
    Theta.reset()
    Masa.reset()
    masa.reset()
    Radio.reset()
    Varilla.reset()
    Longitud.reset()
    longitud.reset() 

rs = np.linspace(40, 208, 60, endpoint = True) #Asigna los valores al eje 'x' (mm) y resalta 60 datos de la Gráfica.

#Declaración de los diferentes valores iniciales de las variables, para la fijación de los Sliders.
g_i = 9807 
theta_i = 50
M_i = 29.54
m_i = 6.76
R_i = 51.5
u_i = 3.42
L_i = 28.36
l_i = 206.64

fig = plt.figure(figsize = (16, 7)) #Definición de las dimensiones del Lienzo, en donde va la Gráfica con los Sliders. 
G_P = plt.axes((0.15, 0.6, 0.7, 0.3)) #Espacio desigando para la Gráfica con las respectivas dimensiones (izquierda, abajo, ancho, alto).

#Etiquetas y agregados asignados a la Gráfica.
G_P.set_ylim(-20,100) 
G_P.set_xlabel('r (mm)', weight='bold', size=15,)
G_P.set_ylabel('Frecuencia angular de \nOscilación ($Ω^{2}$)', weight='bold', size=15)
G_P.set_title('Metrónomo de Beethoven', weight='bold', size = 25)
plt.grid(True)

#Realiza la Gráfica, en el espacio principal designado, tomando como argumentos los valores inciales de las Variables, con el eje 'x'.
line ,= G_P.plot(rs, Omega(g_i, rs, theta_i, M_i, m_i, R_i, u_i, L_i, l_i), '-ok', label = 'Posibles Distorsiones del Metrónomo de Beethoven', color = 'royalblue')
plt.legend()

#Asignación de los subnombres y dimensiones de los Sliders.
G_s = plt.axes((0.55, 0.45, 0.30, 0.05)) 
Ang_s = plt.axes((0.15, 0.45, 0.30, 0.05)) 
M_s = plt.axes((0.15, 0.15, 0.30, 0.05)) 
m_s = plt.axes((0.15, 0.35, 0.30, 0.05)) 
R_s = plt.axes((0.55, 0.25, 0.30, 0.05)) 
u_s = plt.axes((0.15, 0.25, 0.30, 0.05)) 
L_s = plt.axes((0.55, 0.15, 0.30, 0.05)) 
l_s = plt.axes((0.55, 0.35, 0.30, 0.05))  
B_s = plt.axes((0.45, 0.07, 0.1, 0.05))  #Botón.

#Asignación y relleno de los Sliders con sus respectivos parámetros.
Gravedad = Slider(ax = G_s, label = 'g (mm/$s^{2}$)', valmin = 40, valmax = 9807, valinit = g_i, valstep = 100, color = 'lightsteelblue')
Theta = Slider(ax = Ang_s, label = 'θ (°)', valmin = 40, valmax = 60, valinit = theta_i, valstep = 1, color = 'greenyellow')
Masa = Slider(ax = M_s, label = 'M (g)', valmin = 23.63 , valmax = 35.44, valinit = M_i, valstep = 0.5, color = 'peru')
masa = Slider(ax = m_s, label = 'm (g)', valmin = 5.41, valmax = 8.11, valinit = m_i, valstep = 0.1, color = 'darkgoldenrod')
Radio = Slider(ax = R_s, label = 'R (mm)', valmin = 35, valmax = 68, valinit = R_i, valstep = 1.5, color = 'coral')
Varilla = Slider(ax = u_s, label = 'u (g)', valmin = 2.74, valmax = 4.1, valinit = u_i, valstep = 0.1, color = 'mediumaquamarine')
Longitud = Slider(ax = L_s, label = 'L (mm)', valmin = 22.53, valmax = 34.2 , valinit = L_i, valstep = 0.5, color = 'slategray')
longitud = Slider(ax = l_s, label = 'l (mm)', valmin = 157.47, valmax = 255.8, valinit = l_i, valstep = 10, color = 'silver')
bot1 = Button(ax = B_s, label = 'Reiniciar') #Asigna el relleno del Botón 'Reiniciar'.

#Hace un llamado a la Función Actualizar, mediante el 'controlador de eventos' on_changed.
Gravedad.on_changed(Actualizar)
Theta.on_changed(Actualizar)
Masa.on_changed(Actualizar)
masa.on_changed(Actualizar)
Radio.on_changed(Actualizar)
Varilla.on_changed(Actualizar)
Longitud.on_changed(Actualizar)
longitud.on_changed(Actualizar)
bot1.on_clicked(Reiniciar) #Hace un llamado a la Función Reiniciar, mediante el 'controlador de eventos' on_clicked.