from kivy.clock import Clock
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage, Image
from kivy.uix.gridlayout import GridLayout

import glob
import time
import asyncio

class SlideShowApp(App):
    def build(self):
        slideshow = SlideShowApp()
        #x = self.window()
        #layout.add_widget(x)
        return slideshow

    def window(self):

        self.c = Carousel(direction='right')
        #Clock.schedule_interval(self.update, 2)

        for i in SlideShowApp.getimages():
            self.curimage = AsyncImage(source=i)
            self.c.add_widget(self.curimage)
            print(self.curimage)
            # time.sleep(3)
            # c.next_slide()

        return self.c

    def getimages():
        images = glob.glob("/home/foxx/Pictures/*.jpg")
        return images

    def update(self, *args):
        print(time.time())


class Layout(GridLayout):
    def __init__(self):
        self.c = None

if __name__ == '__main__':
    SlideShowApp().run()
