import tkinter as tk
from tkinter import messagebox

class Ticktactoe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text=" ", font=("Arial,20"), width=5, height=2, command=lambda i=i, j=j: self.on_click(i, j))
                btn.grid(row=i, column=j)
        reset_btn = tk.Button(self.root, text="Reset", command=self.reset)
        reset_btn.grid(row=3, column=1)

    def on_click(self, i, j):
        index = i * 3 + j
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.update_button(i, j)
            if self.check_winner():
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                self.reset()
            elif " " not in self.board:
                messagebox.showinfo("Draw!", "It's a draw")
                self.reset()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def update_button(self, i, j):
        index = i * 3 + j
        btn_text = self.board[index]
        btn = self.root.grid_slaves(row=i, column=j)[0]
        btn.config(text=btn_text, state=tk.DISABLED)

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return True
        return False

    def reset(self):
        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                self.board[index] = " "
                btn = self.root.grid_slaves(row=i, column=j)[0]
                btn.config(text=" ", state=tk.NORMAL)
        self.current_player = "X"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = Ticktactoe()
    game.run()








