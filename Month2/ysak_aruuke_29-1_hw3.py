class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computation(self):
        print( f'calculations: {self.__cpu * self.__memory - 5}')

    def __str__(self):
        return f'cpu: {self.__cpu}, memory: {self.__memory}'

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory





class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f"Вы звоните с {sim_card_number}, на {call_to_number}")

    def __str__(self):
        return f'sim_cards_list: {self.sim_cards_list}'



class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list, location):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
        self.location = location

    def usp_gps(self, location1, location2):
        print(f"Vash mershrut ot {location1} do {location2}")

    def __str__(self):
        return super(SmartPhone, self).__str__(f"Location: {self.location}") + f"Cpu: {self.cpu}, " \
                                                                               f"Memory: {self.memory}" \
                                                                               f"Sim_card: {self.sim_cards_list}"





Computer1 = Computer(4 , 8)
Phone1 = Phone(["76866768", "7878"])
SmartPhone1 = SmartPhone(4, 8, ["76866768", "7878"], "ot Mederova94 do Ibraimova103" )
SmartPhone2 = SmartPhone(4, 8, ["76866768", "7878"], "ot Mederova94 do Ibraimova103" )
Phone1.call(2, '0995526606')
SmartPhone1.usp_gps("Mederove53", "Shopokova86")








        # super(Computer, self).__init__(cpu, memory)
        # super(Phone, self).__init__(sim_cards_list)









