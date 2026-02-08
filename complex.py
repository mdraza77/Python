class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):  # Dunder function (Double Underscore) __add__
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):  # Dunder function (Double Underscore) __sub__
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


cmp1 = Complex(5, 3)
cmp1.showNumber()

cmp2 = Complex(4, 4)
cmp2.showNumber()

# cmp3 = cmp1.add(cmp2)
cmp3 = cmp1 + cmp2  # Dunder function (Double Underscore) used
cmp3.showNumber()
