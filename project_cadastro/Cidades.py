from Banco import Banco

banco = Banco()

class Cidade:
    def __init__(self, cidade_id, nome: str, uf:str):
        self.dict: {}

        self.id = cidade_id
        self.nome = nome
        self.uf = uf


    def insert(self):

        try:
            banco.cursor.execute("insert into city (name, uf) values ('" + self.nome + "', '" + self.uf + "'")
            banco.commit()
            banco.cursor.close()
            return "Localidade cadastrada com sucesso!"
        except:
            return "Ocorreu um erro na inserção da Localidade"

    def update(self):
        try:
            banco.cursor.execute("update city set name = '" + self.nome + "', '" + self.uf + "'")
            banco.commit()
            banco.cursor.close()

            return "Cidade atualizada com sucesso!"

        except:
            return "Erro ao atualizar cidade!"
    def delete(self):
        try:
            banco.cursor.execute("delete from city where id = '" + self.id + "'")
            banco.commit()
            banco.cursor.close()

            return "Cidade excluida com sucesso!"
        except:
            return "Erro ao excluir cidade!"

    def selectUser(self, cidade_id):
        try:
            banco.cursor.execute("select * from cidade where id = '" + cidade_id + "'")
            banco.commit()
            banco.cursor.close()

            data = []

            for linha in data:
                self.id = linha[0]
                self.nome = linha[1]
                self.uf = linha[2]

            return "Busca feita com sucesso!"

        except:
            return "Erro ao buscar cidade!"
