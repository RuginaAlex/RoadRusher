# 🛣️ Cross the Road Game

**Cross the Road** is a retro-inspired game where players navigate through a busy highway filled with fast-moving cars. The goal is to cross the road safely without colliding with any obstacles. This project was created using **Object-Oriented Programming (OOP)** principles to demonstrate modular and organized code structure, enhancing the gameplay experience.

---

## 🌟 Features
- 🎮 **Interactive gameplay**: Dodge oncoming cars as you move forward across multiple lanes.
- 🛤️ **Multiple lanes with alternating traffic directions**: Cars move in different directions on each lane, adding a realistic challenge.
- 🚀 **Dynamic level progression**: As you cross the highway, the level increases, speeding up the traffic.
- 🕹️ **Retro graphics and animations**: Simple graphics bring a nostalgic feel to the game.

## 📸 Screenshot
![Cross the Road Gameplay](https://github.com/RuginaAlex/RoadRusher/issues/1#issue-2646278503)  
*(Replace with a link to your screenshot)*

---

## 🚀 Getting Started
Follow these steps to set up and run the game locally.

### ✅ Prerequisites
- **Python** (version 3.x)
- **Turtle Graphics** (comes pre-installed with Python)

### 📥 Installation
1. **Clone the repository**: `git clone https://github.com/yourusername/CrossTheRoad.git`
2. **Navigate into the project directory**: `cd CrossTheRoad`
3. **Run the game**: `python main.py`

---

## 🎮 How to Play
1. **Objective**: Cross the road by avoiding the cars and reaching the finish line.
2. **Controls**:
   - ⬆️ `Up Arrow`: Move forward.
   - ⬇️ `Down Arrow`: Move backward.
3. **Gameplay**:
   - Wait for the "GO!" signal after the highway populates with cars.
   - Use the arrow keys to navigate and avoid obstacles.
   - Each successful crossing increases the level and the speed of traffic.

---

## 🛠️ Code Structure
This game was built using **Object-Oriented Programming (OOP)**, with each key element of the game represented as a separate class for modularity and scalability.
- **`Player` Class** (`player.py`): Controls player movement and position reset when leveling up.
- **`CarManager` Class** (`car_manager.py`): Manages car spawning, movement, and speed increment as levels progress.
- **`Scoreboard` Class** (`scoreboard.py`): Displays the level, game over message, and "GO!" start signal.
- **`BackgroundSetter` Class** (`background.py`): Creates and renders the road and grass lanes, as well as the striped lines for visual effect.

---

## 📚 Key Concepts Demonstrated
- **Object-Oriented Programming (OOP)**: Implemented core classes (`Player`, `CarManager`, `Scoreboard`, `BackgroundSetter`) to organize and modularize code.
- **Encapsulation**: Each class encapsulates specific functionalities and properties, promoting clean code.
- **Inheritance**: Inherited from Turtle class to leverage the `Turtle` graphics library for easy visualization.

---

## 🤝 Contributions
Contributions are welcome! If you find a bug or have an idea for improvement, feel free to open an issue or submit a pull request.

---

## 📜 License
This project is licensed under the MIT License.
