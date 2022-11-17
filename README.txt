
HOW TO PLAY
-----------

Run "server.py" and "client.py" independently to begin.

You will first be prompted to enter the IP address of the server you wish to connect to.

If the IP address provided is invalid/fails to connect, the program will tell you so, 
and entering "Y" or "y" will allow you to re-enter the address.
Entering anything else will terminate the program.

Once connected, you will be prompted to choose from one of three difficulties: Easy, medium, and hard.
    Entering "1" will set the difficulty to easy.
    Entering "2" will set the difficulty to medium.
    Entering "3" will set the difficulty to hard.

After entering the difficulty, the tic-tac-toe board will be displayed, and you will be prompted to enter a move.
A move input is an integer in range 1-9 corresponding to the chosen position, layed out as follows:

     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9

If an invalid move is entered, or the chosen position is already occupied, you will be re-prompted to enter a move.

The tic-tac-toe board will then be displayed with your updated move on it.
The program will then pause momentarily while the computer chooses its move.
After the computer chooses its move, the board will be re-displayed and you will again be prompted to enter a move.

This continues until a game-ending board state occurs (win, loss, tie).

Once the game ends, you will be prompted whether or not you wish to play again,
and entering "Y" or "y" will allow you to play again without having to re-enter the IP address.
Entering anything else will terminate the program.


PROTOCOL
--------

Once the server accepts a connection from the client, it will await a message of either "E", "M", or "H"
from the client, corresponding to each difficulty level.

This will then prompt the server to send a string containing the visual display of the tic-tac-toe board.
The client prints out the board automatically once received and immediately awaits another message.

Each time the server sends the client a string containing the tic-tac-toe board,
it will then send a length-1 string status message, corresponding to the state of the game:

    "M" - The server is awaiting a player's input. This prompts the client to prompt the player to enter a move.
    "B" - The player's previous input was invalid (position already taken), indicating the request of another input.
    "A" - The computer is choosing a move.
        This prompts the client to tell the player that the server is choosing its move and await another message.
    "P", "T", "C" - Correspond to player victory, tie, and computer victory respectively.
        This prompts the client to stop receiving status messages.

Each time the client receives a message of "M" or "B", the player is then prompted to input their move.
This move is then sent to the server in a message string containing the single digit of the player's chosen position.
The server then updates the tic-tac-toe object by performing the player's move for them given their chosen position.

Each time the player's/computer's move is registered on the tic-tac-toe object, a check is done to see if the game has
ended, in which case the server will send a game-ending status message ("P", "T", or "C") to the client
and close the connection. This notifies the client to tell the player that the game has ended and prompt the player
whether they would like to play again, in which case the client will reconnect to the server using the
previously-provided IP address.


COMPUTER DIFFICULTY
-------------------

The computer has 3 difficulty options: Easy, medium, and hard.

Easy difficulty directs the computer to simply choose a randomly open spot on the board.

The medium difficulty directs the computer to choose its move as follows:

    If the computer can win this turn, choose the winning position.
    If not, and the player can win in their next turn, block their winning position.
    Otherwise, choose a random position.

Finally, the hard difficulty follows an optimal 8-step tic-tac-toe algorithm, making it impossible to beat:

    1. If the computer can win this turn, choose the winning position.
    2. If the player can win in their next turn, block their winning position.
    3. If possible, play a position creating a "fork", where you can win in more than one position on your next turn.
    4. If the player can create a fork in their next turn, block the position needed to create the fork.
    5. If the center is open, choose the center.
    6. If the player occupies a corner, choose the opposite corner if possible.
    7. Choose an empty corner if possible.
    8. Choose an empty side.
