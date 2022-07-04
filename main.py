from kivy.clock import Clock
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
import glob
import random
import time
import asyncio
import kivy


def getimages(self):
    self.images = glob.glob("/home/foxx/Pictures/*.jpg")
    for i in self.images:
        print(i)
        image = AsyncImage(source=i)
        self.carousel.add_widget(image)
    return self.images


class SlideShow(App):
    def build(self):
        Clock.schedule_interval(self.update, 3)
        #create child widget
        self.carousel = Carousel(direction='right')
        #load images
        self.images = getimages(self)


        ## create root layout and add widgets
        root = BoxLayout()
        root.add_widget(self.carousel)

        return root

    def update(self, *args):
        print(time.time())
        if self.carousel.next_slide:
            self.carousel.load_next()
        else:
            self.carousel.clear_widgets()
            getimages(self)



if __name__ == '__main__':
    SlideShow().run()


