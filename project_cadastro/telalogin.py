from tkinter import *
from tkinter import messagebox
import AppCidades
import AppClientes
import Appusuarios


class Login:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Login")
        self.master.geometry("600x600")
        self.master.resizable(False, False)

        self.fonte = ("Arial", "12")


        self.container = Frame(master)
        self.container["padx"] = 20
        self.container["pady"] = 20
        self.container.pack(padx=10, pady=10)


        self.titulo = Label(self.container, text="Login", font=("Arial", "24", "bold"))
        self.titulo.pack(pady=10)


        self.lblEmail = Label(self.container, text="E-mail ou telefone:", font=self.fonte)
        self.lblEmail.pack(anchor=W)
        self.txtEmail = Entry(self.container, font=self.fonte, width=40)
        self.txtEmail.pack(pady=5)


        self.lblPassword = Label(self.container, text="Senha:", font=self.fonte)
        self.lblPassword.pack(anchor=W, pady=(10, 0))
        self.txtPassword = Entry(self.container, show="*", font=self.fonte, width=40)
        self.txtPassword.pack(pady=5)


        self.btnLogin = Button(self.container, text="Entrar", font=self.fonte, command=self.login, width=20, bg="#1877F2", fg="white")
        self.btnLogin.pack(pady=20)


        self.forgot_password_link = Label(self.container, text="Esqueceu a senha?", font=self.fonte, fg="#1877F2")
        self.forgot_password_link.pack(pady=5)

        self.create_account_link = Label(self.container, text="Criar nova conta", font=self.fonte, fg="#1877F2")
        self.create_account_link.pack(pady=5)

    def login(self):

        email = self.txtEmail.get()
        password = self.txtPassword.get()

        if email and password:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.master.destroy()
            self.open_menu()
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")

    def open_menu(self):
        menu_window = Tk()
        Menu(menu_window)
        menu_window.mainloop()
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
                                  command=self.show_Cidades)
        self.city_button.pack(pady=5)

        self.client_button = Button(self.button_frame, text="Clientes", font=("Helvetica", 12), width=25,
                                    command=self.show_Clientes)
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
            self.master.withdraw()
            top.protocol("WM_DELETE_WINDOW", self.on_closing)

        def on_closing(self):
            self.master.deiconify()

root = Tk()
app = Login(master=root)
root.mainloop()
