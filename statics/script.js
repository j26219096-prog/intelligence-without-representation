async function run() {
    const res = await fetch("/step");
    const data = await res.json();

    document.getElementById("world").innerHTML =
        "🤖 Agent: " + data.agent + " | 🎯 Goal: " + data.goal + " | Reward: " + data.reward;
}
