import numpy as np
import matplotlib.pyplot as plt

def funcion_de_forma(r, rs, sigma):
    """Función de forma que describe la deformación del espacio-tiempo."""
    return (np.tanh(sigma * (r + rs)) - np.tanh(sigma * (r - rs))) / (2 * np.tanh(sigma * rs))

def metrica_alcubierre(x, y, t, vt, rs, sigma):
    """Calcula la métrica de Alcubierre en un punto (x, y)."""
    r = np.sqrt(y**2) #Distancia desde el eje x
    f = funcion_de_forma(r, rs, sigma)
    alfa = -(1 - vt**2 * f**2)
    beta = vt * f
    gamma = 1
    return alfa, beta, gamma

# Parámetros
vt = 0.5  # Velocidad de la burbuja
rs = 1.0  # Radio de la burbuja
sigma = 10 # Controla la nitidez de la transicion.
t = 0.0   # Tiempo

# Crea una malla
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calcula la métrica en cada punto de la malla
alfa, beta, gamma = metrica_alcubierre(X, Y, t, vt, rs, sigma)

# Visualiza la componente alfa de la métrica (g_tt)
plt.figure(figsize=(10, 6))
plt.imshow(alfa, extent=[-5, 5, -5, 5], origin='lower', cmap='viridis')
plt.colorbar(label='Componente alfa (g_tt)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Componente g_tt de la métrica de Alcubierre')
plt.show()

#Visualiza la componente beta de la metrica(g_tx)
plt.figure(figsize=(10, 6))
plt.imshow(beta, extent=[-5, 5, -5, 5], origin='lower', cmap='viridis')
plt.colorbar(label='Componente beta (g_tx)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Componente g_tx de la métrica de Alcubierre')
plt.show()