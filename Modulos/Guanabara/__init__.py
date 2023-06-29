
import tkinter as tk


class Game:
    def __init__(self):
        self.score = 0

        self.window = tk.Tk()
        self.window.title("Jogo do Clique")

        self.label_score = tk.Label(self.window, text="Pontuação: 0")
        self.label_score.pack(pady=10)

        self.button_click = tk.Button(
            self.window, text="Clique aqui!", command=self.increment_score)
        self.button_click.pack(pady=10)

    def increment_score(self):
        self.score += 1
        self.label_score.config(text="Pontuação: " + str(self.score))

    def start(self):
        self.window.mainloop()


game = Game()
game.start()
