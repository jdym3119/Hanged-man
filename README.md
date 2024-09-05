# hanged man
### Figure:
This is a classic game where you have to guess a hidden word letter by letter before the hangman drawing is completed.
Next I will show you the structure of the code.
```python
import random
class HangedMan:
    def __init__(self, words:list):
        self.words=words
        self.secret_word=random.choice(words).lower()
        self.guessed_letters=set()
        self.attempt=7
        self.word=["_"]*len(self.secret_word)
    def getter_attempts(self):
        return self.attempt
    def getter_word(self):
        return self.word
    def show_secret_word(self):
        return self.secret_word
    def show_words(self):
        return self.words
    def guess_letter(self, letter):
        letter=letter.lower()
        if letter in self.secret_word:
            self.guessed_letters.add(letter)
            for i in range(len(self.secret_word)):
                if self.secret_word[i] == letter:
                    self.word[i] = letter
        else:
            self.attempt-=1
        return letter in self.secret_word
    def win(self):
        return self.attempt >0 and set(self.secret_word).issubset(self.word)
    def lose(self):
        return self.attempt == 0 and not self.win()
```
This is the GUI or knows as Graphic User Interface.
```python
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from hanged import HangedMan

def display():
    tittle_label.config(text="Hanged Man")
    word_label.config(text=game.getter_word())
    attempts_label.config(text=f"Attempts left: {game.getter_attempts()}")
    image_label.config(text=get_image(game.getter_attempts()))
def guess():
    letter=letter_entry.get()
    if len(letter) == 1:
        if game.guess_letter(letter):
            display()
            if game.win()==True:
                messagebox.showinfo("Hanged Man","You win!")
                reset_game()
        else:
            display()
            if game.lose()==True:
                messagebox.showinfo("Hanged Man","Game over!")
                reset_game()
    else:
        messagebox.showwarning("Invalid input","Please choose a single letter.")
    letter_entry.delete(0, tk.END)
def reset_game():
    global game
    game=HangedMan(words)
    display()
def get_image(attempt):
    return IMAGES[7-attempt]
words=[
    "abandonar", "abogado", "absoluto", "acceso", "actividad", "admirar", "afirmar", "agregar",
    "agujero", "alegria", "alumno", "analisis", "aprender", "aroma", "asombro", "atencion",
    "aventura", "bajo", "balon", "batalla", "beneficio", "biologia", "borrador", "calidad",
    "camara", "capital", "carrera", "cavidad", "celebrar", "ciudad", "colores", "cometa",
    "compania", "computadora", "corazon", "cultura", "deporte", "escribir", "espacio", "familia",
    "felicidad", "futuro", "galaxia", "guitarra", "heroe", "historia", "hoja", "hospital",
    "imaginacion", "increible", "instrumento", "jardin", "jugar", "juventud", "libro", "luces",
    "misterio", "musica", "nacion", "natural", "oceano", "ordenador", "palabra", "pintura",
    "plantear", "plastico", "pueblo", "quimica", "raiz", "risa", "salud", "sabiduria",
    "sorpresa", "teatro", "temor", "universo", "vacaciones", "viento", "volar", "vuelta",
    "zapato", "zoologia", "cierto", "coche", "despertar", "doble", "docil", "esfuerzo",
    "futbol", "generar", "granada", "horizonte", "humano", "iman", "insecto", "lluvia",
    "medalla", "misterio", "nuevo", "octubre", "parrafo", "quedar", "rastro", "solucion",
    "subir", "tormenta", "tristeza", "ventana", "yogur", "zapato"
]

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']
game=HangedMan(words)
root=tk.Tk()
width = 600
height = 800
root.geometry(f"{width}x{height}")

root.title("Hanged Man")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")

root.configure(background="#11c9c4")
tittle_label=tk.Label(root,text="Hanged Man",font=("Arial",30),bg="#11c9c4")
tittle_label.pack(pady=40, anchor="center")
word_label=tk.Label(root,text=game.getter_word(),font=("Arial",20),bg="#9ef7f5")
word_label.pack(pady=20, anchor="center")
attempts_label=tk.Label(root,text=f"Attempts left: {game.getter_attempts()}",font=("Arial",16),bg="#11c9c4")
attempts_label.pack(pady=10, anchor="center")
image_label=tk.Label(root,text=get_image(game.getter_attempts()),bg="#9ef7f5",font=("Arial",20))
image_label.pack(pady=20, anchor="center")
letter_entry=tk.Entry(root,font=("Arial",16))
letter_entry.pack(pady=20, anchor="center")
guess_button=tk.Button(root,text="Guess",command=guess,font=("Arial",16),bg="#2a7e7c")
guess_button.pack(pady=10, anchor="center")
reset_button=tk.Button(root,text="Reset",command=reset_game,font=("Arial",16),bg="#2a7e7c")
reset_button.pack(pady=10, anchor="center")
root.mainloop()
```
I've chosen this text for creating the images for simplicity because I couldn't find images of the game Hangman on the web. The texts that simulate the images can be found at: (https://gist.github.com/kevin-lozoya/4b7903e5b4eecec25530467b7844e4fb).
Thanks for watching, I hope you found it to your liking.
