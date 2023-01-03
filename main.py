from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(700, 410)
        p.background(255)

        #Hier wähle ich die Farbe
        p.fill(140, 90, 55)

        p.rectMode(p.CENTER)
        #Ich verwende ein Qudrat
        #p.square(150, 122, 156)
  
        #Hier wird die erte for-Scleife verwendet!
        #ES wird 10 mal die Zählvariabeauf der Console gedruckt.
        for i in range(10):
            print(i)    
            #In der Schleife können wir auch Formen erzeugen!
            p.square(350, 205, 250 - i*25)
   
    p.setup = setup
  
myp5 = window.p5.new(sketch)
