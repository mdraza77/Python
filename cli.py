import fire


class MathTools:
    def add(self, a=5, b=5):
        return int(a) + int(b)

    def substract(self, a=5, b=5):
        return int(a) - int(b)

    def multiply(self, a=5, b=5):
        return int(a) * int(b)

    def divide(self, a=5, b=5):
        return int(a) / int(b)


if __name__ == "__main__":
    fire.Fire(MathTools)
