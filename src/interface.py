import tkinter as tk
from tkinter import ttk
from controller import Controller
from shipment_page import ShipmentPage
from route_page import RoutePage
from report_page import ReportPage
from literals import GUI_TITLE, SIDEBAR_FONT

class Interface():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry('1000x600')
        self.root.resizable(width=False, height= False)
        self.root.title(GUI_TITLE)
        self.__sidebar()
        self.home_page()
        self.root.mainloop()
        pass

    def __sidebar(self) -> None:
        self.sidebar_menu = tk.Frame(master=self.root, bg= '#4390E8', name= "sidebar")
        self.sidebar_menu.pack(side=tk.LEFT, fill= "y")
        self.sidebar_menu.pack_propagate(False)
        self.sidebar_menu.configure(width=200, height=600)
        btn_style = ttk.Style()
        btn_style.configure('W.TButton', font = SIDEBAR_FONT, foreground = '#06075B')
        btn_route = ttk.Button(self.sidebar_menu, command= lambda:self.raise_page(self.route_page), text='Calcular Rota', style= 'W.TButton', width=20)
        btn_route.pack(pady= 10)
        btn_new_shipment = ttk.Button(self.sidebar_menu, command= lambda:self.raise_page(self.shipment_page), text='Cadastrar Transporte', style= 'W.TButton', width=20)
        btn_new_shipment.pack(pady= 10)
        btn_report = ttk.Button(self.sidebar_menu, command= lambda:self.raise_page(self.report_page), text='Acessar Relatórios', style= 'W.TButton', width=20)
        btn_report.pack(pady= 10)
        btn_quit = ttk.Button(self.sidebar_menu, command= self.quit, text='Sair', style= 'W.TButton', width=20)
        btn_quit.pack(pady= 10)
    
    def home_page(self) -> None:
        self.home_frame = tk.Frame(master= self.root, bg = '#BFD6E8')
        self.home_frame.pack(side=tk.LEFT,fill= "y")
        self.home_frame.pack_propagate(False)
        self.home_frame.configure(width=800, height=600)
        btn_home = ttk.Label(self.home_frame, text='Pagina Inicial', style= "W.TButton")
        btn_home.pack(fill= "x" )
    
    def route_page(self) -> None:
        self.new_route_page = RoutePage(self.root)

    def shipment_page(self) -> None:
        self.new_shipment_page = ShipmentPage(self.root)
    
    def report_page(self) -> None:
        self.new_report_page = ReportPage(self.root)

    def __clean_frames(self):
        for frame in self.root.winfo_children():
            if frame.winfo_name() != "sidebar":
                frame.destroy()

    def quit(self):
        self.root.destroy()

    def raise_page(self, page_name):
        self.__clean_frames()
        page_name()

    def select_test(self, text):
        print(text)

    