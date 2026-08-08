<p align="center">
  <img src="images/image.png" alt="ActOS" width="180">
</p>


# ActOS

**AI-native operating system for robots.**

ActOS is a modular robotics runtime designed to give AI agents a unified way to perceive, reason, and act across different types of robots — robotic arms, quadrupeds, humanoids, wheeled robots, and more.

The goal is simple:

> **One AI layer. Any robot.**

## Architecture

```text
                    ┌──────────────────┐
                    │     AI AGENT     │
                    │    LLM / VLM     │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │     AI Actions   │
                    │  move / grasp /   │
                    │  navigate / etc. │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │   Action System  │
                    │     Action()     │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
           Vision         Motion         Hardware
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                           ROBOT
```

## Current Status

ActOS is currently in early development.

### Latest commit

```text
feature: added actions
```

The initial action system has been added and provides the foundation for allowing AI agents to interact with the robot through standardized actions.

### Currently working on

* Vision AI
* `ai_actions`
* `Action` class
* AI → Action execution pipeline

## Core Concept

Instead of allowing an LLM to directly control hardware:

```text
LLM → Servo
```

ActOS uses an abstraction layer:

```text
LLM
 ↓
AI Action
 ↓
Action
 ↓
Robot Capability
 ↓
Hardware
```

For example:

```python
AI → grasp("red cup")

        ↓

Action(
    name="grasp",
    target="red cup"
)

        ↓

Robot
```

This allows the AI layer to remain independent of the underlying robot.

## Vision

Vision AI will provide the perception layer required for the action system.

The intended pipeline is:

```text
Camera
  ↓
Vision AI
  ↓
Objects / Positions / State
  ↓
AI Actions
  ↓
Actions
  ↓
Robot
```

For example:

```text
Camera
 ↓
YOLO
 ↓
red cup @ (423, 281)
 ↓
AI
 ↓
grasp("red cup")
 ↓
Action
 ↓
Manipulator
```

## AI Actions

`ai_actions` will provide the interface between AI reasoning and ActOS actions.

Example concept:

```python
ai_action = {
    "action": "grasp",
    "target": "red_cup"
}
```

The action system can then translate this into the appropriate robot-specific implementation.

This means the AI does not need to know whether it is controlling:

* a robotic arm
* a quadruped
* a humanoid
* a wheeled robot
* another supported platform

It only needs to understand the available capabilities.

## Action System

The `Action` class is being developed as the core abstraction for executable robot behavior.

Conceptually:

```python
class Action:
    name
    parameters
    execute()
```

Actions should eventually support:

* execution
* validation
* status
* cancellation
* errors
* results
* asynchronous execution

## Design Goals

### Robot agnostic

ActOS should work across different robot morphologies.

### AI native

AI should be able to discover and use robot capabilities without directly interacting with hardware APIs.

### Modular

Vision, reasoning, actions, navigation, hardware drivers, and controllers should remain independent modules.

### Fast

LLMs should perform high-level reasoning while low-level control remains deterministic and real-time.

```text
LLM
 ↓
High-level decision

Action System
 ↓
Task execution

Controller
 ↓
Real-time control

Hardware
```

### Local-first

ActOS is intended to support local AI models and CPU-based inference, making it suitable for edge robotics.

## Roadmap

* [x] Initial project structure
* [x] Action system foundation
* [ ] `Action` class
* [ ] AI Actions
* [ ] Vision AI
* [ ] Object detection
* [ ] Action execution pipeline
* [ ] Robot capability system
* [ ] Hardware abstraction layer
* [ ] Async action execution
* [ ] Memory
* [ ] Navigation
* [ ] Multi-robot support
* [ ] LLM tool calling
* [ ] VLM integration

## Vision

The long-term goal of ActOS is to create a general-purpose **AI operating layer for physical robots**.

```text
              ┌─────────────────┐
              │      ActOS      │
              └────────┬────────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
        Vision        AI          Actions
          │            │            │
          └────────────┼────────────┘
                       │
                 Robot Abstraction
                       │
       ┌───────────────┼───────────────┐
       │               │               │
      ARM           QUADRUPED       HUMANOID
```

**ActOS — AI that can act in the physical world.**
