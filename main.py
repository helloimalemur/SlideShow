from kivy.clock import Clock
from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
import glob
import time
import multiprocessing
import os
import uploadserver

## need to white creation of "images/" folder


def net():
    uploadserver.app.run()


class SlideShowApp(App):
    def build(self):
        print("building app") # build app and set variables
        self.imageglob = self.getimages()
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
            self.ig = self.imageglob
            self.getimages()
            self.tused = ()
            x = self.genlist()
            self.carousel.clear_widgets()
            self.loadimages(x)


    def getimages(self): #grab images and return as glob
        print("create image glob")
        #path = "/run/media/foxx/HDD/PHOTO/2-15/"
        path = "images/"

        filetype = ("*.jpg", "*.JPG", "*.png", "*.PNG")
        s = set()
        for i in filetype:
            s = s | set(glob.glob(path + i))
        self.imageglob = list(s)
        return self.imageglob

    def genlist(self):  # return list of images to use on this cycle
        print("generating and reducing list")
        self.pused = self.using  # set previously used
        self.tused = list(set(self.pused) | set(self.tused))  # total used = prev + total
        us = list(set(self.ig) - set(self.tused))  # using glob - previously used
        self.using = us[0:20]  # use only first x of previously unused
        return self.using

    def loadimages(self, im):  # load images
        path = str(os.getcwd() + "/images/")
        print(path) #passed into carousel
        print("loading images into carousel")
        for i in im:
            print(i)
            image = AsyncImage(source=str(i), allow_stretch=True)
            self.carousel.add_widget(image)


if __name__ == '__main__':
    session = multiprocessing.Process(target=net)
    session.start()
    SlideShowApp().run()
    session.terminate()
