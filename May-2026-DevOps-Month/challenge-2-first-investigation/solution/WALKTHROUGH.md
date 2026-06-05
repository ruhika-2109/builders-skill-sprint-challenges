# Solution — Challenge 2: First Investigation

> Try it yourself first!

## The break
The Lambda's code is:
```python
def handler(event, context):
    return {"result": config["value"]}   # 'config' was never defined
```
`config` doesn't exist, so every run raises a **NameError** and the function fails. That drives the `Errors` metric and turns the `challenge2-broken-fn-errors` alarm red.

## What the agent should say
Something like: *"`challenge2-broken-fn` is throwing a NameError — `config` is not defined — on every invocation."* It may suggest defining `config` or removing that line.

### ✅ Verified real output (from a live run)
On a real deploy, the agent returned exactly this kind of result:

> **Root Cause Identified 🔴** — The Lambda function `challenge2-broken-fn` is failing due to a code bug — an undefined `config` variable. Every invocation crashes immediately with:
> ```
> NameError: name 'config' is not defined
>   File "/var/task/index.py", line 4, in handler
>     return {"result": config["value"]}
> ```
> - **Error rate:** 100% — all invocations failed
> - **Region:** us-east-1 · **Runtime:** Python 3.12
> - **Timeout/Memory:** 10s / 128 MB — not the issue
> - It also offered fix options and **flagged that the function was deployed by the root user** as a security best-practice violation.

That security note is a nice bonus — it shows the agent doing proactive prevention, not just root cause.

## The fix (bonus)
In the Lambda **Code** tab, replace the handler with:
```python
def handler(event, context):
    return {"result": "ok"}
```
Click **Deploy**, then **Test** — it succeeds, and the alarm goes back to green.

## Why this is the easiest "real" incident
The failure is **100% deterministic** (it fails the same way every time) and the root cause is one obvious line of code. Perfect for seeing how the agent investigates without any complicated setup.

## Cleanup
CloudFormation → `challenge-2` → **Delete**.
