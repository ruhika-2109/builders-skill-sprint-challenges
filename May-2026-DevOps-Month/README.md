# 🤖 Builders Skill Sprint — May 2026

## Meet AWS DevOps Agent (No-Code-Required Edition)

Welcome! In this hands-on set you'll try **AWS DevOps Agent** — an AI teammate that looks at your AWS resources, finds what's wrong, and tells you how to fix it. **No CDK, no command line, no coding needed.** You upload one small file in the AWS Console, make something break on purpose, then just **ask the agent in plain English** what happened.

> ⚠️ **AWS DevOps Agent is a paid service** (with a 2-month free trial — *not* free-tier). Read [COST-AND-CLEANUP.md](COST-AND-CLEANUP.md) **before you start** and delete your stacks when done.

---

## 🎯 Challenges

| # | Challenge | What you do | Difficulty |
|---|-----------|-------------|-----------|
| 1 | **Meet Your Agent** | Create the agent and chat with it | ⭐ Easy |
| 2 | **First Investigation** | Break a tiny Lambda, ask the agent why | ⭐ Easy |
| 3 | **Stress & Diagnose** | Max out an EC2 server, ask the agent | ⭐⭐ Medium |
| 4 | **Bad Deploy Detective** | Break a web app, let the agent find the fix | ⭐⭐ Medium |
| 5 | **Build Your Own** | Invent your own break-and-investigate | 🚀 Innovate |

Every challenge is **point-and-click in the AWS Console**. The hardest thing you'll type is a question to the agent.

---

## 📋 What You Need

- An **AWS account** with **AWS DevOps Agent** turned on (start the free trial)
- A web browser — that's it
- About **20–30 minutes** per challenge

No CDK. No SAM. No CLI. No GitHub setup. Just the AWS Console.

---

## 🚀 Start Here

1. Read **[SETUP.md](SETUP.md)** once — it shows how to turn on the agent (5 minutes).
2. Do the challenges in order (1 → 5). Each folder has a `README.md` with step-by-step clicks.
3. Stuck? Each challenge has a `solution/` folder — peek only after you've tried.

---

## 📁 Folder Structure

```
May-2026/
├── README.md                   ← You are here
├── SETUP.md                    ← Turn on the agent (do this first)
├── COST-AND-CLEANUP.md         ← How to avoid charges (read it!)
├── challenge-1-meet-your-agent/
├── challenge-2-first-investigation/
├── challenge-3-stress-and-diagnose/
├── challenge-4-bad-deploy-detective/
└── challenge-5-build-your-own-agentic-sre/
```

Each challenge folder has:
- `README.md` — the steps
- `template.yaml` — the file you upload in the console (challenges **2–4**; challenge 1 is chat-only, challenge 5 is build-your-own)
- `solution/` — the answer, for when you're done or stuck

---

## 🏆 Scoring

| # | Challenge | Difficulty | Points |
|---|-----------|------------|--------|
| 1 | Meet Your Agent | ⭐ | 10 |
| 2 | First Investigation | ⭐ | 20 |
| 3 | Stress & Diagnose | ⭐⭐ | 20 |
| 4 | Bad Deploy Detective | ⭐⭐ | 30 |
| 5 | Build Your Own | 🚀 | 🏆 Best one gets a shoutout! |

---

## 📝 How to Submit

1. Finish a challenge (the agent tells you the root cause).
2. Take a **screenshot** of the agent's answer.
3. Submit at [https://www.awsugmdu.in/](https://www.awsugmdu.in/) — say which challenge.

---

## 💡 Tips

- Start with Challenge 1 — it proves your free trial works before you spend anything.
- Always **delete your stack** after each challenge (one button in CloudFormation).
- The agent understands plain English — just ask it like you'd ask a coworker.

---

## 🔗 Resources

- [AWS DevOps Agent product page](https://aws.amazon.com/devops-agent/) — features + free trial
- [About AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html)
- [Getting Started](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent.html)

---

Happy investigating! 🚀
