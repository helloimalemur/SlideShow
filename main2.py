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
    #for i in self.images:
    #    print(i)
    #    image = AsyncImage(source=i)
    #    self.carousel.add_widget(image)
    return self.images

#if empty set imagelist as first 100 images, if not empty, diff against main list - take next 100 images not used already and set imagelist
#diff against usedimages
def genlist(self):
    if self.used:
        self.used = list(set(self.used) + set(self.using))
        self.using = ()
        self.using = list(set(self.images) | set(self.used))
        self.using = self.using[0:99]
    else:
        self.used = ()
        self.using = list(set(self.images[0:99]))
    return self.using

def loadimages(self, im):
    for i in im:
        print(i)
    image = AsyncImage(source=str(i))
    self.carousel.add_widget(image)

class SlideShow(App):
    def build(self):
        self.used = ()
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
        x = genlist(self)
        loadimages(self, x)
        if self.carousel.next_slide:
            self.carousel.load_next()
        else:
            self.carousel.clear_widgets()
            getimages(self)



if __name__ == '__main__':
    SlideShow().run()


