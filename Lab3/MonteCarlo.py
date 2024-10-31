import numpy as np


class MonteCarlo:
    def __init__(self, x_min: float, x_max: float, y_min: float, y_max: float, n: int, lst_of_functions: list[str]):
        self.n = n
        self.count = 0
        self.ready = 0

        self.shape = [(x_max - x_min), (y_max - y_min)]
        self.space = self.shape[0] * self.shape[1]

        rng = np.random.default_rng()
        self.X = rng.uniform(x_min, x_max, n)
        self.Y = rng.uniform(y_min, y_max, n)

        self.lst_of_functions = lst_of_functions

    def _function(self, x: float, y: float):
        for func in self.lst_of_functions:
            if eval(func):
                self.count += 1

    def _progressbar(self):
        fullness = self.ready / self.n

        filled_up_Length = round(100 * fullness)
        percentage = round(100 * fullness, 1)

        bar = '=' * filled_up_Length + '-' * (100 - filled_up_Length)

        print(f'[{bar}] {percentage}%', flush=True, end='\r')
        if self.ready == self.n:
            print()

    def run(self):
        for x, y in zip(self.X, self.Y):
            self._function(x, y)
            self.ready += 1
            self._progressbar()
        print(f"Needed area: {self.count * self.space / self.n}")
        return self.count * self.space / self.n


if __name__ == "__main__":
    n = int(input("Number of repetitions:\n>>> "))
    # n = 1000
    x_min, x_max, y_min, y_max = map(int, input("Shape (x_min, x_max, y_min, y_max):\n>>> ").split())
    # x_min, x_max, y_min, y_max = 0, 4, 0, 3

    functions = input("Enter functions (Example: x <= 1 and y <= 1, x > 1 and x <= 3 and y <= 3):\n>>> ").split(",")  # x <= 1 and x >= 0 and y <= 1, x > 1 and x <= 3 and y <= 3, x > 3 and x <= 4 and y >= 2 and y <= 3
    # functions = ["x <= 1 and x >= 0 and y <= 1", "x > 1 and x <= 3 and y <= 3", "x > 3 and x <= 4 and y >= 2 and y <= 3"]

    mc = MonteCarlo(x_min, x_max, y_min, y_max, n, functions)
    result = mc.run()
    # print(result)
