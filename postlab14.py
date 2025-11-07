class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159

    def area(self):
        return self.pi * self.radius ** 2

    def perimeter(self):
        return 2 * self.pi * self.radius

r = float(input("Enter radius of circle: "))
c1 = Circle(r)

print("Area of Circle:", c1.area())
print("Perimeter of Circle:", c1.perimeter())

#question 2
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

    def discount(self, percent):
        self.price = self.price - (self.price * percent / 100)

book1 = Book("Python Basics", "John Smith", 500)
book2 = Book("Learn Data Science", "Emma Johnson", 650)

print("Before Discount:")
book1.show()
book2.show()

book1.discount(10)

print("After 10% Discount on Book 1:")
book1.show()