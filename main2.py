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
    self.images = glob.glob("/home/foxx/Pictures/o/*.jpg")
    for i in self.images:
        print(i)
        image = AsyncImage(source=i)
        self.carousel.add_widget(image)
    return self.images


class SlideShow(App):
    def build(self):
        Clock.schedule_interval(self.update, 3) # clock runs update function every 3 seconds after loading main widget
        self.carousel = Carousel(direction='right') #create child Carousel widget
        self.images = getimages(self) #load images and add to Carousel widget
        root = BoxLayout()# create root widget
        root.add_widget(self.carousel) # add child widgets
        return root #return root widget

    def update(self, *args):
        #print(time.time()) #debug output
        if self.carousel.next_slide: #if there is a next slide
            self.carousel.load_next() #load the next slide in carousel
            self.carousel.remove_widget(self.carousel.previous_slide)
        #elif self.carousel.next_slide == False:
        #    self.
        else: #otherwise
            self.carousel.clear_widgets() #clear the widgets from carousel
            getimages(self)# and reload images from folder and reinitialize the child widget

if __name__ == '__main__':
    SlideShow().run()
