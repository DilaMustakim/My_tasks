"""Oson1. "Oson1" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchi bor.
output_a() - bu funksiya klassdagi "a" ni qiymatini print qilsin."""

class Oson1:
	def __init__(self):
		self.a = 10

	def output_a(self):
		print(self.a)

"""Oson2. "Oson2" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchilari bor.
summa() - bu funksiya klassdagi "a" va "b" ni yig'indisini print qilsin."""

class Oson2:
  def __init__(self):
    self.a = 12
    self.b = 9
  
  def summa(self):
    print(self.a + self.b)

"""Oson3. "Oson3" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchisi bor.
plus_minus() - bu funksiya klassdagi "a" ni musbat yoki manfiy ekanligini print qilsin."""

class Oson3:
  def __init__(self):
    self.a = 32

  def plus_minus(self):
    if self.a >= 0:
      print("Musbat")
    else:
      print("Manfiy")

"""Oson4. "Oson4" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchi bor.
odd_even() - bu funksiya klassdagi "a" ni toq yoki juft ekanligini print qilib bersin."""

class Oson4:
  def __init__(self):
    self.a = 27

  def odd_even(self):
    if self.a % 2==0:
      print("Juft")
    else :
      print("Toq")

"""Oson5. "Oson5" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchisi bor.
daraja() - bu funksiya klassdagi "a" ni "b" chi darajasini print qilsin."""

class Oson5:
  def __init__(self):
    self.a = 2
    self.b = 3
  
  def daraja(self):
    print(self.a**self.b)

"""6. "MyClass8" nomli klass elon qililar. Bu klassdan "numbers" list o'zgaruvchisi bor.
compare_lists(new_list) - bu funksiya klassdagi "numbers" ni elementlar yig'indisi 
"new_list" ni elementlar yig'indisidan katta aniqlab katta listni print qilsin."""

class MyClass8:
  def __init__(self):
    self.numbers = [1,2,3,4,5]

  def compare_lists(self, new_list):
    if len(self.numbers)>len(new_list):
      print(self.numbers)
    elif len(self.numbers)<len(new_list):
      print(new_list)
    else:
      print(self.numbers,'\t',new_list)

""" "MyClass10" nomli klass elon qililar. Bu klass "numbers" list o'zgaruvchilari bor.
divide(d) - bu funksiya klassadagi "numbers" list elementlarini "d" qoldiqsiz bo'linsa bitta list yig'sin funksiyani ichida.
va funksiya oxirida bolinadigonlarni listini return qilsin."""

class MyClass10:
  def __init__(self):
    self.numbers = [1,2,3,4,5]

  def divide(self,d):
    res = []
    for i in self.numbers:
      if d % i == 0:
        res.append(i)
    return res

"""vorisdorlik-1:
    "Texnika" parent klass. Konstruktorida esa (brand, model, type) parametrlari bor.
      info() - (brand, model, type) ni print qilib beradi.

    "Notebooks" child klassi bor. Unda konstruktirida qo'shimcha (video_card, ram, display).
      more_info() - (brand, model, type, video_card, ram, display) ni print qilib beradi.
      
    "Televisions" child klassi bor. Unda konstruktirida (size, display) parametrlari bor.
      more_info() - (brand, model, type, size, display) ni print qilib beradi.
    
    "Smartphones" child klassi bor. Unda konstruktirida (size, sim_count) parametrlari bor.
      more_info() - (brand, model, type, size, sim_count) ni print qilib beradi."""

class Texnika(object):
  def __init__(self,brand,model,type):
    Texnika.brand = brand
    Texnika.model = model
    Texnika.type = type 
  
  def info(self):
    print(f"Brand: {self.brand}  Model: {self.model}  Type: {self.type}")


class Notebooks(Texnika):
  def __init__(self,brand,model,type,video_card,ram,display):
    super().__init__(brand,model,type)
    self.video_card = video_card
    self.ram = ram
    self.display = display

  def more_info(self):
    print(f"Brand: {self.brand}  Model: {self.model}  Type: {self.type}  Video Card: {self.video_card}  Ram: {self.ram}  Display: {self.display}")


class Televisions(Texnika):
  def __init__(self,brand,model,type, size, display):
    super().__init__(brand,model,type)
    self.size = size
    self.display = display

  def more_info(self):
    print(f"Brand: {self.brand}  Model: {self.model}  Type: {self.type}  Size: {self.size}  Display: {self.display}")


class Smartphones(Texnika):
  def __init__(self,brand,model,type, size, sim_count):
    super().__init__(brand,model,type)
    self.size = size
    self.sim_count = sim_count

  def more_info(self):
    print(f"Brand: {self.brand}  Model: {self.model}  Type: {self.type}  Size: {self.size}  Sim_count: {self.sim_count}")

ntbk = Smartphones("Redmi","Note 8","Pro", 115, 200)
ntbk.more_info()

"""vorisdorlik-2 :
  "Transport" parent klass. Konstruktorida esa (brand, model, type) parametrlari bor.
    info() - (brand, model, type) ni print qilib beradi.
    
  "ElentroCars" - child klassi bor. Unda konstruktirida qo'shimcha (battery_life, chargin_time).
    more_info() - (brand, model, type, battery_life, chargin_time) ni print qilib beradi.

  "SportCars" - child klassi bor. Unda konstruktirida qo'shimcha (motor, color).
    more_info() - (brand, model, type, motor, color) ni print qilib beradi.
    
  "Truck" - child klassi bor. Unda konstruktirida qo'shimcha (motor, height, long, wieght).
    more_info() - (brand, model, type, height, long, wieght) ni print qilib beradi."""


class Transport(object):
  def __init__(self,brand,model,type):
    self.brand = brand
    self.model = model
    self.type = type 
  
  def info(self):
    print(f"Brand: {self.brand}  Model: {self.model}  Type: {self.type}")


class ElentroCars(Transport):
  def __init__(self,brand,model,type,battery_life, chargin_time):
    super().__init__(brand,model,type)
    self.chargin_time = chargin_time
    self.battery_life = battery_life

  def more_info(self):
    print(f"Brand: {self.brand}  Model: {self.model}  Type: {self.type}  Chargin time: {self.chargin_time}  Battery life: {self.battery_life} ")


class SportCars(Transport):
  def __init__(self,brand,model,type, motor, color):
    super().__init__(brand,model,type)
    self.motor = motor
    self.color = color

  def more_info(self):
    print(f"Brand: {self.brand}  Model: {self.model}  Type: {self.type}  Motor: {self.motor}  Color: {self.color}")


class Truck(Transport):
  def __init__(self,brand,model,type, motor, height, long, wieght):
    super().__init__(brand,model,type)
    self.motor = motor
    self.height = height
    self.long = long
    self.wieght = wieght

  def more_info(self):
    print(f"Brand: {self.brand}  Model: {self.model}  Type: {self.type}  Wieght: {self.wieght}  Long: {self.long}  Height: {self.height}  Motor: {self.motor}")
