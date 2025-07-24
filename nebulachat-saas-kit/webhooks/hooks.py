
import json, requests

def trigger_webhook(event, payload, config):
    if event in config and config[event]["enabled"]:
        cfg = config[event]
        try:
            res = requests.request(
                cfg["method"], cfg["url"],
                headers=cfg.get("headers", {}),
                json=payload
            )
            print("Webhook sent:", res.status_code)
        except Exception as e:
            print("Webhook error:", e)
