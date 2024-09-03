from tkinter import *
import AppCidades
import AppClientes
import Appusuarios

class Menu:
    def __init__(self, master):
        self.master = master
        master.title("Menu Principal")
        master.geometry("600x600")
        master.resizable(False, False)


        self.title_frame = Frame(master)
        self.title_label = Label(self.title_frame, text="MENU", font=("Arial", 18))
        self.title_frame.pack(pady=10)
        self.title_label.pack()


        self.button_frame = Frame(master)

        self.user_button = Button(self.button_frame, text="Usuários", font=("Helvetica", 12), width=25,
                                  command=self.show_usuarios)
        self.user_button.pack(pady=5)

        self.city_button = Button(self.button_frame, text="Cidades", font=("Helvetica", 12), width=25,
                                  command=self.show_cidades)
        self.city_button.pack(pady=5)

        self.client_button = Button(self.button_frame, text="Clientes", font=("Helvetica", 12), width=25,
                                    command=self.show_clientes)
        self.client_button.pack(pady=5)

        self.button_frame.pack(pady=10)

    def show_usuarios(self):
        self.open_window(Appusuarios.Application)

    def show_cidades(self):
        self.open_window(AppCidades.Application)

    def show_clientes(self):
        self.open_window(AppClientes.Application)

    def open_window(self, app_class):
        top = Toplevel(self.master)
        top.title(app_class.__name__)
        app_class(top)



