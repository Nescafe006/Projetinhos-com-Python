from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Application:
    def __init__(self, master=None):
        self.master = master
        self.fonte = ("Verdana", "8")


        self.container1 = Frame(master, pady=10)
        self.container1.pack()
        self.container2 = Frame(master, padx=20, pady=5)
        self.container2.pack()
        self.container3 = Frame(master, padx=20, pady=5)
        self.container3.pack()
        self.container4 = Frame(master, padx=20, pady=5)
        self.container4.pack()
        self.container5 = Frame(master, padx=20, pady=5)
        self.container5.pack()
        self.container6 = Frame(master, padx=20, pady=5)
        self.container6.pack()
        self.container7 = Frame(master, padx=20, pady=5)
        self.container7.pack()
        self.container8 = Frame(master, padx=20, pady=10)
        self.container8.pack()
        self.container9 = Frame(master, pady=15)
        self.container9.pack()


        self.titulo = Label(self.container1, text="Informe os dados :", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        self.lblidusuario = Label(self.container2, text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)
        self.txtidusuario = Entry(self.container2, width=10, font=self.fonte)
        self.txtidusuario.pack(side=LEFT)
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10, command=self.buscarUsuario)
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.container3, width=25, font=self.fonte)
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone = Entry(self.container4, width=25, font=self.fonte)
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        self.txtemail = Entry(self.container5, width=25, font=self.fonte)
        self.txtemail.pack(side=LEFT)

        self.lblusuario = Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)
        self.txtusuario = Entry(self.container6, width=25, font=self.fonte)
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.container7, width=25, show="*", font=self.fonte)
        self.txtsenha.pack(side=LEFT)

        # Buttons
        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12, command=self.inserirUsuario)
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12, command=self.alterarUsuario)
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12, command=self.excluirUsuario)
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack()

        self.treeview_frame = Frame(master)
        self.treeview_frame["padx"] = 100
        self.treeview_frame["pady"] = 100
        self.treeview_frame.pack()

        self.treeview = ttk.Treeview(self.treeview_frame, columns=("Nome", "Telefone", "E-mail", "Usuário", "Senha"),
                                     show="headings", selectmode="browse")

        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Telefone", text="Telefone")
        self.treeview.heading("E-mail", text="E-mail")
        self.treeview.heading("Usuário", text="Usuário")
        self.treeview.heading("Senha", text="Senha")

        self.treeview.pack()

    def inserirUsuario(self):
        nome = self.txtnome.get()
        telefone = self.txttelefone.get()
        email = self.txtemail.get()
        usuario = self.txtusuario.get()
        senha = self.txtsenha.get()

        if nome and telefone and email and usuario and senha:
            self.treeview.insert("", "end", values=(nome, telefone, email, usuario, senha))
            self.limparCampos()
            messagebox.showinfo("Sucesso", "Usuário inserido com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")

    def alterarUsuario(self):
        selected_item = self.treeview.selection()
        if selected_item:
            nome = self.txtnome.get()
            telefone = self.txttelefone.get()
            email = self.txtemail.get()
            usuario = self.txtusuario.get()
            senha = self.txtsenha.get()

            if nome and telefone and email and usuario and senha:
                self.treeview.item(selected_item, values=(nome, telefone, email, usuario, senha))
                self.limparCampos()
                messagebox.showinfo("Sucesso", "Usuário alterado com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
        else:
            messagebox.showwarning("Aviso", "Nenhum usuário selecionado para alterar!")

    def excluirUsuario(self):
        selected_item = self.treeview.selection()
        if selected_item:
            self.treeview.delete(selected_item)
            self.limparCampos()
            messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Nenhum usuário selecionado para excluir!")

    def buscarUsuario(self):
        idusuario = self.txtidusuario.get()
        if idusuario:

            for item in self.treeview.get_children():
                if self.treeview.item(item, 'values')[0] == idusuario:
                    nome, telefone, email, usuario, senha = self.treeview.item(item, 'values')[1:]
                    self.txtnome.delete(0, END)
                    self.txtnome.insert(INSERT, nome)
                    self.txttelefone.delete(0, END)
                    self.txttelefone.insert(INSERT, telefone)
                    self.txtemail.delete(0, END)
                    self.txtemail.insert(INSERT, email)
                    self.txtusuario.delete(0, END)
                    self.txtusuario.insert(INSERT, usuario)
                    self.txtsenha.delete(0, END)
                    self.txtsenha.insert(INSERT, senha)
                    messagebox.showinfo("Sucesso", "Usuário encontrado e dados carregados!")
                    return
            messagebox.showwarning("Não Encontrado", "Usuário não encontrado.")
        else:
            messagebox.showwarning("Aviso", "Nenhum ID de usuário fornecido!")

    def limparCampos(self):
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)
