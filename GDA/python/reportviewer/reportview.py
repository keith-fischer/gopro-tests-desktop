#!/usr/bin/env python
# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
import Tkinter as tk
import simplerestserver
import time
import threading
from flask import Flask, url_for
from flask import json
from flask import Response
from flask import Flask, request
from flask_restful import Resource, Api

from json import dumps
# --------------------------------------------------------------------------
#
# --------------------------------------------------------------------------
class ReportViewer:
    bannertxt = ""
    _self = None
    _win = None
    _lbl = None
    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------
    def __init__(self):
        # self.bannermainloop=threading.Thread(target=self.init)
        # #self.bannermainloop.daemon = True
        # self.bannermainloop.start()
        self.init()

    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------
    def init(self):
        self.banner_txt = "Banner not Ready"
        self.banner_txt_old = ""
        self.width = 700
        self.height = 500
        self.banner_win = tk.Tk()
        self.banner_win.withdraw()
        self.banner_win.title('Camera Mode Banner')
        screenWi = self.banner_win.winfo_screenwidth()
        screenHe = self.banner_win.winfo_screenheight()
        self.banner_win.update()
        # retrieve the requested size which is different as the current size
        guiWi = self.width  # root.winfo_reqwidth()
        guiHe = self.height  # root.winfo_reqheight()
        # position of the window
        x = (screenWi - guiWi) / 2
        y = (screenHe - guiHe) / 2
        self.banner_win.geometry("%dx%d+%d+%d" % (guiWi, guiHe, x, y))
        self.banner_lbl = tk.Label(self.banner_win,  width=self.width,compound=tk.CENTER,bg="white",fg="black",text=self.banner_txt,font="Verdana 40 bold", cursor="arrow")
        self.banner_lbl.pack()
        self.counter =0
        self.banner_win.deiconify()
        self.banner_txt = "Banner is Ready"
        self.setbannertxt(self.banner_txt)
        self.banner_win.update_idletasks()
        self.banner_win.update()
        #self.banner_win.after(2000, self.eventloop)
        #self.httpserver = BannerServer.RunServer(self.respsmsg)

        CameraBannerText._self=self
        CameraBannerText._win = self.banner_win
        CameraBannerText._lbl=self.banner_lbl

        simplerestserver.callback=CameraBannerText.respsmsg
        simplerestserver.JSON_FIELD="banner"
        simplerestserver.start()

        #self.eventloop()
        #self.banner_win.mainloop()

    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------
    def eventloop(self):
        while True:
            self.bannerupdate()
            self.banner_win.update_idletasks()
            self.banner_win.update()
            time.sleep(1)
            #self.banner_win.mainloop(1)
    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------
    @staticmethod
    def respsmsg(msg):
        CameraBannerText.bannertxt = msg
        CameraBannerText._lbl.config(text=CameraBannerText.bannertxt, cursor="arrow")
        CameraBannerText._lbl.update_idletasks()
        CameraBannerText._win.lift()
        CameraBannerText._win.call('wm', 'attributes', '.', '-topmost', True)
        #CameraBannerText._win.after_idle(CameraBannerText._self, 'wm', 'attributes', '.', '-topmost', False)
        CameraBannerText._win.update_idletasks()
        CameraBannerText._win.update()
    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------
    def mainloop(self):
        self.banner_win.mainloop()

        #self.server = MsgServer()

    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------
    def setbannertxt(self,txt):
        CameraBannerText.bannertxt = txt
        #self.banner_win.after(1000, self.eventloop)
        #self.banner_win.mainloop(100)

    # --------------------------------------------------------------------------
    #
    # --------------------------------------------------------------------------
    def bannerupdate(self):
        self.counter +=1
        self.banner_txt = CameraBannerText.bannertxt
        #txt = "%s-Banner is ready" % str(self.counter)
        #self.setbannertxt(txt)
        if self.banner_txt != self.banner_txt_old:
            self.banner_lbl.config(text=self.banner_txt)
            self.banner_lbl.update_idletasks()

            #self.setbannertxt(txt)
            self.banner_win.update_idletasks()
            self.banner_win.update()
        # if not self.banner_lbl:
        #     self.banner_lbl = self.banner_win.Label(self.banner_win,textvariable=self.banner_txt,compound=tk.CENTER,bg="white",fg="black",text=self.banner_txt,font="Verdana 40 bold").pack()
            # else:
        self.banner_txt_old = self.banner_txt

        #self.banner_win.after(2000, self.eventloop)

        #self.banner_win.mainloop(100)

banner=CameraBannerText()
