"""Google Sheets webhook sync for lead updates"""
import requests
import json
from datetime import datetime
from typing import Optional

class SheetsSyncer:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def sync_lead(self, lead: dict) -> bool:
        """Sync single lead to Google Sheets via webhook"""
        payload = {
            "date": lead.get("date", datetime.now().isoformat()),
            "name": lead.get("name", ""),
            "mobile": lead.get("mobile", ""),
            "reg_no": lead.get("reg_no", ""),
            "car_model": lead.get("car_model", ""),
            "variant": lead.get("variant", ""),
            "year": lead.get("year", ""),
            "km": lead.get("km", ""),
            "address": lead.get("address", ""),
            "follow_up": lead.get("follow_up", ""),
            "source": lead.get("source", ""),
            "context": lead.get("context", ""),
            "license": lead.get("license", ""),
            "remark": lead.get("remark", "")
        }
        
        try:
            response = requests.post(self.webhook_url, json=payload, timeout=10)
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Sheet sync error: {e}")
            return False

    def sync_batch(self, leads: list) -> dict:
        """Sync multiple leads"""
        results = {"success": 0, "failed": 0, "errors": []}
        for lead in leads:
            try:
                if self.sync_lead(lead):
                    results["success"] += 1
                else:
                    results["failed"] += 1
            except Exception as e:
                results["failed"] += 1
                results["errors"].append(str(e))
        return results
