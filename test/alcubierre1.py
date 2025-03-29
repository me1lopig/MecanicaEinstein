import numpy as np
import matplotlib.pyplot as plt

def funcion_de_forma(r, rs):
    """Función de forma que describe la deformación del espacio-tiempo."""
    return (rs**2 * (rs**2 - r**2)) / (rs**2 + r**2)**2

def metrica_alcubierre(x, y, t, vt, rs):
    """Calcula la métrica de Alcubierre en un punto (x, y)."""
    r = np.sqrt((x - vt * t)**2 + y**2)
    f = funcion_de_forma(r, rs)
    alfa = -vt * f
    beta = 0
    gamma = 1 - vt**2 * f**2
    return alfa, beta, gamma

# Parámetros
vt = 0.5  # Velocidad de la burbuja
rs = 1.0  # Radio de la burbuja
t = 0.0   # Tiempo

# Crea una malla
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Calcula la métrica en cada punto de la malla
alfa, beta, gamma = metrica_alcubierre(X, Y, t, vt, rs)

# Visualiza la deformación del espacio-tiempo
plt.figure(figsize=(8, 6))
plt.imshow(gamma, extent=[-5, 5, -5, 5], origin='lower', cmap='viridis')
plt.colorbar(label='Componente gamma de la métrica')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Deformación del espacio-tiempo (Métrica de Alcubierre)')
plt.show()