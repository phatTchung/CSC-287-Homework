import * as readline from "readline";

// this is for reading input from the terminal
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

// small helper to ask a question and wait for the answer
function ask(question: string): Promise<string> {
    return new Promise((resolve) => {
        rl.question(question, (answer) => {
            resolve(answer);
        });
    });
}

function printBoard(board: string[][]): void {
    /**
     * Show the tic-tac-toe board on the screen.
     */
    for (const row of board) {
        console.log(row.join(" | "));
    }
    console.log();
}

function checkWinner(board: string[][], player: string): boolean {
    /**
     * Check if the given player (X or O) has won.
     * Returns true if they win, false if not.
     */

    // check rows
    for (const row of board) {
        if (row.every((cell) => cell === player)) {
            return true;
        }
    }

    // check columns
    for (let col = 0; col < 3; col++) {
        let win = true;
        for (let row = 0; row < 3; row++) {
            if (board[row][col] !== player) {
                win = false;
                break;
            }
        }
        if (win) {
            return true;
        }
    }

    // check diagonals
    let diag1Win = true;
    let diag2Win = true;

    for (let i = 0; i < 3; i++) {
        if (board[i][i] !== player) {
            diag1Win = false;
        }
        if (board[i][2 - i] !== player) {
            diag2Win = false;
        }
    }

    if (diag1Win || diag2Win) {
        return true;
    }

    return false;
}

async function playGame(): Promise<void> {
    /**
     * Run one game of tic-tac-toe for two players.
     * Handles moves, checks winner, and checks draw.
     */

    // 2D board (array of arrays)
    let board: string[][] = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ];

    let currentPlayer: string = "X";

    while (true) {
        printBoard(board);
        const moveStr = await ask(`Your move, ${currentPlayer} (1–9): `);

        const moveNum = Number(moveStr);

        if (!Number.isInteger(moveNum) || moveNum < 1 || moveNum > 9) {
            console.log("Invalid move! Pick 1–9.");
            continue;
        }

        const num = moveNum - 1;
        const row = Math.floor(num / 3);
        const col = num % 3;

        if (board[row][col] === "X" || board[row][col] === "O") {
            console.log("Spot already taken!");
            continue;
        }

        board[row][col] = currentPlayer;

        // winner?
        if (checkWinner(board, currentPlayer)) {
            printBoard(board);
            console.log(`${currentPlayer} is the winner!`);
            break;
        }

        // draw?
        const isDraw = board.every((r) =>
            r.every((cell) => cell === "X" || cell === "O")
        );

        if (isDraw) {
            printBoard(board);
            console.log("It's a draw!");
            break;
        }

        // switch turn
        currentPlayer = currentPlayer === "X" ? "O" : "X";
    }
}

async function main() {
    while (true) {
        await playGame();
        const again = (await ask("Play again? (yes/no): ")).toLowerCase();

        if (again !== "yes") {
            console.log("Goodbye!");
            break;
        }
    }

    rl.close();
}

main();
