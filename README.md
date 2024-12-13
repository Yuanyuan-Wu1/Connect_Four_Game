# Connect Four Game

An intelligent Connect Four game developed with Processing Python Mode, featuring AI opponents with multiple difficulty levels.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [AI Implementation](#ai-implementation)
- [Future Enhancements](#future-enhancements)
- [Testing](#testing)
- [Contributing](#contributing)

## Overview

Connect Four is a classic two-player game where players take turns dropping colored disks into a vertical grid. The objective is to connect four disks of the same color vertically, horizontally, or diagonally. This implementation features an AI opponent using the Minimax algorithm with Alpha-Beta pruning.

## Features

- Player vs AI gameplay
- Multiple AI difficulty levels
- Score tracking system
- Interactive graphical interface
- Real-time game state display
- Automated AI decision making

## Project Structure
connect_four/
├── connect_four.pyde # Main game entry point
├── board.py # Board class and grid management
├── disk.py # Disk class for game pieces
├── game_controller.py # Game state and flow control
├── ai_player.py # AI logic implementation
├── ai_learning.py # AI learning capabilities
└── scores.txt # Score recording

### Component Descriptions

- **connect_four.pyde**: Main game loop and Processing setup
- **board.py**: Manages the game grid and piece placement
- **game_controller.py**: Controls game flow and win conditions
- **ai_player.py**: Implements AI decision-making algorithms

## Installation

### Prerequisites
1. Processing 4.0 or higher
2. Python Mode for Processing
3. Python 3.6+

### Setup Steps
1. Install Processing from [processing.org](https://processing.org/download)
2. Add Python Mode in Processing
3. Clone this repository
4. Open `connect_four.pyde` in Processing
5. Click the Run button

## How to Play

1. Start the game
2. Enter your name when prompted
3. Click on a column to drop your disk
4. Try to connect four disks while preventing AI from doing the same
5. Game ends when either player wins or board is full

### Controls
- Mouse click: Drop disk in selected column
- Click anywhere after game over to restart

## AI Implementation

### Difficulty Levels
- **Easy**: Random moves
- **Medium**: 3-depth Minimax search
- **Hard**: 5-depth Minimax with Alpha-Beta pruning

### AI Strategies
python
def evaluate_position(self, board):
"""Evaluates current board position"""
score = 0
# Horizontal evaluation
for row in range(self.height):
for col in range(self.width - 3):
window = [board.grid[row][col+i] for i in range(4)]
score += self.evaluate_window(window)
# Vertical evaluation
for row in range(self.height - 3):
for col in range(self.width):
window = [board.grid[row+i][col] for i in range(4)]
score += self.evaluate_window(window)
return score
:

### Key AI Features
1. Position evaluation
2. Threat detection
3. Win-move recognition
4. Pattern-based learning

## Future Enhancements

### AI Improvements
- [ ] Implement deep learning model
- [ ] Add opening book
- [ ] Optimize evaluation function
- [ ] Add parallel computing

### Feature Additions
- [ ] Online multiplayer
- [ ] Leaderboard system
- [ ] Game replay functionality
- [ ] Save/Load games

### Performance Optimization
- [ ] Implement caching mechanism
- [ ] Optimize data structures
- [ ] Improve search algorithms
- [ ] Add concurrent processing

## Testing

Run tests using:
```bash
python -m pytest board_test.py
python -m pytest game_controller_test.py
```

### Test Coverage
- Board functionality
- Game controller logic
- AI decision making
- Win condition detection

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

### Code Style
- Follow PEP 8 guidelines
- Add docstrings for new functions
- Include unit tests for new features

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Processing Foundation for the Processing development environment
- Python Mode developers
- Connect Four game concept creators

## Contact

For questions or suggestions, please open an issue in the repository.
