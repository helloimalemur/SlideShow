from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
import glob
import time
import asyncio

class SlideShow(App):
    def build(self):
        #l = Label(text="yo")
        c = Carousel(direction='right')
        images = glob.glob("*.jpg")
        for i in images:
            curimage = AsyncImage(source=i)
            c.add_widget(curimage)
            time.sleep(3)
            #c.next_slide()
        return c


if __name__ == '__main__':
    SlideShow().run()


