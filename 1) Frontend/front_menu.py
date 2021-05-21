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
    def AddWidgetMetas(self,msg, *args):
        pass


class conversao_kv(Screen):
    pass
class Menu(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        
        return Gerenciador()
    
Menu().run()