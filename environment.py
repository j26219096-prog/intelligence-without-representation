import random

class Environment:
    def __init__(self):
        self.reset()

    def reset(self):
        self.agent_pos = random.randint(0, 9)
        self.goal = random.randint(0, 9)
        return abs(self.goal - self.agent_pos)

    def step(self, action):
        self.agent_pos = max(0, min(9, self.agent_pos + action))
        distance = abs(self.goal - self.agent_pos)

        reward = 10 if distance == 0 else -1
        done = distance == 0

        return distance, reward, done
