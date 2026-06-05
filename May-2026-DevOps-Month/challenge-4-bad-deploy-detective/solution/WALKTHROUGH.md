# Solution — Challenge 4: Bad Deploy Detective

> Try it yourself first!

## The break
The app starts healthy (returns `{"status": "ok"}`). You "deploy a bad change" by editing the code to:
```python
version = release["number"]   # 'release' was never defined -> crash
```
Now every request raises a **NameError**, the app errors, and the `challenge4-webapp-errors` alarm goes red.

## What the agent should say
That `challenge4-webapp` began failing **after your recent code change**, and the cause is the undefined `release`. It should suggest reverting/fixing that line.

## The fix
Put the good code back in the Lambda **Code** tab:
```python
import json

def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"status": "ok", "app": "bad-deploy-detective"}),
    }
```
Click **Deploy**, refresh the URL — back to "ok", alarm green.

## The lesson
This is the classic "it worked, I deployed, now it's broken" story. The agent's value is connecting **the incident** to **the change you just made** — and (bonus) you can hand its findings to a coding assistant like Kiro to write the fix.

## Cleanup
CloudFormation → `challenge-4` → **Delete**. This also removes the public URL.
