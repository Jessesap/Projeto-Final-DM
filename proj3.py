from kivy.app import App 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass
class Cardapio(Screen):
    pass
class Buffet(Screen):
    def on_checkbox_Active1(self, checkboxInstance, isActive):
            if isActive:
                self.ids.lb5.text = "Filé Bovino Selecionado"
            else:
                self.ids.lb5.text = "Nenhuma Seleção"      

    def on_checkbox_Active2(self, checkboxInstance, isActive):
        if isActive:
            self.ids.lb6.text = "Filé Suino Selecionado"
        else:
            self.ids.lb6.text = "Nenhuma Seleção"       
                
    def on_checkbox_Active3(self, checkboxInstance, isActive):
        if isActive:
            self.ids.lb7.text = "Franbacon Selecionado"
        else:
            self.ids.lb7.text = "Nenhuma Seleção"  
        
    def on_checkbox_Active4(self, checkboxInstance, isActive):
        if isActive:
            self.ids.lb8.text = "Queijo Coalho Selecionado"
        else:
            self.ids.lb8.text = "Nenhuma Seleção" 
  
class Menu(Screen):
    pass

# class Cardapio(Screen):
    

class Apresentacao(Screen): 
    def on_checkbox_Active1(self, checkboxInstance, isActive):
        if isActive:
            self.ids.lb1.text = "Stout Selecionada"
        else:
            self.ids.lb1.text = "Não Selecionado"      

    def on_checkbox_Active2(self, checkboxInstance, isActive):
        if isActive:
            self.ids.lb2.text = "IPA Selecionada"
        else:
            self.ids.lb2.text = "Não Selecionado"      
             
    def on_checkbox_Active3(self, checkboxInstance, isActive):
        if isActive:
            self.ids.lb3.text = "Weiss Selecionada"
        else:
            self.ids.lb3.text = "Não Selecionado"   
    
    def on_checkbox_Active4(self, checkboxInstance, isActive):
        if isActive:
            self.ids.lb4.text = "Porter Selecionada"
        else:
            self.ids.lb4.text = "Não Selecionado"          

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