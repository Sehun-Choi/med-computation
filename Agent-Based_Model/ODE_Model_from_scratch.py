import numpy as np, matplotlib.pyplot as plt

# --- Set Initial Parameters ---
N = 1000 # Total population
I0 = 1 # Initial number of infected individuals
S, I, R = N-I0, I0, 0 # Initial number of susceptible, infected, and recovered individuals
beta, gamma = 0.1, 0.015 # Infection and recovery rates

T = 600 # Total time steps for the simulation
dt = 0.01

Sarr = [S]; Iarr = [I]; Rarr = [R]; Tarr = [1]

# --- Core Logic ---
def update_SIR(S, I, R, N, beta, gamma, dt):
    dSdt = -beta * S * I / N
    dRdt = gamma * I
    dIdt = -dSdt - dRdt
    S += dSdt * dt; I += dIdt * dt; R += dRdt * dt
    return S, I, R

# --- Main Simulation ---
for t in np.arange(0, T, dt):
    S, I, R = update_SIR(S, I, R, N, beta, gamma, dt)
    Sarr.append(S); Iarr.append(I); Rarr.append(R);
    Tarr.append(t)

# --- Visualization ---
plt.plot(Tarr, Sarr, label="Susceptible", color="blue", linewidth=2)
plt.plot(Tarr, Iarr, label="Infected", color="red", linewidth=2)
plt.plot(Tarr, Rarr, label="Recovered", color="green", linewidth=2)

plt.title("ODE Model")
plt.xlabel("Time (Days)")
plt.ylabel("Number of people")
plt.legend(loc="best")

plt.show()