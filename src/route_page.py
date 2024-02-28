import tkinter as tk
from tkinter import ttk
from controller import Controller

TRUCK_NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

class RoutePage():
    def __init__(self, parent) -> None:
        self.ct = Controller()
        self.city_list = self.ct.get_city_list()
        self.origin_city: str
        self.small_truck_number:int
        self.medium_truck_number:int
        self.large_truck_number:int
        self.total_distance:int
        self.total_price:float
    
        self.root = tk.Frame(master= parent, bg = '#BFD6E8')
        self.root.pack(side=tk.LEFT,fill= "y")
        self.root.pack_propagate(False)
        self.root.configure(width=800, height=600)
        self.title = ttk.Label(self.root, text='Calcular Rota', style= "W.TButton")
        self.title.pack(fill= "x", padx= 20, pady= 2 )

        self.route_selection_block()
        self.vehicle_selection_block()


    def route_selection_block(self) -> None:
    # Operações de seleção de rota
        self.route_header = tk.Frame(master= self.root)
        self.route_header.pack(fill="x", side= "top", padx= 20, pady= 5)
        self.route_header_label = ttk.Label(self.route_header, text='--Seleção de Origem e Destino--', border= 1)
        self.route_header_label.pack(side= 'top', padx= 20, ipady= 5)    
        self.route_selection_frame = tk.Frame(master= self.root)
        self.route_selection_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
    # origem
        self.origin_label = ttk.Label(self.route_selection_frame, text='Origem:')
        self.origin_label.pack(side= 'left', padx= 10)
        self.origin_entry = tk.StringVar()
        origin_input = ttk.OptionMenu(self.route_selection_frame, self.origin_entry, self.city_list[0], *self.city_list) 
        origin_input.pack(side= 'left', padx= 5)
    # destino
        self.destination_label = ttk.Label(self.route_selection_frame, text='Destino:')
        self.destination_label.pack(side= 'left', padx= 10)
        self.destination_entry = tk.StringVar()
        destination_input = ttk.OptionMenu(self.route_selection_frame, self.destination_entry, self.city_list[0], *self.city_list)        
        destination_input.pack(side= 'left', padx= 5)

    def vehicle_selection_block(self) -> None:
    # Operações de seleção de Veiculos
        self.vehicles_header = tk.Frame(master= self.root)
        self.vehicles_header.pack(fill="x", side= "top", padx= 20, pady= 5)
        self.vehicles_header_label = ttk.Label(self.vehicles_header, text='--Seleção de Veículos--', border= 1)
        self.vehicles_header_label.pack(side= 'top', padx= 20, ipady= 5)    
        self.vehicles_selection_frame = tk.Frame(master= self.root)
        self.vehicles_selection_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
    # small
        self.small_label = ttk.Label(self.vehicles_selection_frame, text='Caminhões Pequenos:')
        self.small_label.pack(side= 'left', padx= 10)
        self.small_entry = tk.StringVar()
        small_input = ttk.OptionMenu(self.vehicles_selection_frame, self.small_entry, TRUCK_NUMBER[0], *TRUCK_NUMBER) 
        small_input.pack(side= 'left', padx= 5)
    # medium
        self.medium_label = ttk.Label(self.vehicles_selection_frame, text='Caminhões Médios:')
        self.medium_label.pack(side= 'left', padx= 10)
        self.medium_entry = tk.StringVar()
        medium_input = ttk.OptionMenu(self.vehicles_selection_frame, self.medium_entry, TRUCK_NUMBER[0], *TRUCK_NUMBER)        
        medium_input.pack(side= 'left', padx= 5)
    # large
        self.large_label = ttk.Label(self.vehicles_selection_frame, text='Caminhões Grandes:')
        self.large_label.pack(side= 'left', padx= 10)
        self.large_entry = tk.StringVar()
        large_input = ttk.OptionMenu(self.vehicles_selection_frame, self.large_entry, TRUCK_NUMBER[0], *TRUCK_NUMBER) 
        large_input.pack(side= 'left', padx= 5)
    #confirm Buttom
        calculate_btn = ttk.Button(self.vehicles_selection_frame, command= self.calculate_route, text="Confirmar")
        calculate_btn.pack(side= 'right', padx= 20)

    def result_block(self) -> None:
        self.result_frame = tk.Frame(master= self.root,)
        self.result_frame.pack(side= 'top', padx= 20, fill = "both", pady = 2)
        self.result_frame_header = tk.Frame(master= self.result_frame)
        self.result_frame_header.pack(side= 'top', padx= 20, fill = "x", pady = 2)
        self.result_header_label = ttk.Label(self.result_frame_header, text='--Sumário do Transporte--', border= 1)
        self.result_header_label.pack(side= 'top', padx= 20, ipady= 5)  
    # Segunda linha
        self.result_body_frame = tk.Frame(master= self.result_frame)
        self.result_body_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
        self.distance_label= ttk.Label(self.result_body_frame, text='Origem:   ' + self.origin, width=50)
        self.distance_label.pack(side= 'left', padx= 60)
        self.price_label = ttk.Label(self.result_body_frame, text='Destino:   ' + self.destinatiom, width=50)
        self.price_label.pack(side= 'left', padx= 60)
    # Terceira linha
        self.result_footer_frame = tk.Frame(master= self.result_frame)
        self.result_footer_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
        self.distance_label= ttk.Label(self.result_footer_frame, text='Distância:   ' + str(self.total_distance), width=20)
        self.distance_label.pack(side= 'left', padx= 50)
        self.price_label = ttk.Label(self.result_footer_frame, text='Preço:   ' + str(self.total_price), width=20)
        self.price_label.pack(side= 'left', padx= 50)
        self.average_price_label = ttk.Label(self.result_footer_frame, text='Preço por km:   ' + str(self.average_price), width=20)
        self.average_price_label.pack(side= 'left', padx= 50)

    
    def calculate_route(self) -> None:
        self.origin = str(self.origin_entry.get())
        self.destinatiom = str(self.destination_entry.get())
        small_truck = int(self.small_entry.get())
        medium_truck = int(self.medium_entry.get())
        large_truck = int(self.large_entry.get())
        self.total_distance = self.ct.get_distance(self.origin, self.destinatiom)
        self.total_price = self.ct.get_total_price(self.total_distance, small_truck, medium_truck, large_truck)
        self.average_price = (self.total_price/self.total_distance)
        for frame in self.root.winfo_children():
            frame.destroy()
        self.route_selection_block()
        self.vehicle_selection_block()
        self.result_block()
    



    def update_vehicles_values(self, small:tk.StringVar, medium:tk.StringVar, large:tk.StringVar) -> None:
        self.small_truck_number = int(small.get())
        self.medium_truck_number = int(medium.get())
        self.large_truck_number = int(large.get())