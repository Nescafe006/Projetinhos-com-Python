from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Application:
    def __init__(self, master=None):
        self.master = master
        self.fonte = ("Verdana", "8")


        self.container = Frame(master)
        self.container["padx"] = 20
        self.container["pady"] = 20
        self.container.pack()


        self.titulo = Label(self.container, text="Cadastro de Clientes", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        # Nome
        self.lblNome = Label(self.container, text="Nome:", font=self.fonte, width=10)
        self.lblNome.pack(anchor=W)
        self.txtNome = Entry(self.container)
        self.txtNome["width"] = 30
        self.txtNome["font"] = self.fonte
        self.txtNome.pack()


        self.lblTelefone = Label(self.container, text="Telefone:", font=self.fonte, width=10)
        self.lblTelefone.pack(anchor=W)
        self.txtTelefone = Entry(self.container)
        self.txtTelefone["width"] = 30
        self.txtTelefone["font"] = self.fonte
        self.txtTelefone.pack()


        self.lblEndereco = Label(self.container, text="Endereço:", font=self.fonte, width=10)
        self.lblEndereco.pack(anchor=W)
        self.txtEndereco = Entry(self.container)
        self.txtEndereco["width"] = 30
        self.txtEndereco["font"] = self.fonte
        self.txtEndereco.pack()


        self.lblCidade = Label(self.container, text="Cidade:", font=self.fonte, width=10)
        self.lblCidade.pack(anchor=W)
        self.txtCidade = Entry(self.container)
        self.txtCidade["width"] = 30
        self.txtCidade["font"] = self.fonte
        self.txtCidade.pack()


        self.lblCPF = Label(self.container, text="CPF:", font=self.fonte, width=10)
        self.lblCPF.pack(anchor=W)
        self.txtCPF = Entry(self.container)
        self.txtCPF["width"] = 30
        self.txtCPF["font"] = self.fonte
        self.txtCPF.pack()


        self.btnInserir = Button(self.container, text="Inserir", font=self.fonte, width=12, command=self.inserirCliente)
        self.btnInserir.pack(side=LEFT, padx=5, pady=5)

        self.btnAlterar = Button(self.container, text="Alterar", font=self.fonte, width=12, command=self.alterarCliente)
        self.btnAlterar.pack(side=LEFT, padx=5, pady=5)

        self.btnExcluir = Button(self.container, text="Excluir", font=self.fonte, width=12, command=self.excluirCliente)
        self.btnExcluir.pack(side=LEFT, padx=5, pady=5)

        self.lblmsg = Label(self.container, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack(pady=5)


        self.treeview_frame = Frame(master)
        self.treeview_frame["padx"] = 100
        self.treeview_frame["pady"] = 100
        self.treeview_frame.pack()

        self.treeview = ttk.Treeview(self.treeview_frame, columns=("Nome", "Telefone", "Endereço", "Cidade", "CPF"),
                                     show="headings", selectmode="browse")

        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Telefone", text="Telefone")
        self.treeview.heading("Endereço", text="Endereço")
        self.treeview.heading("Cidade", text="Cidade")
        self.treeview.heading("CPF", text="CPF")

        self.treeview.pack()

    def inserirCliente(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        endereco = self.txtEndereco.get()
        cidade = self.txtCidade.get()
        cpf = self.txtCPF.get()

        if nome and telefone and endereco and cidade and cpf:
            self.treeview.insert("", "end", values=(nome, telefone, endereco, cidade, cpf))
            self.limparCampos()
            messagebox.showinfo("Sucesso", "Cliente inserido com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")

    def alterarCliente(self):
        selected_item = self.treeview.selection()
        if selected_item:
            nome = self.txtNome.get()
            telefone = self.txtTelefone.get()
            endereco = self.txtEndereco.get()
            cidade = self.txtCidade.get()
            cpf = self.txtCPF.get()

            if nome and telefone and endereco and cidade and cpf:
                self.treeview.item(selected_item, values=(nome, telefone, endereco, cidade, cpf))
                self.limparCampos()
                messagebox.showinfo("Sucesso", "Cliente alterado com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
        else:
            messagebox.showwarning("Aviso", "Nenhum cliente selecionado para alterar!")

    def excluirCliente(self):
        selected_item = self.treeview.selection()
        if selected_item:
            self.treeview.delete(selected_item)
            self.limparCampos()
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Nenhum cliente selecionado para excluir!")

    def limparCampos(self):
        self.txtNome.delete(0, END)
        self.txtTelefone.delete(0, END)
        self.txtEndereco.delete(0, END)
        self.txtCidade.delete(0, END)
        self.txtCPF.delete(0, END)

