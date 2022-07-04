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
        #create child widget
        carousel = Carousel(direction='right')

        #load images
        images = glob.glob("/home/foxx/Pictures/*.jpg")

        #for i in images:

        ## create root layout and add widgets
        root = BoxLayout()
        root.add_widget(carousel)
        return root


if __name__ == '__main__':
    SlideShow().run()


