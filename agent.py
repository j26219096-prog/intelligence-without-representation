import random

class Agent:
    def __init__(self):
        self.q = {}
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.2

    def get_q(self, state, action):
        return self.q.get((state, action), 0)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice([-1, 1])
        return max([-1, 1], key=lambda a: self.get_q(state, a))

    def learn(self, state, action, reward, next_state):
        old = self.get_q(state, action)
        future = max(self.get_q(next_state, a) for a in [-1, 1])
        self.q[(state, action)] = old + self.alpha * (reward + self.gamma * future - old)
