from flask import Flask, jsonify, render_template
from agent import Agent
from environment import Environment

app = Flask(__name__)
agent = Agent()
env = Environment()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/step")
def step():
    state = abs(env.goal - env.agent_pos)
    action = agent.choose_action(state)
    next_state, reward, done = env.step(action)
    agent.learn(state, action, reward, next_state)

    if done:
        env.reset()

    return jsonify({
        "agent": env.agent_pos,
        "goal": env.goal,
        "reward": reward
    })

if __name__ == "__main__":
    app.run(debug=True)
