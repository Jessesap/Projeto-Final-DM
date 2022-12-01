from kivy.app import App 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Cardapio(Screen):
    

class Apresentacao(Screen): 
    def on_checkbox_Active1(self, checkboxInstance, isActive):
        if isActive:
            self.ids.pb.value += 25
            self.ids.lb1.text = "Item Selecionado1"
        else:
            self.ids.lb1.text = "Nenhuma Seleção" 
            
        if self.ids.pb.value == 100:
                self.ids.lb5.text = "Total de itens atingido!"
        else:
            if self.ids.pb.value == 75:
                self.ids.lb5.text = "Um item para fechar o pedido"
            else:
                self.ids.lb5.text = "Itens permitidos por pedido: 4"      

    def on_checkbox_Active2(self, checkboxInstance, isActive):
        if isActive:
            self.ids.pb.value += 25
            self.ids.lb2.text = "Item Selecionado2"
        else:
            self.ids.lb2.text = "Nenhuma Seleção" 
            
        if self.ids.pb.value == 100:
                self.ids.lb5.text = "Total de itens atingido!"
        else:
            if self.ids.pb.value == 75:
                self.ids.lb5.text = "Um item para fechar o pedido"
            else:
                self.ids.lb5.text = "Itens permitidos por pedido: 4"      
             
    def on_checkbox_Active3(self, checkboxInstance, isActive):
        if isActive:
            self.ids.pb.value += 25
            self.ids.lb3.text = "Item Selecionado3"
        else:
            self.ids.lb3.text = "Nenhuma Seleção" 
            
        if self.ids.pb.value == 100:
                self.ids.lb5.text = "Total de itens atingido!"
        else:
            if self.ids.pb.value == 75:
                self.ids.lb5.text = "Um item para fechar o pedido"
            else:
                self.ids.lb5.text = "Itens permitidos por pedido: 4"  
    
    def on_checkbox_Active4(self, checkboxInstance, isActive):
        if isActive:
            self.ids.pb.value += 25
            self.ids.lb4.text = "Item Selecionado4"
        else:
            self.ids.lb4.text = "Nenhuma Seleção" 
            
        if self.ids.pb.value == 100:
                self.ids.lb5.text = "Total de itens atingido!"
        else:
            if self.ids.pb.value == 75:
                self.ids.lb5.text = "Um item para fechar o pedido"
            else:
                self.ids.lb5.text = "Itens permitidos por pedido: 4"  
    
        # def checa_pedido(self):
        #     if self.ids.pb.value == 100:
        #             self.ids.lb5.text = "Total de itens por pedido atingido!"
        #     else:
        #         if self.ids.pb.value == 75:
        #             self.ids.lb5.text = "Aviso: falta um item para fechar o pedido"
        #         else:
        #             self.ids.lb5.text = "Itens permitidos por pedido: 4"         

class Pagamento(Screen):
    def __init__(self, atividades = [], **kwargs):
        super().__init__(**kwargs)
        for ativ in atividades:
            self.ids.box.add_widget(Funcoes(text=ativ))
    
    def addComponentes(self):
        texto = self.ids.tarefa.text
        self.ids.box.add_widget(Funcoes(text=texto))
        self.ids.tarefa.text = ''
    
    def spinner_Clicado(self, value):
        self.ids.escolha.text = value             
            
            
class Funcoes(BoxLayout):
    def __init__(self,text='',**kwargs):          
        super().__init__(**kwargs)
        self.ids.lab1.text = text

class proj3(App):
    def build(self):
        return Gerenciador()  
    
if __name__ == "__main__":
    proj3().run()