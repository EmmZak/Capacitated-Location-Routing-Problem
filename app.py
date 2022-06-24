from DataLoader import DataLoader

file_path = "dataset/Instances_Prodhon_LRP/coord20-5-1.dat"

dataset = DataLoader(path=file_path)

print(dataset.nb_customers, dataset.nb_depots) # 20 5

print(dataset)
"""
Dataset: 
path: dataset/Instances_Prodhon_LRP/coord20-5-1.dat 
nb_customers: 20 
nb_depots: 5 
customer_coordinates_list: [(20, 35), (8, 31), (29, 43), (18, 39), (19, 47), (31, 24), (38, 50), (33, 21), (2, 27), (1, 12), (26, 20), (20, 33), (15, 46), (20, 26), (17, 19), (15, 12), (5, 30), (13, 40), (38, 5), (9, 40)] 
depot_coordinates_list: [(6, 7), (19, 44), (37, 23), (35, 6), (5, 8)] 
vehicle_capacity: 70.0 
depot_capacity_list: [140, 140, 140, 140, 140] 
customer_demand_list: [17, 18, 13, 19, 12, 18, 13, 13, 17, 20, 16, 18, 15, 11, 18, 16, 15, 15, 15, 16] 
depot_opening_costs: [10841, 11961, 6091, 7570, 7497] 
route_opening_cost: 1000.0 
is_int: False 
"""