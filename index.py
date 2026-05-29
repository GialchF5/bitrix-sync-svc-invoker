import json
import os
import urllib.request


def handler(event, context):
    url = os.environ["CONTAINER_URL"].rstrip("/")
    token = os.environ.get("RUN_TOKEN", "")
    headers = {
        "X-Ycf-Container-Integration-Type": "async",
    }
    if token:
        headers["X-Run-Token"] = token

    req = urllib.request.Request(url, method="GET", headers=headers)

    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            status = resp.getcode()
    except Exception as e:
        return {"ok": False, "error": str(e)}

    return {"ok": True, "status": status}
