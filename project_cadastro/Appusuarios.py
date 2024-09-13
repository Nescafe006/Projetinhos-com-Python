from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from usuarios import usuarios


class cadastro:
    def __init__(self, master=None):
        self.master = master
        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack(pady=20)

        self.container = Frame(master)
        self.container.pack(pady=5, padx=20)

        self.segundoContainer = Frame(master)
        self.segundoContainer.pack(pady=5, padx=20)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack(pady=5, padx=20)

        self.quartoContainer = Frame(master)
        self.quartoContainer.pack(pady=5, padx=20)

        self.quintoContainer = Frame(master)
        self.quintoContainer.pack(pady=5, padx=20)

        self.sextoContainer = Frame(master)
        self.sextoContainer.pack(pady=5, padx=20)

        self.setimoContainer = Frame(master)
        self.setimoContainer.pack(pady=10, padx=20)

        self.cad = Label(self.primeiroContainer, text="Cadastro de Usuarios")
        self.cad.pack()

        self.buscarID = Label(self.container, text="Buscar ID:", font=self.fontePadrao)
        self.buscarID.pack(side=LEFT)
        self.entID = Entry(self.container)
        self.entID["width"] = 5
        self.entID.pack(side=LEFT)

        self.botaoID = Button(self.container, text="Buscar")
        self.botaoID["command"] = self.buscarUsuario
        self.botaoID.pack(padx=5)

        self.txtNome = Label(self.segundoContainer, text="Nome: ", font=self.fontePadrao, width=10)
        self.txtNome.pack(side=LEFT)
        self.entNome = Entry(self.segundoContainer)
        self.entNome["width"] = 25
        self.entNome.pack(side=LEFT)

        self.txtTelefone = Label(self.terceiroContainer, text="Telefone:", font=self.fontePadrao, width=10)
        self.txtTelefone.pack(side=LEFT)
        self.entTelefone = Entry(self.terceiroContainer)
        self.entTelefone["width"] = 25
        self.entTelefone.pack()

        self.txtEmail = Label(self.quartoContainer, text="Email:", font=self.fontePadrao, width=10)
        self.txtEmail.pack(side=LEFT)
        self.entEmail = Entry(self.quartoContainer)
        self.entEmail["width"] = 25
        self.entEmail.pack()

        self.txtUsuario = Label(self.quintoContainer, text="Usuario: ", font=self.fontePadrao, width=10)
        self.txtUsuario.pack(side=LEFT)
        self.entUsuario = Entry(self.quintoContainer)
        self.entUsuario["width"] = 25
        self.entUsuario.pack()

        self.txtSenha = Label(self.sextoContainer, text="Senha: ", font=self.fontePadrao, width=10)
        self.txtSenha.pack(side=LEFT)
        self.entSenha = Entry(self.sextoContainer)
        self.entSenha["width"] = 25
        self.entSenha["show"] = "*"
        self.entSenha.pack()

        self.botInsert = Button(self.setimoContainer, text="Inserir", width=12)
        self.botInsert["command"] = self.inserirUsuario
        self.botInsert.pack(side=LEFT)

        self.botAlterar = Button(self.setimoContainer, text="Alterar", width=12)
        self.botAlterar["command"] = self.alterarUsuario
        self.botAlterar.pack(side=LEFT)

        self.botExcluir = Button(self.setimoContainer, text="Excluir", width=12)
        self.botExcluir["command"] = self.excluirUsuario
        self.botExcluir.pack(side=LEFT)

        self.botLimpar = Button(self.setimoContainer, text="Limpar", width=12)
        self.botLimpar["command"] = self.limpar
        self.botLimpar.pack(side=LEFT)

        self.botPdf = Button(self.setimoContainer, text="PDF", width=12, command=self.criarPdf)
        self.botPdf.pack(side=LEFT)

        self.tree = self.createTreeView(master)

    def limpar(self):

        if self.entID.get() or self.entNome.get() or self.entTelefone.get() or self.entEmail.get() or self.entUsuario.get() or self.entSenha.get():
            self.entID.delete(0, END)
            self.entNome.delete(0, END)
            self.entTelefone.delete(0, END)
            self.entEmail.delete(0, END)
            self.entUsuario.delete(0, END)
            self.entSenha.delete(0, END)
            messagebox.showinfo("", "Campos limpos")

    def inserirUsuario(self):
        user = usuarios()

        if self.entNome.get() and self.entTelefone.get() and self.entEmail.get() and self.entUsuario.get() and self.entSenha.get():

            user.nome = self.entNome.get()
            user.telefone = self.entTelefone.get()
            user.email = self.entEmail.get()
            user.usuario = self.entUsuario.get()
            user.senha = self.entSenha.get()

            self.entID.delete(0, END)
            self.entNome.delete(0, END)
            self.entTelefone.delete(0, END)
            self.entEmail.delete(0, END)
            self.entUsuario.delete(0, END)
            self.entSenha.delete(0, END)

            result = user.insertUser()
            messagebox.showinfo("Inserir", result)
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos")

        self.atualizarTreeView()

    def alterarUsuario(self):
        user = usuarios()

        if self.entID.get() and self.entNome.get() and self.entTelefone.get() and self.entEmail.get() and self.entUsuario.get() and self.entSenha.get():
            user.id = self.entID.get()
            user.nome = self.entNome.get()
            user.telefone = self.entTelefone.get()
            user.email = self.entEmail.get()
            user.usuario = self.entUsuario.get()
            user.senha = self.entSenha.get()

            self.entID.delete(0, END)
            self.entNome.delete(0, END)
            self.entTelefone.delete(0, END)
            self.entEmail.delete(0, END)
            self.entUsuario.delete(0, END)
            self.entSenha.delete(0, END)

            result = user.updateUser()
            messagebox.showinfo("Alterar", result)
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos")

        self.atualizarTreeView()

    def excluirUsuario(self):
        user = usuarios()

        user.id = self.entID.get()

        if self.entID.get():
            result = user.deleteUser()
            messagebox.showinfo("Excluir", result)

            self.entID.delete(0, END)
            self.entNome.delete(0, END)
            self.entTelefone.delete(0, END)
            self.entEmail.delete(0, END)
            self.entUsuario.delete(0, END)
            self.entSenha.delete(0, END)
        else:
            messagebox.showwarning("Aviso", "Selecione um ID para a exclusão")

        self.atualizarTreeView()

    def buscarUsuario(self):
        user = usuarios()

        user.id = self.entID.get()

        if self.entID.get():
            result = user.selectUser()
            messagebox.showinfo("Busca", result)

            self.entID.delete(0, END)
            self.entID.insert(INSERT, user.id)

            self.entNome.delete(0, END)
            self.entNome.insert(INSERT, user.nome)

            self.entTelefone.delete(0, END)
            self.entTelefone.insert(INSERT, user.telefone)

            self.entEmail.delete(0, END)
            self.entEmail.insert(INSERT, user.email)

            self.entUsuario.delete(0, END)
            self.entUsuario.insert(INSERT, user.usuario)

            self.entSenha.delete(0, END)
            self.entSenha.insert(INSERT, user.senha)
        else:
            messagebox.showwarning("Aviso", "Selecione um ID para a busca")

    def criarPdf(self):
        user = usuarios()
        dados = user.buscarTreeView()

        c = canvas.Canvas("conteudo_usuarios.pdf", pagesize=letter)
        path = "conteudo_usuarios.pdf"

        largura, altura = letter
        c.setFont("Helvetica", 10)

        x = 100
        y = altura - 50

        c.drawString(x, y, "ID")
        c.drawString(x + 50, y, "Nome")
        c.drawString(x + 150, y, "Telefone")
        c.drawString(x + 230, y, "Email")
        c.drawString(x + 350, y, "Usuario")
        c.drawString(x + 450, y, "Senha")

        y -= 20

        for linha in dados:
            c.drawString(x, y, str(linha[0]))
            c.drawString(x + 50, y, str(linha[1]))
            c.drawString(x + 150, y, str(linha[2]))
            c.drawString(x + 230, y, str(linha[3]))
            c.drawString(x + 350, y, str(linha[4]))
            c.drawString(x + 450, y, str(linha[5]))
            y -= 15

            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = altura - 50
                c.drawString(x, y, "ID")
                c.drawString(x + 50, y, "Nome")
                c.drawString(x + 150, y, "Telefone")
                c.drawString(x + 230, y, "Email")
                c.drawString(x + 350, y, "Usuario")
                c.drawString(x + 450, y, "Senha")
                y -= 20

        c.save()
        os.startfile(path)

    def createTreeView(self, root):

        user = usuarios()

        self.tree = ttk.Treeview(root, columns=("ID", "Nome", "Telefone", "Email", "Usuario", "Senha"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.heading("Senha", text="Senha")
        self.tree.bind("<<TreeviewSelect>>", self.selecionaUsuario)
        self.tree.pack(fill=BOTH, expand=True)

        for item in self.tree.get_children():
            self.tree.delete(item)
        rows = user.buscarTreeView()

        for row in rows:
            self.tree.insert("", END, values=row)

        return self.tree

    def atualizarTreeView(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        user = usuarios()
        rows = user.buscarTreeView()

        for row in rows:
            self.tree.insert("", END, values=row)

    def selecionaUsuario(self, event):
        seleciona_item = self.tree.selection()
        if seleciona_item:
            item = seleciona_item[0]
            values = self.tree.item(item, 'values')

            self.entID.delete(0, END)
            self.entID.insert(INSERT, values[0])

            self.entNome.delete(0, END)
            self.entNome.insert(INSERT, values[1])

            self.entTelefone.delete(0, END)
            self.entTelefone.insert(INSERT, values[2])

            self.entEmail.delete(0, END)
            self.entEmail.insert(INSERT, values[3])

            self.entUsuario.delete(0, END)
            self.entUsuario.insert(INSERT, values[4])

            self.entSenha.delete(0, END)
            self.entSenha.insert(INSERT, values[5])
