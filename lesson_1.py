"""Абстракция"""



# class vehicle:
#     def start_engine(self):
#         pass
    
#     def stop_engine(self):
#         pass
    
#     def drive(self):
#         pass
    
# class car(vehicle):
#     def start_engine(self):
#         return 'Двигатель заведен'
    
#     def stop_engine(self):
#         return 'Двигатель автомобиля не завелен'
    
#     def drive(self):
#         return 'Автомобиль едет'
    
# class bycycle(vehicle):
#     def start_engine(self):
#         return 'Велик НЕ поехал потому что нет двигателя'
    
#     def stop_engine(self):
#         return 'Велик НЕ заглушился потому что нет двигателя'
    
#     def drive(self):
# #         return 'Велик едет'

# class Employee:
    
#     def __init__(self, zp, name):
        
#         self.zp = zp    
#         self.name = name
        


#     def calculate_salary():
#         return 0
    
#     def display_info():
#         return 'f{self.name}, есть {self.zp}'

# class FullTimeEmployee(Employee):
#     def calculate_salary(self):
#         return self.zp * 1.2
    
    
    
    
    
# class PartTimeEmployee(Employee):
#     def __init__(self, zp, name, hours_worked):
#         self.hours_worked = hours_worked
#         super().__init__(name, zp)
            
            
#     def calculate_salary(self):
#         return self.zp * 0.5 * self.hours_worked
    
#     def process_salary(Employee):
#         Employee.display_info()
#         salary  = Employee.calculate_salary()
#         return 'f Зарплата - {self.zp}'
    
# time_1 = Employee('30000' 'sASHA ' '4 hours')
# time_2 = Employee('50000' 'Genna ' '12')


# time_1.display_info()
# time_2.display_info()




class Employee:
    def __init__(self, zp, name):
        self.zp = zp
        self.name = name

    def calculate_salary(self):
        return 0

    def display_info(self):
        return f'{self.name}, зарплата: {self.zp}'


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.zp * 1.2


class PartTimeEmployee(Employee):
    def __init__(self, zp, name, hours_worked):
        self.hours_worked = hours_worked
        super().__init__(zp, name)

    def calculate_salary(self):
        return self.zp * 0.5 * self.hours_worked

    def display_info(self):
        return f'{self.name}, зарплата: {self.calculate_salary()}'


Time1 = FullTimeEmployee(30000, 'Sasha')
Time2 = PartTimeEmployee(50000, 'Genna', 12)

print(Time1.display_info())


print(Time2.display_info())


