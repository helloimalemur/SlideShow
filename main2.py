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
    print("create image glob")
    self.imageglob = glob.glob("/home/foxx/Pictures/*.jpg")
    return self.imageglob


# if empty set imagelist as first 100 images, if not empty, diff against main list - take next 100 images not used already and set imagelist
# diff against usedimages
def genlist(self):
    print("generating and reducing list")
    self.pused = self.using
    self.tused = list(set(self.pused) | set(self.tused))
    us = list(set(self.ig) - set(self.tused))
    self.using = us[0:20] #set ims actually loaded
    return self.using


def loadimages(self, im):
    print("loading images into carousel")
    #im = genlist(self)
    for i in im:
        print(i)
        image = AsyncImage(source=str(i))
        self.carousel.add_widget(image)


class SlideShow(App):
    def build(self):
        print("building app")
        self.imageglob = getimages(self)
        self.ig = self.imageglob
        self.used = ()
        self.using = ()
        self.tused = ()
        self.pused = ()
        Clock.schedule_interval(self.update, 4)
        # create child widget
        self.carousel = Carousel(direction='right')
        # load images
        # self.images = getimages(self)
        ## create root layout and add widgets
        root = BoxLayout()
        root.add_widget(self.carousel)
        return root

    def update(self, *args):
        print("updating..")
        print(time.time())
        #x = genlist(self)
        #loadimages(self, x)
        if self.carousel.next_slide:
            print("swiping")
            self.carousel.load_next()
        else:
            self.tused = ()
            x = genlist(self)
            self.carousel.clear_widgets()
            loadimages(self, x)
            #getimages(self)


if __name__ == '__main__':
    SlideShow().run()
