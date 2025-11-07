class Menu:
    def __init__(self):
        pass

    def Menu(self):
        print("Menu")
        print("1 - Registrar Limpeza")
        print("2 = Editar registro")
        print("3 - Excluir registro")
        print("4 - Sair")

        op = int(input("Selecione uma opção: "))
    
        match op:
            case 1:
                self.registrar_limpeza()
            case 2:
                self.editar_registro()
            case 3:
                self.excluir_registro()
            case 4: 
                print("Saindo...")
                break
        
    def registrar_limpeza(self):
        

class Registro:
    def __init__(self, sala, tipo, responsavel):
        self.sala = sala
        self.tipo = tipo
        self.responsavel = responsavel



registro1 = Registro()
