import tkinter as tk
from tkinter import ttk
from controller import Controller

TRUCK_NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

class ShipmentPage():
    def __init__(self, parent) -> None:
        self.ct = Controller()
        self.city_list = self.ct.get_city_list()
        self.destinations_frames:tk.Frame = []
        self.product_frames = []
        self.route_list = []
        self.origin_city: str
        self.small_truck_number:int
        self.medium_truck_number:int
        self.large_truck_number:int
        self.manifest = []
        self.total_weight:float
        self.total_distance:int
        self.transport_distribution:dict
        self.total_price:float

        self.root = tk.Frame(master= parent, bg = '#BFD6E8')
        self.root.pack(side=tk.LEFT,fill= "y")
        self.root.pack_propagate(False)
        self.root.configure(width=800, height=600)
        self.title = ttk.Label(self.root, text='Novo Transporte', style= "W.TButton")
        self.title.pack(fill= "x", padx= 20, pady= 2 )

        self.product_inclusion_block()

    def product_inclusion_block(self) -> None:
    # Operações de inclusão de produtos    
        self.product_input_header = tk.Frame(self.root,)
        self.product_input_header.pack(side= 'top', padx= 20, fill = "x", pady = 2)
        self.product_header_label = ttk.Label(self.product_input_header, text= "--Adicionar Produto: só são aceitos produtos inéditos, entradas inválidas serão desconsideradas--")
        self.product_header_label.pack(side= 'top', padx= 20, pady= 2)
        self.product_input_frame = tk.Frame(self.root)
        self.product_input_frame.pack(side= 'top', padx= 20, fill = "x", pady= 2)

        name_entry_label = ttk.Label(self.product_input_frame, text= "Nome do Produto:" )
        quant_entry_label = ttk.Label(self.product_input_frame, text= "Número de unidades:" )
        weight_entry_label = ttk.Label(self.product_input_frame, text= "Peso por unidade[kg]:" )
        self.name_entry = ttk.Entry(self.product_input_frame)
        self.quant_entry = ttk.Entry(self.product_input_frame, width= 5)
        self.weight_entry = ttk.Entry(self.product_input_frame, width= 5)
        name_entry_label.pack(side= 'left', padx= 5)
        self.name_entry.pack(side= 'left', padx= 5)
        quant_entry_label.pack(side= 'left', padx= 5)
        self.quant_entry.pack(side= 'left', padx= 5)
        weight_entry_label.pack(side= 'left', padx= 5)
        self.weight_entry.pack(side= 'left', padx= 5)
    # Botão de confirmação
        product_confirm_btn = ttk.Button(self.product_input_frame, command=lambda: self.add_product_frame(self.name_entry.get(), self.quant_entry.get(), self.weight_entry.get()), text="Confirmar")
        product_confirm_btn.pack(side= 'right', padx= 20)
        self.product_input_footer = tk.Frame(self.root,)
        self.product_input_footer.pack(side= 'top', padx= 20, fill = "x", pady = 2)
        product_close_button = ttk.Button(self.product_input_footer, command= self.end_product_inclusion, text= "Encerrar inclusão de produtos")
        product_close_button.pack(side= 'top', padx= 20, pady= 2)

    def origin_definition_block(self) -> None:
        # Operações de seleção de origem
        self.origin_frame = tk.Frame(master= self.root)
        self.origin_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
        self.origin_label = ttk.Label(self.origin_frame, text='Cidade de Origem')
        self.origin_label.pack(side= 'left', padx= 10)
    # dropdown
        origin_entry = tk.StringVar()
        city_menu = ttk.OptionMenu(self.origin_frame, origin_entry, self.city_list[0], *self.city_list)
        city_menu.pack(side= 'left', padx= 50)
    #confirm Buttom
        origin_confirm_btn = ttk.Button(self.origin_frame, command=lambda: self.add_origin_frame(origin_entry), text="Confirmar")
        origin_confirm_btn.pack(side= 'right', padx= 20)

    def destinations_block(self) -> None:
    # Operações de inclusão de destinos
        self.destinations_input_header = tk.Frame(self.root,)
        self.destinations_input_header.pack(side= 'top', padx= 20, fill = "x", pady = 2)
        self.destinations_header_label = ttk.Label(self.destinations_input_header, text= "--Adicionar Destino--")
        self.destinations_header_label.pack(side= 'top', padx= 20, pady= 2)
        self.destinations_input_frame = tk.Frame(self.root)
        self.destinations_input_frame.pack(side= 'top', padx= 20, fill = "x", pady= 2)
    # dropdowns
        self.delivered_product:str
        new_destinations_entry = tk.StringVar()
        self.new_product_entry = tk.StringVar()
        city_label = ttk.Label(self.destinations_input_frame, text= "Cidade:")
        product_label = ttk.Label(self.destinations_input_frame, text= "Entrega de:" )
        quantity_label = ttk.Label(self.destinations_input_frame, text= "Qnt:" )
        destinations_menu = ttk.OptionMenu(self.destinations_input_frame, new_destinations_entry, self.city_list[0], *self.city_list)
        item_menu = ttk.OptionMenu(self.destinations_input_frame, self.new_product_entry,self.manifest[0], *self.manifest, command= self.update_new_product_entry)
        self.quant_entry = ttk.Entry(self.destinations_input_frame, width= 5, )
        self.quant_entry.insert(0, "0")
        city_label.pack(side= 'left', padx= 2)
        destinations_menu.pack(side= 'left', padx= 5)
        product_label.pack(side= 'left', padx= 2)
        item_menu.pack(side= 'left', padx= 5)
        quantity_label.pack(side= 'left', padx= 2)
        self.quant_entry.pack(side= 'left', padx= 5)
    # Botão de confirmação
        destinations_confirm_btn = ttk.Button(self.destinations_input_frame, command=lambda: self.add_destination_frame(new_destinations_entry.get(), self.new_product_entry.get(), self.quant_entry.get()), text="Confirmar")
        destinations_confirm_btn.pack(side= 'right', padx= 20)
    #botão para encerrar inclusão
        self.destinations_input_footer = tk.Frame(self.root,)
        self.destinations_input_footer.pack(side= 'top', padx= 20, fill = "x", pady = 2)
        self.destinations_end_btn = ttk.Button(self.destinations_input_footer,command= self.end_destinations_inclusion, text= "Encerrar inclusão de destinos")
        self.destinations_end_btn.pack(side= 'top', padx= 20, pady= 2)

    def summary_block(self) -> None:
        self.complete_calculations()
        self.sumary_frame = tk.Frame(master= self.root,)
        self.sumary_frame.pack(side= 'top', padx= 20, fill = "both", pady = 2)
        self.sumary_frame_header = tk.Frame(master= self.sumary_frame)
        self.sumary_frame_header.pack(side= 'top', padx= 20, fill = "x", pady = 2)
        self.sumary_header_label = ttk.Label(self.sumary_frame_header, text='--Sumário do Transporte--', border= 1)
        self.sumary_header_label.pack(side= 'top', padx= 20, ipady= 5)  
    # Segunda linha 
        self.sumary_body_frame = tk.Frame(master= self.sumary_frame)
        self.sumary_body_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
        self.small_label = ttk.Label(self.sumary_body_frame, text='Caminhões Pequenos:   ' + str(self.transport_distribution["small"]))
        self.small_label.pack(side= 'left', padx= 5)
        self.medium_label = ttk.Label(self.sumary_body_frame, text='Caminhões Médios:   ' + str(self.transport_distribution["medium"]))
        self.medium_label.pack(side= 'left', padx= 5)
        self.large_label = ttk.Label(self.sumary_body_frame, text='Caminhões Grandes:   ' + str(self.transport_distribution["large"]))
        self.large_label.pack(side= 'left', padx= 5)
        self.weight_label = ttk.Label(self.sumary_body_frame, text='Carga Total[kg]:   ' + str(self.total_weight))
        self.weight_label.pack(side= 'left', padx= 5)
        self.distance_label = ttk.Label(self.sumary_body_frame, text='Distancia Total[km]:   ' + str(self.total_distance))
        self.distance_label.pack(side= 'left', padx= 5)
    # terceira linha
        self.sumary_footer_frame = tk.Frame(master= self.sumary_frame)
        self.sumary_footer_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
        self.price_label = ttk.Label(self.sumary_footer_frame, text='Preço Total:   ' + str(self.total_price))
        self.price_label.pack(padx= 30)
        self.price_average_label = ttk.Label(self.sumary_footer_frame, text='Preço Médio por item:   ' + str(self.price_per_item))
        self.price_average_label.pack(padx= 30)
    # encerrar interação
        self.sumary_btn_frame = tk.Frame(master= self.sumary_frame)
        self.sumary_btn_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
        self.sumary_accept_btn = ttk.Button(master= self.sumary_btn_frame, command= self.accept_shipment, text="Aceitar Transporte")
        self.sumary_accept_btn.pack(fill="x", side= "top", padx= 20, pady= 2)
        self.sumary_refusal_btn = ttk.Button(master= self.sumary_btn_frame, command= self.refuse_shipment, text="Rejeitar Transporte")
        self.sumary_refusal_btn.pack(fill="x", side= "top", padx= 20, pady= 2)
    

    def add_product_frame(self, name, quant, weight) -> None:
        new_name = str(name)
        new_quant = int(quant)
        new_weight = float(weight)

        self.name_entry.delete(0, 50)
        self.quant_entry.delete(0, 50)
        self.weight_entry.delete(0, 50)

        if new_quant <= 0 or new_weight <= 0:
            pass
        elif new_name in self.manifest:
            pass
        else:
            self.ct.add_item(new_name, weight=new_weight, quantity=new_quant)
            self.manifest = self.ct.get_names_manifest()
            prod_frame = tk.Frame(self.root)
            prod_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
            name_label = ttk.Label(prod_frame, text= ("Nome do Produto: " + new_name) )
            quant_label = ttk.Label(prod_frame, text= ("Número de Unidades: " + str(new_quant)))
            weight_label = ttk.Label(prod_frame, text= ("Peso Unitário: " + str(new_weight) + "kg"))
            name_label.pack(side= 'left', padx= 2)
            quant_label.pack(side= 'left', padx= 2)
            weight_label.pack(side= 'left', padx= 2)
            self.product_frames.append(prod_frame)

    def end_product_inclusion(self):
        if len(self.product_frames) > 0:
            self.product_input_frame.destroy()
            self.product_input_header.destroy()
            self.product_input_footer.destroy()
            for frame in self.product_frames:
                frame.destroy()
            self.truck_distribution_frame()
            self.origin_definition_block()
            

    def end_origin_inclusion(self):
        if len(self.route_list) != 0:
            self.origin_frame.destroy()
            self.destinations_block()

    def end_destinations_inclusion(self) -> None:
        if len(self.destinations_frames) != 0 and self.total_distance > 0:
            self.destinations_input_header.destroy()
            self.destinations_input_frame.destroy()
            self.destinations_input_footer.destroy()
            self.vehicles_header.destroy()
            self.vehicles_selection_frame.destroy()
            for frame in self.destinations_frames:
                frame.destroy()
            self.summary_block()

    # def update_origin(self, origin:tk.StringVar) -> None:
    #     self.origin_city = origin.get()
    #     print(self.origin_city)

    def update_vehicles_values(self, small:tk.StringVar, medium:tk.StringVar, large:tk.StringVar) -> None:
        self.small_truck_number = int(small.get())
        self.medium_truck_number = int(medium.get())
        self.large_truck_number = int(large.get())
    
    def add_destination_frame(self, city:str, product:str, product_quantity:float): #Gera o frame de inclusão de um destino e aciona o controller
        if float(product_quantity) < 0 :
            pass
        else:
            str(city)
            str(product)
            str(product_quantity)
            distance =  self.ct.get_distance(city1=city, city2=self.route_list[-1])
            if city != self.route_list[-1]:
                self.route_list.append(city)
                self.ct.add_destination(city=city)
            self.total_distance = self.ct.get_total_distance()
            index = len(self.destinations_frames)
            dest_frame = tk.Frame(self.root)
            dest_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
            num_label = ttk.Label(dest_frame, text= str(index))
            city_label = ttk.Label(dest_frame, text= ("Cidade: " + city))
            dist_label = ttk.Label(dest_frame, text= ("Distância: " + str(distance) + "km"))
            total_dist_label = ttk.Label(dest_frame, text= ("Distância Total: " + str(self.total_distance) + "km"))
            product_label = ttk.Label(dest_frame, text=("Entrega - " + product + " - " + product_quantity + " un"))
            num_label.pack(side= 'left', padx= 2)
            city_label.pack(side= 'left', padx= 2)
            dist_label.pack(side= 'left', padx= 2)
            total_dist_label.pack(side= 'left', padx= 2)
            product_label.pack(side= 'right', padx= 2)
            self.destinations_frames.append(dest_frame)

    def add_origin_frame(self, city:tk.StringVar): #Gera o frame de inclusão da origem e aciona o controller
        self.origin_city = city.get()
        self.route_list.append(self.origin_city)
        self.ct.set_origin(self.origin_city)
        index = len(self.destinations_frames)
        dest_frame = tk.Frame(self.root)
        dest_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
        num_label = ttk.Label(dest_frame, text= str(index))
        city_label = ttk.Label(dest_frame, text= ("Cidade: " + self.origin_city + "   - ORIGEM"))
        num_label.pack(side= 'left', padx= 2)
        city_label.pack(side= 'left', padx= 2)
        self.destinations_frames.append(dest_frame)
        self.end_origin_inclusion()

    def update_new_product_entry(self): # Usado para permitir a seleção da lista de produtos
        self.delivered_product = self.new_product_entry.get()
        print(self.delivered_product)

    def truck_distribution_frame(self) -> None:
        self.transport_distribution = self.ct.get_best_transport()
        self.total_weight = self.ct.get_total_weight()
    # Operações de seleção de Veiculos
        self.vehicles_header = tk.Frame(master= self.root)
        self.vehicles_header.pack(fill="x", side= "top", padx= 20, pady= 5)
        self.vehicles_header_label = ttk.Label(self.vehicles_header, text='--Seleção de Veículos--', border= 1)
        self.vehicles_header_label.pack(side= 'top', padx= 20, ipady= 5)    
        self.vehicles_selection_frame = tk.Frame(master= self.root)
        self.vehicles_selection_frame.pack(fill="x", side= "top", padx= 20, pady= 2)
    # small
        self.small_label = ttk.Label(self.vehicles_selection_frame, text='Caminhões Pequenos:   ' + str(self.transport_distribution["small"]))
        self.small_label.pack(side= 'left', padx= 10)
    # medium
        self.medium_label = ttk.Label(self.vehicles_selection_frame, text='Caminhões Médios:   ' + str(self.transport_distribution["medium"]))
        self.medium_label.pack(side= 'left', padx= 10)
    # large
        self.large_label = ttk.Label(self.vehicles_selection_frame, text='Caminhões Grandes:   ' + str(self.transport_distribution["large"]))
        self.large_label.pack(side= 'left', padx= 10)
    # weight
        self.weight_label = ttk.Label(self.vehicles_selection_frame, text='Carga Total[kg]:   ' + str(self.total_weight))
        self.weight_label.pack(side= 'left', padx= 10)

    def complete_calculations(self) -> None:
        self.total_price = self.ct._get_total_price()
        self.price_per_item = self.ct.get_price_per_item()
    
    def accept_shipment(self) -> None:
        self.ct.save_shipment()
        self.sumary_frame.destroy()

    def refuse_shipment(self) -> None:
        self.sumary_frame.destroy()
    
    def close_page(self) -> None:
        self.root.destroy()



