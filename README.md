# portfolio-project

**Remember that this project cannot be submitted late.**

Write a class named **ChessVar** for playing an abstract board game that is a variant of chess--atomic chess. The following explanation of the rules assumes some familiarity with the rules of chess - specifically how the pieces move and capture. If you have any questions about those rules, please don't hesitate to ask.

The starting position for the game is the normal starting position for standard chess. You will need to keep track of which player's turn it is. As in standard chess, white moves first. Pieces move and capture the same as in standard chess, except that **there is no check or checkmate, and there is no castling, en passant, or pawn promotion**. As in standard chess, each pawn should be able to move two spaces forward on its first move (but not on subsequent moves). 

If a player's king is captured or blown up, the game ends, and that player loses. 

Locations on the board will be specified using "algebraic notation", with columns labeled a-h and rows labeled 1-8, as shown in this diagram:

![board](starting_position.png "starting position")

<<<<<<< Updated upstream
Special rules for this variant of chess:
=======
**Key Learning Objectives:**

- Object-oriented design and encapsulation
- Complex game logic validation
- Unit testing with pytest
- Type hints for code clarity
- Algebraic notation parsing
>>>>>>> Stashed changes

In Atomic Chess, whenever a piece is captured, an "explosion" occurs at the 8 squares immediately surrounding the captured piece in all the directions. This explosion kills all of the pieces in its range except for **pawns**. Different from regular chess, where only the captured piece is taken off the board, in Atomic Chess, every capture is suicidal. Even the capturing piece is affected by the explosion and must be taken off the board. As a result, a pawn can only be removed from the board when directly involved in a capture. If that is the case, both capturing and captured pawns must be removed from the board. Because every capture causes an explosion that affects not only the victim but also the capturing piece itself, **the king is not allowed to make captures**. Also, a player **cannot blow up both kings at the same time**. In other words, the move that would kill both kings in one step is not allowed. Blowing up a king has the same effect as capturing it, which will end the game.
[(https://www.chess.com/terms/atomic-chess#captures-and-explosions)](https://www.chess.com/terms/atomic-chess#captures-and-explosions)

Your ChessVar class must include the following:
* An **init method** that initializes any data members
* A method called **get_game_state** that just returns 'UNFINISHED', 'WHITE_WON', 'BLACK_WON'. 
* A method called **make_move** that takes two parameters - strings that represent the square moved from and the square moved to.  For example, make_move('b2', 'b4').  If the square being moved from does not contain a piece belonging to the player whose turn it is, or if the indicated move is not allowed, or if the game has already been won, then it should **just return False**.  Otherwise it should make the indicated move, remove any captured (explosion) pieces from the board, update the game state (unfinished to who wins) if necessary, update whose turn it is, and return True.

You need to implement a method called **print_board** that outputs the current state of the board. This will be extremely helpful for testing. You can choose any format for displaying the board, provided it is legible to others. If you're uncertain about the acceptability of your format, ask it on the discussion board.

<<<<<<< Updated upstream
Feel free to add whatever other classes, methods, or data members you want.  All data members of a class must be private.  Every class should have an init method that initializes all of the data members for that class.

Here's a very simple example of how the class could be used:
```
=======
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
>>>>>>> Stashed changes
game = ChessVar()
print(game.make_move('d2', 'd4'))  # output True
print(game.make_move('g7', 'g5'))  # output True
print(game.make_move('c1', 'g5'))  # output True
game.print_board()
print(game.get_game_state())  # output UNFINISHED
```
<<<<<<< Updated upstream
The file must be named: ChessVar.py
=======

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
>>>>>>> Stashed changes
