# Multi-Player 2D Turtle Racing & Betting Simulator

A modular, desktop event-driven application built in Python utilizing the standard `turtle` graphics engine. The system implements real-time animated simulation, dynamic state management for player persistent bankrolls and win streaks, strict input validation, and a non-blocking main execution loop.

---

## Technical Overview & Architecture

- **Event Loop & Rendering Engine:** Utilizes frame-buffer batching via `screen.tracer(0)` and explicit manual updates (`screen.update()`) to maintain a smooth frame rate and eliminate GUI flicker during runtime animation.
- **Dynamic Physics Simulation:** Implements a pseudo-random tick movement model using discrete interval steps (`random.randint`), generating non-deterministic race velocity for every competitor entity.
- **Persistent State Management:** Stores player balances, active wagers, and consecutive win streaks across iterative game sessions using nested dictionary data structures without memory leakage or state decay.
- **Input Sanitization & Boundary Logic:** Enforces bounds checking on player prompts to prevent buffer errors, invalid color inputs, or wager entries exceeding available account balances.

---

## Tech Stack & Dependencies

- **Language:** Python 3.10+
- **GUI & Graphics:** Python Standard Library `turtle`
- **Utility Modules:** `random`, `time`
- **Version Control:** Git / GitHub

---

## Getting Started

### Prerequisites

Ensure you have a modern Python 3 installation on your system. No external third-party dependencies or virtual environments are required.

### Installation & Execution

1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/turtle-2d-racing-game.git](https://github.com/yourusername/turtle-2d-racing-game.git)