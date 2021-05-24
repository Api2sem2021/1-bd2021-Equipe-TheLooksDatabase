from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.animation import Animation


class Gerenciador(ScreenManager):
    pass

class codigo_acao(Screen):
    pass

class perfil_kv(Screen):
    pass

class noticia_kv(Screen):
    pass

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
                self.ids.num1.text = 'Quanto deseja alcançar?'
                self.ids.resp.text = self.ids.metas_input.text
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