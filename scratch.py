class Duck:
    def __init__(self, name, bill_description, tail_length, leash):
        self.name = name
        self.bill = Bill(bill_description)
        self.tail = Tail(tail_length)
        self.leash = leash
    def about(self):
        print(
            f"\nThis duck has a {self.bill.description} bill, a pretty {self.leash.color} leash, and a {self.tail.length} tail.\n")
class Bill:
    def __init__(self, description):
        self.description = description
class Tail:
    def __init__(self, length):
        self.length = length
class Leash:
    def __init__(self, color):
        self.color = color
my_red_leash = Leash("red")
duck = Duck("Quackers", "wide orange", "long", my_red_leash)
duck_two = Duck("Feathers", "skinny yello", "short", my_red_leash)
duck.about()