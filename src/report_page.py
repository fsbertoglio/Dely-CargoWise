import tkinter as tk
from tkinter import ttk
from controller import Controller
from literals import TRUCK_DISTANCE_PRICE

class ReportPage():
    def __init__(self, parent) -> None:
        self.ct = Controller()
        self.city_list = self.ct.get_city_list()
        self.shipment_list = []
    
        self.root = tk.Frame(master= parent, bg = '#BFD6E8')
        self.root.pack(side=tk.LEFT,fill= "y")
        self.root.pack_propagate(False)
        self.root.configure(width=800, height=600)
        self.title = ttk.Label(self.root, text='Reporte de Transportes', style= "W.TButton")
        self.title.pack(fill= "x", padx= 20, pady= 2 )
        self.generate_reports()

    def report_box_block(self, report) -> None:
        self.report_box = tk.Text(self.root, height=10, width= 50)
        self.report_box.pack(fill= "x", padx= 20, pady= 2 )
        self.report_box.insert(tk.END, report)


    def generate_reports(self) -> None:
        self.shipment_list = self.ct.get_shipment_list()
            #Custo por Trecho = {shipment["price_per_hop"]}
        index = 0
        for shipment in self.shipment_list:
            index += 1
            route = shipment["route"]
            total_price = shipment["total_price"]
            report = f"""Número do Transporte = {index}
            Rota e Distâncias = {route}
            Distância Total = {shipment["total_distance"]} km
            Custo Total = {total_price} R$
            Custo Médio por kilômetro = {shipment["average_price+km"]} R$
            Produtos = {shipment["products"]}
            Veiculos por Modalidade =   [Caminhões Pequenos = {shipment["transport_distribution"]["small"]}]
                                        [Caminhões Médios = {shipment["transport_distribution"]["medium"]} ] 
                                        [Caminhões Grandes = {shipment["transport_distribution"]["large"]} ] 
            Custo por Modalidade =      [Caminhões Pequenos = {TRUCK_DISTANCE_PRICE["small"] * shipment["total_distance"]}] R$
                                        [Caminhões Médios = {TRUCK_DISTANCE_PRICE["medium"] * shipment["total_distance"]} ] R$
                                        [Caminhões Grandes = {TRUCK_DISTANCE_PRICE["large"] * shipment["total_distance"]} ] R$
            Número Total de Veículos = {shipment["transport_distribution"]["small"] + shipment["transport_distribution"]["small"] + shipment["transport_distribution"]["small"]} Caminhões
            Número Total de Itens Transportados = {shipment['total_items']} un
            """

            self.report_box_block( report)

