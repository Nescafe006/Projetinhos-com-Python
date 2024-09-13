from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from fpdf import FPDF


class Application:
    def __init__(self, master=None):
        self.master = master
        self.fonte = ("Verdana", "8")

        self.container = Frame(master)
        self.container["padx"] = 20
        self.container["pady"] = 20
        self.container.pack()

        self.titulo = Label(self.container, text="Cadastro de Cidades", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        self.lblNome = Label(self.container, text="Nome:", font=self.fonte, width=10)
        self.lblNome.pack(anchor=W)
        self.txtNome = Entry(self.container)
        self.txtNome["width"] = 30
        self.txtNome["font"] = self.fonte
        self.txtNome.pack()

        self.lblEstado = Label(self.container, text="Estado:", font=self.fonte, width=10)
        self.lblEstado.pack(anchor=W)
        self.txtEstado = Entry(self.container)
        self.txtEstado["width"] = 30
        self.txtEstado["font"] = self.fonte
        self.txtEstado.pack()

        self.btnInserir = Button(self.container, text="Inserir", font=self.fonte, width=12, command=self.inserirCidade)
        self.btnInserir.pack(side=LEFT, padx=5, pady=5)

        self.btnAlterar = Button(self.container, text="Alterar", font=self.fonte, width=12, command=self.alterarCidade)
        self.btnAlterar.pack(side=LEFT, padx=5, pady=5)

        self.btnExcluir = Button(self.container, text="Excluir", font=self.fonte, width=12, command=self.excluirCidade)
        self.btnExcluir.pack(side=LEFT, padx=5, pady=5)

        self.btnGerarPDF = Button(self.container, text="Gerar PDF", font=self.fonte, width=12, command=self.gerarPDF)
        self.btnGerarPDF.pack(side=LEFT, padx=5, pady=5)

        self.btnVoltarMenu = Button(self.container, text="Voltar ao Menu", font=self.fonte, width=12, command=self.voltarMenu)
        self.btnVoltarMenu.pack(side=LEFT, padx=5, pady=5)

        self.lblmsg = Label(self.container, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack(pady=5)

        self.treeview_frame = Frame(master)
        self.treeview_frame["padx"] = 100
        self.treeview_frame["pady"] = 100
        self.treeview_frame.pack()

        self.treeview = ttk.Treeview(self.treeview_frame, columns=("Nome", "Estado"),
                                     show="headings", selectmode="browse")

        self.treeview.heading("Nome", text="Nome")
        self.treeview.heading("Estado", text="Estado")

        self.treeview.pack()

    def inserirCidade(self):
        nome = self.txtNome.get()
        estado = self.txtEstado.get()

        if nome and estado:
            self.treeview.insert("", "end", values=(nome, estado))
            self.limparCampos()
            messagebox.showinfo("Sucesso", "Cidade inserida com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")

    def alterarCidade(self):
        selected_item = self.treeview.selection()
        if selected_item:
            nome = self.txtNome.get()
            estado = self.txtEstado.get()

            if nome and estado:
                self.treeview.item(selected_item, values=(nome, estado))
                self.limparCampos()
                messagebox.showinfo("Sucesso", "Cidade alterada com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
        else:
            messagebox.showwarning("Aviso", "Nenhuma cidade selecionada para alterar!")

    def excluirCidade(self):
        selected_item = self.treeview.selection()
        if selected_item:
            self.treeview.delete(selected_item)
            self.limparCampos()
            messagebox.showinfo("Sucesso", "Cidade excluída com sucesso!")
        else:
            messagebox.showwarning("Aviso", "Nenhuma cidade selecionada para excluir!")

    def gerarPDF(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Cadastro de Cidades", ln=True, align="C")
        pdf.ln(10)

        for item in self.treeview.get_children():
            nome, estado = self.treeview.item(item, 'values')
            pdf.cell(100, 10, txt=f"Nome: {nome}", ln=True)
            pdf.cell(100, 10, txt=f"Estado: {estado}", ln=True)
            pdf.ln(5)

        pdf.output("cidades.pdf")
        messagebox.showinfo("Sucesso", "PDF gerado com sucesso!")


    def voltarMenu(self):

        self.master.destroy()

    def limparCampos(self):
        self.txtNome.delete(0, END)
        self.txtEstado.delete(0, END)

