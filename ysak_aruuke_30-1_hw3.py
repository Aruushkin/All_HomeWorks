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


    def __eq__(self, other):
        return self.__cpu == other.__cpu

    def __ne__(self, other):
        return self.__cpu != other.__cpu

    def __lt__(self, other):
        return self.__cpu < other.__cpu

    def __le__(self, other):
        return self.__cpu <= other.__cpu

    def __gt__(self, other):
        return self.__cpu > other.__cpu

    def __ge__(self, other):
        return self.__cpu >= other.__cpu




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
        print(f"Идет звонок с симкарты  {sim_card_number}, на {call_to_number}")

    def __str__(self):
        return f'sim_cards_list: {self.sim_cards_list}'



class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list, location):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
        self.location = location

    def usp_gps(self, location1, location2):
        print(f"Ваш маршрут от {location1} до {location2}")

    def __str__(self):
        return super(SmartPhone, self).__str__(f"Location: {self.location}") + f"Cpu: {self.cpu}, " \
                                                                               f"Memory: {self.memory}" \
                                                                               f"Sim_card: {self.sim_cards_list}"





Computer1 = Computer(5 , 5)
print(Computer1)

Phone1 = Phone(["0550300300", "0500634463"])
print(Phone1)

SmartPhone1 = SmartPhone(4, 8, ["05059200395", "0708724563"], "от Ахунбаева до Абдрахманова 99/1" )
SmartPhone2 = SmartPhone(9, 6, ["0996660672", "0555671710"], "от Юнусалиева 48 до Жибек жолу " )

Phone1.call('2-О!', '0708345202')
SmartPhone1.usp_gps("Жукеева-Пудовкина", "Исанова 52")

Computer1.make_computation()





print(Computer1 == SmartPhone1)
print(SmartPhone1 != SmartPhone2)
print(SmartPhone1 < SmartPhone2)
print(SmartPhone2 > Computer1)
print(SmartPhone1 <= SmartPhone2)
print(SmartPhone2 >= Computer1)



