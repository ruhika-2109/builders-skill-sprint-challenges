# Challenge 4: Bad Deploy Detective ⭐⭐

## Goal
You have a tiny web app that works. You'll **"ship a bad deploy"** — edit the code so it crashes — just like a real botched release. Then you let AWS DevOps Agent find what broke and tell you how to fix it.

## Time
~25 minutes. Cheap (one Lambda).

> ℹ️ **Heads up:** this app has a **public URL with no login** so it's easy to open in a browser. That's fine for a throwaway demo — just **delete the stack** when you're done so it isn't left open.

## Before You Start
Finish [SETUP.md](../SETUP.md).

## Steps

### 1. Create the stack
1. Console search → **CloudFormation** → **Create stack** → **With new resources (standard)**.
   > ⚠️ Pick **"standard"**, NOT "With existing resources (import resources)" — the import option throws a `DeletionPolicy` error.
2. **Choose an existing template** → **Upload a template file** → **Choose file** and upload:
   ```
   May-2026/challenge-4-bad-deploy-detective/template.yaml
   ```
3. **Next** → Stack name: `challenge-4` → **Next** → **Next**.
4. Tick **"I acknowledge… IAM resources"** → **Submit**. Wait for **CREATE_COMPLETE**.

### 2. Check it works
1. On the stack's **Outputs** tab, click the **AppUrl** link.
2. Your browser shows `{"status": "ok", ...}`. The app is healthy. 👍

### 3. Ship the "bad deploy"
1. Console search → **Lambda** → open `challenge4-webapp` → **Code** tab.
2. Replace the whole code with this broken version:
   ```python
   import json

   def handler(event, context):
       # BAD DEPLOY: this line crashes the app on every request.
       version = release["number"]
       return {"statusCode": 200, "body": json.dumps({"status": "ok"})}
   ```
3. Click **Deploy**.
4. Refresh the **AppUrl** in your browser a few times — now it errors. You just broke production. 😈

### 4. Let the agent investigate
1. Open the **DevOps Agent** web app → **Chat**.
2. Ask:
   ```
   My app challenge4-webapp just started failing after I deployed a change.
   What broke and how do I fix it?
   ```
3. The agent should point at your **recent change** — the line using `release`, which doesn't exist.

## ✅ You're done when…
The agent identifies that your latest code change broke the app (an undefined `release`) and suggests reverting it.

## 📸 Submit
Screenshot the agent's answer → [awsugmdu.in](https://www.awsugmdu.in/).

## Hints
- App still shows "ok"? Make sure you clicked **Deploy** after editing, then refresh.
- Tell the agent it happened "after I deployed a change" — that nudge helps it focus on the recent edit.

## Bonus Points
- **Fix it like a pro:** put the original good code back, **Deploy**, refresh — the app returns "ok" and the alarm clears.
- Using [Kiro](https://kiro.dev/) or another coding assistant? Paste the agent's findings and let it write the fix for you, then redeploy.

## ⚠️ Cleanup
CloudFormation → `challenge-4` → **Delete** (this also removes the public URL). See [COST-AND-CLEANUP.md](../COST-AND-CLEANUP.md).
