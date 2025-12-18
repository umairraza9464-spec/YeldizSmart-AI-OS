"""Lead classification logic for HOT/WARM/COLD quality"""
from datetime import datetime, timedelta
from ai_core.gemini_client import GeminiClient

class LeadClassifier:
    def __init__(self, gemini_client: GeminiClient = None):
        self.gemini = gemini_client

    def classify(self, listing: dict) -> dict:
        """Classify lead into HOT/WARM/COLD with AI help"""
        
        # Get AI classification if available
        ai_result = {}
        if self.gemini:
            try:
                ai_result = self.gemini.classify_listing(listing)
            except:
                pass
        
        # Calculate listing age in hours
        created_at = listing.get('created_at')
        if isinstance(created_at, str):
            created_dt = datetime.fromisoformat(created_at)
        else:
            created_dt = created_at
        
        age_hours = (datetime.now() - created_dt).total_seconds() / 3600 if created_dt else 999
        
        # Determine quality based on rules + AI
        is_owner = ai_result.get('is_owner', True)
        is_dealer = ai_result.get('is_dealer', False)
        
        if is_dealer:
            quality = "COLD"
        elif is_owner and age_hours < 4:
            quality = "HOT"
        elif is_owner and age_hours < 24:
            quality = "WARM"
        else:
            quality = "COLD"
        
        return {
            "quality": quality,
            "confidence": ai_result.get('confidence', 50),
            "reason": ai_result.get('reason', 'Rule-based classification'),
            "is_owner": is_owner,
            "is_dealer": is_dealer,
            "age_hours": age_hours
        }
