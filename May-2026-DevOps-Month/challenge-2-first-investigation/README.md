# Challenge 2: First Investigation ⭐

## Goal
Create a tiny Lambda function that's **broken on purpose**, run it so it fails, then ask AWS DevOps Agent **"why is this failing?"** and read its answer. Your first real investigation.

## Time
~20 minutes. Cheap (one small Lambda).

## Before You Start
Finish [SETUP.md](../SETUP.md). You'll upload one file — no coding, no command line.

## Steps

### 1. Create the stack (upload the file)
1. In the Console search bar, type **CloudFormation** and open it.
2. Click **Create stack** → choose **With new resources (standard)**.
   > ⚠️ **Pick "standard", NOT "With existing resources (import resources)".** The import option causes a `DeletionPolicy` / "Cannot execute a change set" error.
3. Under **Prepare template**, choose **Choose an existing template**.
4. Under **Template source**, choose **Upload a template file** → **Choose file** and upload:
   ```
   May-2026/challenge-2-first-investigation/template.yaml
   ```
5. Click **Next**. Name the stack `challenge-2`. Click **Next**, then **Next** again.
6. Tick the box **"I acknowledge that AWS CloudFormation might create IAM resources"**.
7. Click **Submit**. Wait ~1 minute for **CREATE_COMPLETE**.

### 2. Make it break
1. Search **Lambda** in the Console, open the function `challenge2-broken-fn`.
2. Click the **Test** tab → **Test** button (any event name, defaults are fine).
3. You'll see a red **error** — that's expected! Click Test **2–3 more times** so the alarm notices.

### 3. Ask the agent
1. Open the **DevOps Agent** web app → **Chat**.
2. Ask:
   ```
   The Lambda function challenge2-broken-fn is failing. What is the root cause?
   ```
3. Read its answer. It should point at the **code error** (a `NameError` — the code uses `config` which was never defined).

## ✅ You're done when…
The agent tells you the function is crashing because of an error in the code (an undefined `config`).

## 📸 Submit
Screenshot the agent's root-cause answer → [awsugmdu.in](https://www.awsugmdu.in/).

## Hints
- No answer yet? Run the **Test** a couple more times and wait a minute — the agent needs to see the failures.
- You can also point the agent at the alarm `challenge2-broken-fn-errors`.
- Want to see the error yourself? Lambda → **Monitor** tab → **View CloudWatch logs**.

## Bonus Points
- Fix it yourself: in the Lambda **Code** tab, change the handler to `return {"result": "ok"}`, **Deploy**, Test again — no more error. Ask the agent to confirm it's healthy now.

## ⚠️ Cleanup
CloudFormation → select `challenge-2` → **Delete**. See [COST-AND-CLEANUP.md](../COST-AND-CLEANUP.md).
