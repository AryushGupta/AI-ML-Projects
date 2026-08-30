# Reinforcement Learning

Reinforcement Learning (RL) is a type of Machine Learning where an **agent learns by interacting with an environment** and receiving **rewards or penalties**.

Instead of being told exactly what to do, the agent **tries actions, sees what happens, and learns from the experience**.

## Simple Example 🐕

Imagine teaching a dog to sit:

- 🐕 **Agent:** Dog
- 🌍 **Environment:** Surroundings
- 🏃 **Action:** Sit
- ⭐ **Reward:** Give a treat when it sits correctly
- ❌ **Penalty:** No treat when it does not

After many attempts, the dog learns:

> "If I sit when asked → I get a reward."

This is the basic idea of Reinforcement Learning.

## Another Example: Game 🎮

Imagine an AI playing a game.

```text
        AI Player
           ↓
        Takes Action
           ↓
       Game Changes
           ↓
      Gets Reward
           ↓
      Learns from it
           ↓
     Takes Better Action
```

For example:

- 🪙 Collect coin → **+10 reward**
- 💥 Hit obstacle → **-10 reward**
- 🏆 Finish level → **+100 reward**

The AI gradually learns which actions give better results.

## Important RL Terms

| Term | Simple Meaning |
|---|---|
| **Agent** | The learner/decision maker |
| **Environment** | The world the agent interacts with |
| **State** | Current situation |
| **Action** | What the agent can do |
| **Reward** | Feedback for an action |
| **Policy** | Strategy used to choose actions |

## RL vs Normal Machine Learning

### Supervised Learning

> "Here is the correct answer. Learn from it."

### Reinforcement Learning

> "Try something. I'll tell you whether it was good or bad."

So, the main goal of RL is:

> **Learn a strategy that maximizes the total reward over time.**

## Real-World Examples

- 🤖 Robots learning to walk
- 🚗 Self-driving systems making decisions
- 🎮 AI playing games
- 💰 Trading systems making decisions
- ⚡ Optimizing industrial processes

## In One Sentence

> **Reinforcement Learning is learning through trial, error, and rewards.**
