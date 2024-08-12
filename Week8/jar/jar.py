class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity
        self.piece = 0


    def __str__(self):
        return "🍪" * self.piece

    def deposit(self, n):

        if self.piece + n > self._capacity:
            raise ValueError("Jar is full")
        self.piece += n

    def withdraw(self, n):
        if self.piece - n < 0:
            raise ValueError("No enough cookies")
        self.piece -= n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self.piece

def main():
    jar = Jar()
    jar.deposit(50)
    print(jar)


if __name__ == "__main__":
    main()
