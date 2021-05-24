from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.animation import Animation
from config import sai_som
from noticias import informacoes


class Gerenciador(ScreenManager):
    pass

class codigo_acao(Screen):
    pass

class perfil_kv(Screen):
    pass

class noticia_kv(Screen):
    def AddWidgetNoticia(self, *args):
        cont = 1
        sair = False
        while not sair:
            if cont ==1:
                self.ids.resp1.text = informacoes(resposta1)
                self.ids.resp2.text = informacoes(resposta2)
                self.ids.resp3.text = informacoes(resposta3)
                self.ids.resp4.text = informacoes(resposta4)
                
                
                cont+=1
                if cont ==2:
                    sair = True

class simulador_kv(Screen):
    pass

class comparativo_kv(Screen):
    pass

class cotacao_kv(Screen):
    pass


class metas_kv(Screen):
    def AddWidgetMetas(self, *args):
        cont = 1
        sair = False
        while not sair:
            if cont ==1:
                self.ids.resp.text = self.ids.metas_input.text
                self.ids.num1.text = 'Quanto deseja alcançar?'
                sai_som('Quanto deseja alcançar?')
                
                cont+=1
                if cont ==2:
                    sair = True

        

class conversao_kv(Screen):
    pass
class Menu(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        
        return Gerenciador()
    
Menu().run()