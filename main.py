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
    return self.images

def update(self):
    print(time.time())



class SlideShow(App):
    def build(self):
        Clock.schedule_interval(update, 2)
        #create child widget
        self.carousel = Carousel(direction='right')

        #load images
        self.images = getimages(self)
        for i in self.images:
            print(i)
            image = AsyncImage(source=i)
            self.carousel.add_widget(image)

        ## create root layout and add widgets
        root = BoxLayout()
        root.add_widget(self.carousel)

        return root


if __name__ == '__main__':
    SlideShow().run()


