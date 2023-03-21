class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append([position[i], (target-position[i]) / speed[i]])

        stack = []

        for car in sorted(cars):
            while len(stack) and stack[-1][1] <= car[1]:
                stack.pop()

            stack.append(car)

        return len(stack)