from tkinter import *
from tkinter import messagebox


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


        self.user_data = {
            "joao@example.com": "123",
            "admin@example.com": "adminpass"
        }

    def login(self):
        email = self.txtEmail.get()
        password = self.txtPassword.get()

        if email in self.user_data and self.user_data[email] == password:
            self.master.withdraw()
            self.show_menu()
        else:
            messagebox.showwarning("Aviso", "Email ou senha incorretos!")

root = Tk()
app = Login(master=root)
root.mainloop()

