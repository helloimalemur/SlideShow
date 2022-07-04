from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
import glob
import time
import asyncio
import kivy

class SlideShow(App):
    def build(self):
        c = Carousel(direction='right')
        images = glob.glob("/home/foxx/Pictures/*.jpg")
        for i in images:
            curimage = AsyncImage(source=i)
            c.add_widget(curimage)
            print(curimage)
            #time.sleep(3)
            #c.next_slide()
        root = BoxLayout()
        root.add_widget(c)
        return root


if __name__ == '__main__':
    SlideShow().run()


