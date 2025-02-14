class ProductOfNumbers:

    def __init__(self):
        self.stream = []

    def add(self, num: int) -> None:
        self.stream.append(num)

    def getProduct(self, k: int) -> int:
        p = 1
        a = self.stream[-k:]
        for i in a:
            p *= i
        return p




# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)