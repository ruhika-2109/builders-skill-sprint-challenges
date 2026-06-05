# Challenge 3: Stress & Diagnose ⭐⭐

## Goal
Create a small EC2 server, **max out its CPU** with one command, then ask AWS DevOps Agent to diagnose the slowdown and recommend a fix. This is a *live performance problem*, not a code bug.

## Time
~25 minutes. 💰 EC2 costs by the hour — **delete the stack as soon as you finish.**

## Before You Start
Finish [SETUP.md](../SETUP.md).

## Steps

### 1. Create the stack
1. Console search → **CloudFormation** → **Create stack** → **With new resources (standard)**.
   > ⚠️ Pick **"standard"**, NOT "With existing resources (import resources)" — the import option throws a `DeletionPolicy` error.
2. **Choose an existing template** → **Upload a template file** → **Choose file**.
3. Upload this file:
   ```
   May-2026/challenge-3-stress-and-diagnose/template.yaml
   ```
4. **Next** → Stack name: `challenge-3` → **Next** → **Next**.
5. Tick **"I acknowledge… IAM resources"** → **Submit**. Wait for **CREATE_COMPLETE** (~2 min).

### 2. Connect to the server (one click, no passwords)
1. Console search → **EC2** → **Instances** → click `challenge3-stress`.
2. Click **Connect** (top right) → **Session Manager** tab → **Connect**.
3. A black terminal opens in your browser. You're in.
   > Session Manager greyed out? Wait ~1 minute after the stack finishes — the instance needs a moment to register.

### 3. Max out the CPU
Paste this and press Enter. It pins **all CPU cores** to 100% using the built-in `yes` tool (nothing to install):
```bash
for i in $(seq $(nproc)); do yes > /dev/null & done
```
Leave it running. CPU is now at 100%.

> **Stop it later** with: `kill %1 %2 %3 %4 2>/dev/null; pkill yes` — or just close the terminal and delete the stack.

### 4. Ask the agent
1. Open the **DevOps Agent** web app → **Chat**.
2. Ask:
   ```
   My EC2 instance challenge3-stress has high CPU. What is causing it and what should I do?
   ```
3. Read its diagnosis and recommendation (e.g. resize the instance, add Auto Scaling, or reduce load).

## ✅ You're done when…
The agent says the instance is CPU-overloaded and gives a recommendation.

## 📸 Submit
Screenshot the agent's diagnosis → [awsugmdu.in](https://www.awsugmdu.in/).

## Hints
- Alarm not red yet? Wait ~2 minutes — it checks every minute. You can watch it: Console → **CloudWatch** → **Alarms** → `challenge3-high-cpu`.
- To stop the CPU load: run `pkill yes` in the terminal (or just delete the stack).
- Give the agent a head start by mentioning the alarm name `challenge3-high-cpu`.

## Bonus Points
- Stop the load (`pkill yes`) and watch the alarm go back to green — ask the agent to confirm recovery.
- Ask the agent: "how do I stop this from happening again?"

## ⚠️ Cleanup (important — this one costs money)
CloudFormation → `challenge-3` → **Delete**. Then check **EC2 → Instances** shows it terminated. See [COST-AND-CLEANUP.md](../COST-AND-CLEANUP.md).
