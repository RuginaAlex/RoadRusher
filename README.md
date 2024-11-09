# 🛣️ Cross the Road Game

**Cross the Road** is a retro-inspired game where players navigate through a busy highway filled with fast-moving cars. The goal is to cross the road safely without colliding with any obstacles. This project was created using **Object-Oriented Programming (OOP)** principles to demonstrate modular and organized code structure, enhancing the gameplay experience.

---

## 🌟 Features
- 🎮 **Interactive gameplay**: Dodge oncoming cars as you move forward across multiple lanes.
- 🛤️ **Multiple lanes with alternating traffic directions**: Cars move in different directions on each lane, adding a realistic challenge.
- 🚀 **Dynamic level progression**: As you cross the highway, the level increases, speeding up the traffic.
- 🕹️ **Retro graphics and animations**: Simple graphics bring a nostalgic feel to the game.

## 📸 Screenshot
![Cross the Road Gameplay]([link_to_your_screenshot.png](https://private-user-images.githubusercontent.com/91621520/384624801-7e29c97e-3864-4508-aae5-08977663a740.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzExNzA2MDgsIm5iZiI6MTczMTE3MDMwOCwicGF0aCI6Ii85MTYyMTUyMC8zODQ2MjQ4MDEtN2UyOWM5N2UtMzg2NC00NTA4LWFhZTUtMDg5Nzc2NjNhNzQwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMDklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTA5VDE2MzgyOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWE3OWUxYzU3NTg4NWYzMjgxNDc2MGRhMWEyZThlNzFkMDRkYWIyMmU3ZGY0MTMwOWRjMmNlOTllYzIxYjhjMjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.fgJM5DYgAu_D-4a_Wo9T1oWI49YApRsCQd9Ls0_to_E))  
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
