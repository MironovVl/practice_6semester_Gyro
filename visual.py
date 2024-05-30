import math
import tkinter as tk
import os
from math import cos

from PIL import ImageTk, Image


class visual:
    im_st = Image.open("images/avi-static.png")
    im_bg = Image.open("images/avi-bg2.png")
    canvas = None
    window1 = tk.Tk()

    def __init__(self):
        self.window1.title('Авиагризонт')
        self.canvas1 = tk.Canvas(self.window1, width=500, height=500)
        self.canvas1.pack()
        imag_st = ImageTk.PhotoImage(self.im_st)
        imag_bg = ImageTk.PhotoImage(self.im_bg)
        # panel = tk.Label(window, image=imag_bg)
        # panel = tk.Label(window, image=imag_avi)
        # panel = tk.Label(window, image=imag_fr)

        self.canvas1.create_image(-500, -500, anchor=tk.NW, image=imag_bg)
        self.canvas1.create_image(0, 0, anchor=tk.NW, image=imag_st)

        self.window1.geometry("+{}+{}".format(50, 50))
        self.window1.update()

    def moveAvi(self, a1, b1):
        im_bg_rotation = self.im_bg.rotate(a1, expand=False)
        imag_avi = ImageTk.PhotoImage(im_bg_rotation)
        imag_st = ImageTk.PhotoImage(self.im_st)
        if a1 != 90 and a1 != -90:
            imag_avi2 = self.canvas1.create_image(-500, -500 + 15*b1 / cos(a1/180*math.pi), anchor=tk.NW, image=imag_avi)
        else:
            imag_avi2 = self.canvas1.create_image(-500, -500, anchor=tk.NW, image=imag_avi)
        self.canvas1.create_image(0, 0, anchor=tk.NW, image=imag_st)
        self.window1.update()
