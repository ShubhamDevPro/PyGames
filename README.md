# PyGames

A simple snake game implemented in both PyGame and as a web application using Flask.

## Files

- `main.py` - Original PyGame version of the snake game
- `app.py` - Flask web application server
- `templates/index.html` - Web version with features like score, food, and game controls

## Running the Original PyGame Version

Make sure you have pygame installed:
```bash
pip install pygame
```

Then run:
```bash
python main.py
```

## Running the Web Version

1. Install Flask:
```bash
pip install -r requirements.txt
```

2. Start the Flask server:
```bash
python app.py
```

3. Open your browser and navigate to:
   - `http://localhost:5006/` - Snake game with score and food collection

## Controls

- **Arrow Keys**: Move the snake/square
- **WASD Keys**: Alternative movement controls (web version)
- **Space**: Pause/Resume (web version only)

## Features

### Original PyGame Version
- Basic snake movement with arrow keys
- Black square on white background
- 30 FPS game loop

### Web Version
- Score system with food collection
- Game start/pause/reset controls
- Visual improvements and responsive design
- Arrow key controls for snake movement