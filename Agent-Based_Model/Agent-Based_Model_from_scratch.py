import numpy as np, matplotlib.pyplot as plt

# --- Set Initial Parameters ---
N = 1000; I0 = 1; T = 600
beta, gamma = 0.1, 0.015 # Infection and recovery rates
dt = 0.1

# --- Initialization ---
# 1: infected, 0: susceptible, -1: recovered
state = np.zeros(N, dtype=int)
state[np.random.choice(N, size=I0, replace=False)] = 1

S = N - I0
R = 0
Sarr = [S]; Iarr = [I0]; Rarr = [R]; Tarr = [0]

# --- Main Logic ---
for t in np.arange(0, T, dt):
    statenew = state.copy()
    Ilist = np.where(state == 1)[0]
    for infected_person in Ilist:
        bumped_person_index = np.random.randint(N)
        state_of_bumped_person = state[bumped_person_index]
        if state_of_bumped_person == 0:
            if np.random.rand() < (beta * dt):
                statenew[bumped_person_index] = 1
        if np.random.rand() < (gamma * dt):
            statenew[infected_person] = -1
    S = np.sum(statenew == 0)
    I = np.sum(statenew == 1)
    R = N - I - S
    Sarr.append(S); Iarr.append(I); Rarr.append(R)
    Tarr.append(t + dt)
    state = statenew

# --- Visualization ---
plt.plot(Tarr, Sarr, label="Susceptible", color="blue", linewidth=2)
plt.plot(Tarr, Iarr, label="Infected", color="red", linewidth=2)
plt.plot(Tarr, Rarr, label="Recovered", color="green", linewidth=2)

plt.title("Agent-Based Model")
plt.xlabel("Time (Days)")
plt.ylabel("Number of People")
plt.legend(loc="best")

plt.show()