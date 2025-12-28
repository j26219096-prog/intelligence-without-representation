let agent = Math.floor(Math.random() * 10);
let goal = Math.floor(Math.random() * 10);

function step() {
  let action = Math.random() < 0.5 ? -1 : 1;
  agent = Math.max(0, Math.min(9, agent + action));

  let reward = agent === goal ? 10 : -1;

  if (agent === goal) {
    goal = Math.floor(Math.random() * 10);
  }

  document.getElementById("world").innerHTML =
    `🤖 Agent Position: ${agent} <br>
     🎯 Goal Position: ${goal} <br>
     🧠 Reward: ${reward}`;
}
