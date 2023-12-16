import copy
import random

class Hat:
    def __init__(self, **user_input):
        # Initialize the Hat with balls based on user input
        self.contents = []
        for key, value in user_input.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number):
        # Simulate drawing a specified number of balls from the hat
        balls_drawn = []
        
        # If the requested number of balls is greater than or equal to the total number, return all balls
        if number >= len(self.contents):
            return self.contents

        # Randomly draw balls from the hat without replacement
        for i in range(number):
            ball_picked = random.choice(self.contents)
            balls_drawn.append(ball_picked)
            self.contents.pop(self.contents.index(ball_picked))

        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_result = 0

    # Run experiments
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        actual = hat_copy.draw(num_balls_drawn)
        actual_dict = {ball: actual.count(ball) for ball in actual}

        result = True
        # Check if the actual ball counts match the expected counts
        for key, value in expected_balls.items():
            if actual_dict.get(key, 0) < value:
                result = False
                break

        # If the result is True, increment the successful experiment count
        if result:
            num_result += 1

    # Calculate and return the probability of success
    return num_result / num_experiments