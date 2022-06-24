

class DataLoader:

    NB_CUSTOMERS_LINE = 0
    NB_DEPOTS_LINE = 1

    def __init__(self, path):
        self.path = path
        self.nb_customers = 0
        self.nb_depots = 0

        self.customer_coordinates_list = list()
        self.depot_coordinates_list = list()

        self.vehicle_capacity = 0

        self.depot_capacity_list = list()

        self.customer_demand_list = list()

        self.depot_opening_costs = list()

        self.route_opening_cost = 0

        self.__OFFSET = 0

        self.is_int = None

        self._load_dataset()

    def _next_offset(self, n=1):
        self.__OFFSET += n

    def _load_depot_capacities(self, lines: list):
        START = self.__OFFSET
        END = self.__OFFSET + self.nb_depots

        self.depot_capacity_list = lines[START: END]

        self._next_offset(self.nb_depots)

    def _load_depot_coordinates(self, lines: list):
        START = self.__OFFSET
        END = self.__OFFSET + self.nb_depots
        
        for line in lines[START: END]:
            line = line.split(' ')
            #print(line)
            line = list(filter(lambda l: l != '', line))
            #print(line)
            x, y = line[0], line[1]
            #print("x y", x, y)
            self.depot_coordinates_list.append((x, y))

        self._next_offset(self.nb_depots)

    def _load_customer_coordinates(self, lines: list):
        START = self.__OFFSET
        END = self.__OFFSET + self.nb_customers
        
        for line in lines[START: END]:
            line = line.split(' ')
            #print(line)
            line = list(filter(lambda l: l != '', line))
            #print(line)
            x, y = line[0], line[1]
            #print("customer x y", x, y)
            self.customer_coordinates_list.append((x, y))

        self._next_offset(self.nb_customers)

    def _load_customer_demands(self, lines: list):
        START = self.__OFFSET
        END = self.__OFFSET + self.nb_customers
        self.customer_demand_list = lines[START: END]
        
        self._next_offset(self.nb_customers)

    def _load_depot_opening_costs(self, lines: list):
        START = self.__OFFSET
        END = self.__OFFSET + self.nb_depots
        self.depot_opening_costs = lines[START: END]

        self._next_offset(self.nb_depots)

    def _transform_dataset(self, lines):
        lines = list(map(lambda line: line.replace('\t', ' '), lines))
        lines = list(map(lambda line: line.replace('\n', ''), lines))
        lines = list(map(lambda line: line.rstrip(), lines))
        lines = list(map(lambda line: line.lstrip(), lines))
        lines = list(filter(lambda line: line != '', lines))

        return lines

    def _load_dataset(self):
        with open(self.path, "r") as f:
            lines = f.readlines()
            
            lines = self._transform_dataset(lines)

            self.nb_customers = int(lines[self.__OFFSET])
            self._next_offset()

            self.nb_depots = int(lines[self.__OFFSET])
            self._next_offset()

            self._load_depot_coordinates(lines)
            
            self._load_customer_coordinates(lines)

            self.vehicle_capacity = float(lines[self.__OFFSET])
            self._next_offset()

            self._load_depot_capacities(lines)

            self._load_customer_demands(lines)

            self._load_depot_opening_costs(lines)

            self.route_opening_cost = float(lines[self.__OFFSET])
            self._next_offset()

            self.is_int = bool(lines[self.__OFFSET] == '1')

            """
            for (x, y), capacity, cost in zip(self.depot_coordinates_list, self.depot_capacity_list, self.depot_opening_costs):
                d = Depot(float(x), float(y), capacity, cost)
                self.depot_list.append(d)
            
            for (x, y), demand in zip(self.customer_coordinates_list, self.customer_demand_list):
                c = Customer(float(x), float(y), demand)
                self.customer_list.append(c)
            """

    def __repr__(self):
        return f'Dataset: {self.__dict__}'

if __name__ == "__main__":

    d = Dataset(path="")

