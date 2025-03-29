import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import streamlit as st


def main():
    # Constantes
    G = 6.67430e-11
    M = 1.989e30
    m = 5.972e24

    # Condiciones iniciales
    r0 = 1.496e11
    v0 = 2.978e4
    theta0 = 0

    # Parámetros de la simulación (ajustables con Streamlit)        
    dt = st.sidebar.slider("Tamaño del paso de tiempo (días)", 0.1, 3.0, 1.0) * 3600 * 24
    t_total = 365.25 * 24 * 3600
    n_steps = int(t_total / dt)

    # Arrays para almacenar los resultados
    t = np.zeros(n_steps)
    r = np.zeros(n_steps)
    theta = np.zeros(n_steps)
    vx = np.zeros(n_steps)
    vy = np.zeros(n_steps)
    x = np.zeros(n_steps)
    y = np.zeros(n_steps)

    # Inicialización
    t[0] = 0
    r[0] = r0
    theta[0] = theta0
    vx[0] = 0
    vy[0] = v0
    x[0] = r0 * np.cos(theta0)
    y[0] = r0 * np.sin(theta0)

    # Bucle de simulación
    for i in range(1, n_steps):
        F = G * M * m / r[i-1]**2
        ax = -F / m * np.cos(theta[i-1])
        ay = -F / m * np.sin(theta[i-1])
        vx[i] = vx[i-1] + ax * dt
        vy[i] = vy[i-1] + ay * dt
        x[i] = x[i-1] + vx[i-1] * dt
        y[i] = y[i-1] + vy[i-1] * dt
        r[i] = np.sqrt(x[i]**2 + y[i]**2)
        theta[i] = np.arctan2(y[i], x[i])
        t[i] = t[i-1] + dt

    # Configuración de la figura y los ejes
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-2*r0, 2*r0)
    ax.set_ylim(-2*r0, 2*r0)
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_title('Animación de la Órbita de la Tierra alrededor del Sol')
    ax.grid(True)

    # Inicialización de los objetos que se animarán
    sun, = ax.plot(0, 0, marker='o', markersize=15, color='yellow', label='Sol')
    earth, = ax.plot([], [], marker='o', markersize=8, color='blue', label='Tierra')
    orbit, = ax.plot([], [], linestyle='--', color='gray', linewidth=0.5, label='Órbita')

    # Función de inicialización para la animación
    def init():
        sun.set_data(0, 0)
        earth.set_data([], [])
        orbit.set_data([], [])
        return sun, earth, orbit

    # Función de animación
    def animate(i):
        earth.set_data(x[i], y[i])
        orbit.set_data(x[:i], y[:i])
        return sun, earth, orbit

    # Creación de la animación
    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=n_steps, blit=True, repeat=False)

    # Mostrar la animación en Streamlit
    st.title('Simulación de la Órbita de la Tierra alrededor del Sol')
    st.pyplot(fig)


if __name__ == "__main__":
    main()