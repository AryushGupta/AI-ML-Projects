# Reinforcement Learning for Thin-Film Deposition

A simple Reinforcement Learning project that uses **Deep Q-Network
(DQN)** to learn how to control a simulated thin-film deposition
process.

## How RL Was Implemented

The project follows the standard Reinforcement Learning loop:

``` text
State
  ↓
RL Agent
  ↓
Action
  ↓
Environment
  ↓
Reward + Next State
  ↓
RL Agent
```

The agent repeatedly interacts with the deposition environment and
learns which actions lead to better results.

## 1. Environment

We created a custom Gymnasium environment:

``` python
ThinFilmDepositionEnv
```

The environment is responsible for:

-   Maintaining the current process state
-   Applying the agent's actions
-   Simulating the deposition response
-   Calculating film quality
-   Calculating the reward
-   Deciding when an episode ends

## 2. State

The agent observes 7 process variables:

``` text
Temperature
Pressure
Precursor flow
Carrier gas flow
RF power
Deposition time
Current film thickness
```

In code:

``` python
state = [
    temperature,
    pressure,
    precursor_flow,
    carrier_flow,
    rf_power,
    deposition_time,
    current_thickness
]
```

These values describe the current condition of the deposition process.

## 3. Action Space

A **discrete action space** with 13 possible actions was used.

  Action   Operation
  -------- -----------------------------------
  0        Do nothing
  1        Increase temperature by 5°C
  2        Decrease temperature by 5°C
  3        Increase pressure by 0.1 Torr
  4        Decrease pressure by 0.1 Torr
  5        Increase precursor flow by 5 sccm
  6        Decrease precursor flow by 5 sccm
  7        Increase carrier flow by 5 sccm
  8        Decrease carrier flow by 5 sccm
  9        Increase RF power by 10 W
  10       Decrease RF power by 10 W
  11       Increase deposition time by 1 s
  12       Decrease deposition time by 1 s

A discrete action space makes the problem suitable for **DQN**.

## 4. Environment Transition

After receiving an action, the environment updates the process
parameters.

``` text
Current state
     ↓
Agent chooses an action
     ↓
Environment updates process parameter
     ↓
Deposition process is simulated
     ↓
New thickness and film quality
     ↓
Next state
```

The environment uses simplified mathematical relationships to simulate
how process parameters affect deposition.

## 5. Film Quality

After every action, the environment calculates:

-   **Next film thickness**
-   **Film uniformity**
-   **Defect rate**

The target conditions are approximately:

``` text
Film thickness ≈ 100 nm
Film uniformity ≥ 95%
Defect rate ≤ 1.5%
```

## 6. Reward Function

The reward encourages:

-   Film thickness close to 100 nm
-   High film uniformity
-   Low defect rate
-   Reasonable deposition time

Conceptually:

``` text
Higher reward → thickness closer to target
Higher reward → better uniformity
Lower reward  → higher defect rate
Lower reward  → excessive deposition time
```

A bonus is given when the desired thickness and quality conditions are
reached.

The agent therefore learns to maximize the **long-term cumulative
reward**.

## 7. Episode Termination

An episode ends when the process reaches the desired conditions:

``` text
Thickness error ≤ 2 nm
Uniformity ≥ 95%
Defect rate ≤ 1.5%
```

An episode is also truncated after:

``` text
Maximum steps = 50
```

This prevents an episode from continuing indefinitely.

## 8. DQN Agent

We used **Deep Q-Network (DQN)** with Stable-Baselines3.

``` python
from stable_baselines3 import DQN

model = DQN(
    policy="MlpPolicy",
    env=env,
    learning_rate=1e-3,
    buffer_size=10000,
    learning_starts=1000,
    batch_size=64,
    gamma=0.99,
    train_freq=4,
    target_update_interval=500,
    exploration_fraction=0.3,
    exploration_final_eps=0.05,
    verbose=1,
    seed=42
)
```

The DQN receives the current state and estimates a Q-value for each of
the 13 actions.

``` text
Current State
      ↓
Neural Network
      ↓
Q0 Q1 Q2 ... Q11 Q12
      ↓
Select an action
```

## 9. Training

The agent is trained by interacting with the environment:

``` python
model.learn(
    total_timesteps=50_000,
    progress_bar=True
)
```

During training:

``` text
State
  ↓
Choose action
  ↓
Environment
  ↓
Reward + next state
  ↓
Update DQN
  ↓
Repeat
```

Initially, the agent explores different actions. Over time, it learns
which actions are expected to produce higher rewards.

## 10. Testing

After training, the agent can be tested using deterministic actions:

``` python
obs, info = env.reset()

for step in range(50):

    action, _ = model.predict(
        obs,
        deterministic=True
    )

    obs, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        break
```

The test tracks:

-   Action
-   Film thickness
-   Film uniformity
-   Defect rate
-   Reward

## 11. Overall Workflow

``` text
Synthetic Deposition Process
          ↓
Custom Gymnasium Environment
          ↓
Define State
          ↓
Define Action Space
          ↓
Define Reward
          ↓
DQN Agent
          ↓
Training
          ↓
Testing
          ↓
Learned Deposition Policy
```

## Technologies Used

-   Python
-   NumPy
-   Pandas
-   Gymnasium
-   Stable-Baselines3
-   DQN

## Note

The deposition environment is a **synthetic simulation created for
reinforcement-learning experimentation**. Its process relationships are
simplified and are not intended to represent a production semiconductor
fabrication model.
