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
import http.server
import socketserver
import threading

def initnet():
    PORT = 8080
    Handler = http.server.SimpleHTTPRequestHandler
    Handler.path = "index.html"
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

#kivy
def getimages(self): #grab images and return as glob
    print("create image glob")
    path = "/run/media/foxx/HDD/PHOTO/2-15/"
    #path = "/home/foxx/Pictures/"
    filetype = ("*.jpg", "*.JPG", "*.png", "*.PNG")
    s = set()
    for i in filetype:
        s = s | set(glob.glob(path + i))
    self.imageglob = list(s)
    return self.imageglob

#kivy
def genlist(self): #return list of images to use on this cycle
    print("generating and reducing list")
    self.pused = self.using #set previously used
    self.tused = list(set(self.pused) | set(self.tused)) # total used = prev + total
    us = list(set(self.ig) - set(self.tused)) #using glob - previously used
    self.using = us[0:20] #use only first x of previously unused
    return self.using

#kivy
def loadimages(self, im): #load images passed into carousel
    print("loading images into carousel")
    for i in im:
        print(i)
        image = AsyncImage(source=str(i))
        self.carousel.add_widget(image)

#kivy class
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

    # kivy
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
    net = threading.Thread(target=initnet)
    net.start()
    SlideShow().run()