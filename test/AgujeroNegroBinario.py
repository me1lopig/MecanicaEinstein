from einsteinpy.bodies import Body
from einsteinpy.simulation import NBodySystem

# Definir dos agujeros negros
bh1 = Body(name="BH1", mass=10.0, position=[0.0, 0.0, 0.0], velocity=[0.0, 0.0, 0.0])
bh2 = Body(name="BH2", mass=10.0, position=[10.0, 0.0, 0.0], velocity=[0.0, 0.1, 0.0])

# Crear el sistema de N cuerpos
system = NBodySystem(bodies=[bh1, bh2])

# Simular el sistema
trajectories = system.simulate(end_time=100.0, step_size=0.1)

# Visualizar las trayectorias
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
for body, trajectory in trajectories.items():
    ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], label=body)
ax.set_title("Agujero negro binario")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.legend()
plt.show()