# Atomic Chess ♟️

A Python implementation of Atomic Chess, a variant of chess where captures trigger explosions. Built as a portfolio project for CS162 (Software Engineering II) at Oregon State University.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📋 Table of Contents

- [About](#about)
- [Features](#features)
- [Game Rules](#game-rules)
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Code Structure](#code-structure)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [Author](#author)

## 🎯 About

Atomic Chess is a chess variant where every capture triggers an explosion that destroys all pieces (except pawns) in the 8 surrounding squares. This implementation demonstrates object-oriented programming principles, game logic validation, and comprehensive testing practices.

**Key Learning Objectives:**
- Object-oriented design and encapsulation
- Complex game logic validation
- Unit testing with pytest
- Type hints for code clarity
- Algebraic notation parsing

## ✨ Features

- ✅ Full implementation of atomic chess rules
- ✅ Standard chess piece movement validation
- ✅ Atomic explosion mechanics on captures
- ✅ Turn-based gameplay management
- ✅ Game state tracking (win/loss detection)
- ✅ Algebraic notation support (e.g., 'e2' to 'e4')
- ✅ Board visualization
- ✅ Comprehensive unit test suite (pytest)
- ✅ Type hints for improved code maintainability

## 📖 Game Rules

### Starting Position
The game begins with the standard chess starting position:

![Starting Position](starting_position.png)

### Movement Rules
- Pieces move and capture like in standard chess
- **No check, checkmate, castling, en passant, or pawn promotion**
- Pawns can move two squares forward on their first move
- Game ends when a king is captured or blown up

### Special Atomic Chess Rules

1. **Explosions on Capture**: When a piece is captured, all pieces (except pawns) in the 8 surrounding squares are destroyed
2. **Capturing is Suicidal**: The capturing piece is also destroyed in the explosion
3. **Kings Cannot Capture**: Since capturing would blow up the king itself
4. **Pawns are Immune**: Pawns are not affected by explosions unless directly involved in the capture
5. **Cannot Blow Up Both Kings**: Moves that would destroy both kings simultaneously are not allowed

[Learn more about Atomic Chess](https://www.chess.com/terms/atomic-chess#captures-and-explosions)

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jogarbaut/OSU-CS162-portfolioproject-github.git
   cd OSU-CS162-portfolioproject-github
   ```

2. **Install dependencies** (for running tests)
   ```bash
   pip install pytest
   ```

## 💻 Usage

### Basic Example

```python
from ChessVar import ChessVar

# Create a new game
game = ChessVar()

# Make moves using algebraic notation
print(game.make_move('e2', 'e4'))  # True - White pawn moves forward
print(game.make_move('d7', 'd5'))  # True - Black pawn moves forward
print(game.make_move('e4', 'd5'))  # True - White pawn captures (triggers explosion!)

# Print the board
game.print_board()

# Check game state
print(game.get_game_state())  # 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON'
```

### Example Game Session

```python
game = ChessVar()

# Fool's Mate style game
game.make_move('f2', 'f3')  # White advances f-pawn
game.make_move('e7', 'e5')  # Black advances e-pawn
game.make_move('g2', 'g4')  # White advances g-pawn
game.make_move('d8', 'h4')  # Black queen attacks

game.print_board()
print(f"Game State: {game.get_game_state()}")
```

## 🧪 Running Tests

The project includes comprehensive unit tests covering all game mechanics.

### Run all tests
```bash
pytest test_chessvar.py -v
```

### Run specific test class
```bash
pytest test_chessvar.py::TestPawnMovement -v
```

### Run with coverage report
```bash
pytest test_chessvar.py --cov=ChessVar --cov-report=html
```

### Test Coverage

The test suite includes:
- ✅ Initialization and setup tests
- ✅ Piece movement validation (all 6 piece types)
- ✅ Atomic explosion mechanics
- ✅ Turn management
- ✅ Win condition detection
- ✅ Edge cases and boundary conditions
- ✅ Invalid move scenarios

## 📁 Code Structure

```
.
├── ChessVar.py           # Main game implementation
├── test_chessvar.py      # Comprehensive unit tests
├── README.md             # Project documentation
├── starting_position.png # Board diagram
└── CLAUDE.md             # Development guidelines
```

### Key Classes and Methods

**`ChessVar` Class**
- `__init__()` - Initialize game board and state
- `make_move(start_pos: str, end_pos: str) -> bool` - Execute a move
- `get_game_state() -> str` - Get current game state
- `is_valid_move(start: Tuple[int, int], end: Tuple[int, int]) -> bool` - Validate moves
- `explode(pos: Tuple[int, int]) -> None` - Handle explosion mechanics
- `kings_both_exist() -> bool` - Check win condition
- `print_board() -> None` - Display current board state
- `pos_to_indices(pos: str) -> Tuple[int, int]` - Convert algebraic notation

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **pytest** - Testing framework
- **Type Hints** - Static type checking for improved code quality
- **Git** - Version control

## 🔮 Future Enhancements

Potential features for future development:

- [ ] Interactive CLI interface for playing games
- [ ] Move history tracking and undo functionality
- [ ] Save/load game state (JSON serialization)
- [ ] AI opponent with minimax algorithm
- [ ] Move validation with detailed error messages
- [ ] PGN (Portable Game Notation) export
- [ ] Web interface using Flask or FastAPI
- [ ] Graphical UI with pygame or tkinter

## 👨‍💻 Author

**Jomel Bautista**
- GitHub: [@jogarbaut](https://github.com/jogarbaut)
- LinkedIn: [linkedin.com/in/jomelbautista](https://linkedin.com/in/jomelbautista)

## 📄 License

This project is licensed under the MIT License - see below for details.

---

## 🎓 Academic Context

This project was developed as a portfolio assignment for **CS162: Introduction to Computer Science II** at Oregon State University. The goal was to demonstrate proficiency in:
- Object-oriented programming
- Complex algorithm implementation
- Code documentation
- Software testing practices

---

**Note**: This is an educational project. Contributions and feedback are welcome!
