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


def getimages(self): #grab images and return as glob
    print("create image glob")
    self.imageglob = glob.glob("/home/foxx/Pictures/*.jpg")
    return self.imageglob


def genlist(self): #return list of images to use on this cycle
    print("generating and reducing list")
    self.pused = self.using #set previously used
    self.tused = list(set(self.pused) | set(self.tused)) # total used = prev + total
    us = list(set(self.ig) - set(self.tused)) #using glob - previously used
    self.using = us[0:20] #use only first x of previously unused
    return self.using


def loadimages(self, im): #load images passed into carousel
    print("loading images into carousel")
    for i in im:
        print(i)
        image = AsyncImage(source=str(i))
        self.carousel.add_widget(image)


class SlideShow(App):
    def build(self):
        print("building app") # build app and set variables
        self.imageglob = getimages(self)
        self.ig = self.imageglob
        self.used = ()
        self.using = ()
        self.tused = ()
        self.pused = ()
        Clock.schedule_interval(self.update, 4) # create clock scheduler
        self.carousel = Carousel(direction='right') # create carousel child widget
        root = BoxLayout() ## create root widget
        root.add_widget(self.carousel) # add child widget to root widget
        return root

    def update(self, *args): # update function to run on Clock Schedule
        print("updating..")
        print(time.time())
        if self.carousel.next_slide: # if we can still swipe then swipe
            print("swiping")
            self.carousel.load_next()
        else: # otherwise clear list of previously used, clear carousel, and reload images to start over
            self.tused = ()
            x = genlist(self)
            self.carousel.clear_widgets()
            loadimages(self, x)


if __name__ == '__main__':
    SlideShow().run()
