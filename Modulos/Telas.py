#importando a classe Time do proprio python
import time
import os
class Telas:

  def entradaSistema(self):
    print( f"+------------------------------------------------------+" )
    print( f"|                                                      |" )
    print( f"|           ** Seja Bem Vindo ao Sistema **            |" )
    print( f"|                                                      |" )
    print( f"+------------------------------------------------------+" )

    self.esperaLimpa()
    
  def esperaLimpa(self,tempo = 3 ):

    time.sleep(tempo)
    #esperar X sec
    #limpa a tela

    self.limpaConsole()
    
  def saidaSistema(self):
    print( f"+------------------------------------------------------+" )
    print( f"|                                                      |" )
    print( f"|          ** Obrigado por usar o Sistema **           |" )
    print( f"|                                                      |" )
    print( f"+------------------------------------------------------+" )
    
  def mensagensSistema(self, mensagem ):
    print( f"+------------------------------------------------------+" )
    print( f"|                                                      |" )
    print( f"  ** {mensagem} **            " )
    print( f"|                                                      |" )
    print( f"+------------------------------------------------------+" )


  def limpaConsole(self):
    print("")
    if os.name == "nt": #windows = nt / Linux = posix / mac = darwin
        os.system("cls")
    elif os.name == "darwin":
        os.system("clear")
    else: 
      os.system("clear")
  
  def exibeMenu (self):
    print( f"+------------------------------------------------------+" )
    print( f"| Bem Vindo {usuario}                                  |" )
    print( f"  ** Menu - Escolha uma opção:                          " )
    print( f"| 1 - Cadastro                                         |" )
    print( f"| 2 - Listar                                           |" )
    print( f"+------------------------------------------------------+" )



    #tipoSistema = os.name
    #switch(tipoSistema):
    #   case "nt":
    #       os.system("cls")
    #       break: