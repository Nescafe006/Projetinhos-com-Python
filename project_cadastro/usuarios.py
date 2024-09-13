from Banco import Banco


class usuarios(object):

    def __init__(self, id=0, nome="", telefone="", email="", usuario="", senha=""):
        self.info = {}
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def inserirUsuario(self):
        b = Banco()

        try:
            c = b.conexao.cursor()

            c.execute(
                "insert into usuarios(nome, telefone, email, usuario, senha) values ('" + self.nome + "','" + self.telefone + "','" + self.email + "','" + self.usuario + "','" + self.senha + "')")

            b.conexao.commit()
            c.close()
            return "Usuario cadastrado com sucesso!"
        except:
            return "Ocorreu um erro!"

    def alterarUsuario(self):
        b = Banco()
        try:
            c = b.conexao.cursor()

            c.execute(
                "update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + "', usuario = '" + self.usuario + "', senha = '" + self.senha + "' where id = " + self.id + " ")

            b.conexao.commit()
            c.close()

            return "Usuario atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuario!"

    def excluirUsuario(self):
        b = Banco()
        try:

            c = b.conexao.cursor()

            c.execute("delete from usuarios where id = " + self.id + " ")

            b.conexao.commit()

            c.close()

            return "Usuario excluido com sucesso"
        except:
            return "Ocorreu um erro na exclusão do usuario"

    def buscarUsuario(self):
        b = Banco()

        try:
            c = b.conexao.cursor()

            c.execute("select * from usuarios where id = " + self.id + " ")

            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso"
        except:
            return "Ocorreu um erro na busca"

    def buscarTreeView(self):
        b = Banco()
        c = b.conexao.cursor()

        c.execute("select * from usuarios")

        rows = []

        for linha in c:
            rows.append((linha[0], linha[1], linha[2], linha[3], linha[4], linha[5]))

        c.close()

        return rows
