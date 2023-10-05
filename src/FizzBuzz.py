class FizzBuzz:
    def __init__(self):
        pass
    def convert(self, num: int) -> str:
        if (num % 3 == 0) and (num % 5 == 0):
            return "FizzBuzz"
        if num % 3 == 0:
            return "Fizz"
        if num % 5 == 0:
            return "Buzz"
        return str(num)
    
    def get_numbers(self, start: int, end: int) -> list:
        return list(range(start, end + 1))
    
    def execute(self, start: int, end: int) -> None:
        for i in self.get_numbers(start, end):
            print(self.convert(i))