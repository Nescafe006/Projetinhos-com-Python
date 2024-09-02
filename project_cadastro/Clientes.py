from Banco import Banco
from tkinter import messagebox
banco = Banco()

class Cliente:
    def __init__(self, cliente_id, name: str, cpf: str, phone: str, email: str, senha: str):
        self.dict: {}
        self.id = cliente_id
        self.name = name
        self.cpf = cpf
        self.phone = phone
        self.email = email
        self.senha = senha


    def insert(self) -> str:
        try:
            banco.cursor.execute(
                "insert into Client (nome, cpf, phone, email, senha) values ('" + self.nome + "', '" + self.cpf + "', '" + self.phone + "', '" + self.email + "', '" + self.senha + "')")
            banco.commit()
            banco.cursor.close()

            return "Cliente cadastrado com sucesso"

        except:
            return "Ocorreu um erro no cadastro de cliente"

    def update(self):
        try:
            banco.cursor.execute(
                "update cliente set name = '" + self.nome + "', cpf = '" + self.cpf + "', phone = '" + self.phone + "', email = '" + self.email + "' where id = '" + self.id + "'")
            banco.connection.commit()

            return "Cliente atualizado!"

        except:
            return "erro na atualização do cliente!"

    def delete(self, cliente_id):
        try:
            banco.cursor.execute("delete from cliente where id = " + cliente_id + "")
            banco.connection.commit()
            banco.cursor.close()

            return "Cliente excluído com sucesso!"

        except:
            return "Erro na exclusão do cliente"

    def select(self, cliente_id):
        try:
            banco.cursor.execute("select * from cliente where id = " + cliente_id + "")

            data = []

            for linha in data:
                self.id =linha [0]
                self.nome = linha [1]
                self.cpf = linha [2]
                self.phone = linha [3]
                self.email =linha [4]
                self.senha =linha [5]

            banco.cursor.close()

            return messagebox.showinfo("", "busca feita com sucesso")
        except:
            return messagebox.showerror("", "erro na busca")