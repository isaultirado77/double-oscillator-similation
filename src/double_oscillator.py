from vpython import canvas, sphere, box, helix, graph, gcurve, vector, color

class Oscillator:
    def __init__(self, mass, spring_constant, rest_length, initial_position, initial_velocity, walls_distance):
        self.mass = mass
        self.spring_constant = spring_constant
        self.rest_length = rest_length
        self.position = vector(initial_position, 0, 0)
        self.velocity = vector(initial_velocity, 0, 0)
        self.acceleration = vector(0, 0, 0)
        self.walls_distance = walls_distance

        self.left_wall = vector(-walls_distance, 0, 0)
        self.right_wall = vector(walls_distance, 0, 0)

    def calculate_acceleration(self):
        left_spring_force = -self.spring_constant * (mag(self.position - self.left_wall) - self.rest_length) * norm(self.position - self.left_wall)
        right_spring_force = -self.spring_constant * (mag(self.position - self.right_wall) - self.rest_length) * norm(self.position - self.right_wall)
        total_force = left_spring_force + right_spring_force
        self.acceleration = total_force / self.mass

    def update_position_and_velocity(self, dt):
        self.calculate_acceleration()
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

class Simulation:
    def __init__(self, oscillator, simulation_time, time_steps):
        self.oscillator = oscillator
        self.simulation_time = simulation_time
        self.time_steps = time_steps
        self.dt = simulation_time / time_steps
        self.time = 0

        # Visualization setup
        self.scene = canvas(title="Sistema masa - dos resortes", width=800, height=400, center=vector(0, 0, 0), background=color.white)
        self.mass = sphere(pos=self.oscillator.position, radius=0.15, color=color.red)
        self.left_wall = box(pos=self.oscillator.left_wall, size=vector(0.05, 1, 1.5), color=color.blue)
        self.right_wall = box(pos=self.oscillator.right_wall, size=vector(0.05, 1, 1.5), color=color.blue)
        self.left_spring = helix(pos=self.oscillator.left_wall, axis=self.mass.pos - self.left_wall.pos, radius=0.05, coils=20, thickness=0.02, color=color.gray(0.5))
        self.right_spring = helix(pos=self.oscillator.right_wall, axis=self.mass.pos - self.right_wall.pos, radius=0.05, coils=20, thickness=0.02, color=color.gray(0.5))

        # Graph setup
        self.graph = graph(title="Sistema masa - dos resortes: x vs t", xtitle="Tiempo (s)", ytitle="Posición (m)", background=color.white)
        self.position_curve = gcurve(color=color.red)

    def run(self):
        while self.time < self.simulation_time:
            rate(1000)  # Control the simulation speed

            # Update oscillator dynamics
            self.oscillator.update_position_and_velocity(self.dt)

            # Update visualization
            self.mass.pos = self.oscillator.position
            self.left_spring.axis = self.mass.pos - self.left_wall.pos
            self.right_spring.axis = self.mass.pos - self.right_wall.pos

            # Update graph
            self.position_curve.plot(self.time, self.oscillator.position.x)

            # Advance time
            self.time += self.dt

if __name__ == "__main__":
    # Parameters for the simulation
    mass = 0.03  # kg
    spring_constant = 4.0  # N/m
    rest_length = 0.5  # m
    initial_position = 0.0  # m
    initial_velocity = 12.5  # m/s
    walls_distance = 1.0  # m
    simulation_time = 1.5  # seconds
    time_steps = 1000

    # Initialize the oscillator and simulation
    oscillator = Oscillator(mass, spring_constant, rest_length, initial_position, initial_velocity, walls_distance)
    simulation = Simulation(oscillator, simulation_time, time_steps)

    # Run the simulation
    simulation.run()
