import builtins

class GravaDados:

    usuariosCadastrados = {
      "loginArmazenado" : "cliente",
      "senhaArmazenada" : "1234",
      "nomeUsuario" : "João dos Santos",
  }


    def salvaDados(self):
        with open("Modulos\\dados.txt","w")as dados:
            dados.write(self.usuariosCadastrados)
            dados.close()
        print("dados armazenados")

    def leDados(self):
        with builtins.open("Modulos\\dados.txt","r")as dados:
            print(f"No arquivo temos: \n {dados}")
            for linha in dados.readlines(): 
                print (linha.rstrip())

    def exportaDados(self):
        print("")

dados = GravaDados()
dados.salvaDados
dados.leDados()