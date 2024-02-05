from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.config import Config
from Wzory_podstawowe import *
from kivy.properties import ObjectProperty, StringProperty



Config.set('graphics', 'width', '350')
Config.set('graphics', 'height', '700')

 
class MainScreen(Screen):
    pass
    
class InfoScreen(Screen):
    pass

class ChooseScreen(Screen):
    pass

class CalculatorScreen(Screen):
    pass 

class Wzory_pod(Screen):
    pass

class Pole_(Screen):
    
    d = ObjectProperty(None)
    g = StringProperty('')

    def btn(self):        
        
        for _ in range(1): 
            try:   
                d = int(self.d.text)
                g = round(pole(d),4)
                break
            except ValueError:
                g = "Chyba coś źle wpisałeś kolego"
         
        self.d.text = ""
        self.g = str(g) 

class Huber_(Screen):
    
    l = ObjectProperty(None)
    d = ObjectProperty(None)
    V = StringProperty('')

    def btn(self):        
        
        for _ in range(1): 
            try:   
                l = int(self.l.text)
                d = int(self.d.text)
                V = round(Huber(l,d),4)
                break
            except ValueError:
                V = "Chyba coś źle wpisałeś kolego"
         
        self.l.text = ""
        self.d.text = ""
        self.V = str(V) 

class Smalian_(Screen):
    
    l = ObjectProperty(None)
    d0 = ObjectProperty(None)
    dl = ObjectProperty(None)
    stan = ObjectProperty(None)    
    V = StringProperty('')

    def btn(self):        
        
        for _ in range(1): 
            try:   
                l = int(self.l.text)
                d0 = int(self.d0.text)
                dl = int(self.dl.text)
                stan = (self.stan.text)
                V = round(Smalian(l,d0,dl,stan),4)
                break
            except ValueError:
                V = "Chyba coś źle wpisałeś kolego"
         
        self.l.text = ""
        self.d0.text = ""
        self.dl.text = ""
        self.stan.text = ""
        self.V = str(V) 

class Hossfeld_(Screen):
    
    l = ObjectProperty(None)
    d = ObjectProperty(None)
    dl = ObjectProperty(None)
    stan = ObjectProperty(None)    
    V = StringProperty('')

    def btn(self):        
        
        for _ in range(1): 
            try:   
                l = int(self.l.text)
                d = int(self.d.text)
                dl = int(self.dl.text)
                stan = (self.stan.text)
                V = round(Hossfeld(l,d,dl,stan),4)
                break
            except ValueError:
                V = "Chyba coś źle wpisałeś kolego"
         
        self.l.text = ""
        self.d.text = ""
        self.dl.text = ""
        self.stan.text = ""
        self.V = str(V) 
        
    
     

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("Den.kv")


class DenApp(App):
    def build(self):

        return kv

if __name__ == "__main__":
    DenApp().run()