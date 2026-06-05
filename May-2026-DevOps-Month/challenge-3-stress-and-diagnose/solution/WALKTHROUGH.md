# Solution — Challenge 3: Stress & Diagnose

> Try it yourself first!

## The "break"
Nothing is misconfigured — you deliberately overload the CPU with a `yes` loop (`for i in $(seq $(nproc)); do yes > /dev/null & done`), which pins every core at 100%. `yes` is built into every Linux, so there's nothing to install. After ~2 minutes the `challenge3-high-cpu` alarm goes red.

## What the agent should say
That the instance `challenge3-stress` has **sustained high CPU**, and a recommendation such as:
- move to a **bigger instance type**,
- add **Auto Scaling** to share the load, or
- **reduce the load** / find the process eating CPU (here, that's the `yes` processes).

## Recovery
Run `pkill yes` in the terminal (or just delete the stack). CPU drops, alarm turns green.

## Why CPU/EC2 is the "medium" step
Unlike Challenge 2's obvious code bug, this is a **performance** problem. The numbers move around, so the agent has to actually *diagnose* load and talk about **capacity** — a different and more realistic skill.

## Cleanup (do this now — EC2 bills hourly)
CloudFormation → `challenge-3` → **Delete**. Confirm the instance is terminated in the EC2 console.
