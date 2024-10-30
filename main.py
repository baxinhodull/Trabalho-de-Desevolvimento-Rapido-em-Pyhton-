import tkinter as tk
from ui import tela_de_login
from database import initialize_db

if __name__ == "__main__":
    initialize_db()
    tela_de_login()