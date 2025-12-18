"""Google Gemini API wrapper for YeldizSmart AI"""
import base64
from pathlib import Path
from typing import Optional
try:
    import google.generativeai as genai
except ImportError:
    genai = None

class GeminiClient:
    def __init__(self, api_key: str, model: str = "gemini-2.0-flash"):
        if not genai:
            raise ImportError("google-generativeai not installed")
        self.api_key = api_key
        self.model = model
        genai.configure(api_key=api_key)
        self.client = genai.GenerativeModel(model)

    def classify_listing(self, payload: dict) -> dict:
        """Classify listing as owner/dealer + HOT/WARM/COLD"""
        prompt = f"""
        Analyze this vehicle listing carefully:
        Title: {payload.get('title', '')}
        Description: {payload.get('description', '')}
        Price: {payload.get('price', '')}
        Seller: {payload.get('seller', '')}
        Age: {payload.get('listing_age_hours', 0)} hours old
        
        Return ONLY a JSON object (no markdown, no code blocks):
        {{
            "is_owner": true/false,
            "is_dealer": true/false,
            "lead_quality": "HOT"/"WARM"/"COLD",
            "confidence": 0-100,
            "reason": "brief explanation",
            "seller_type": "owner"/"dealer"/"unknown"
        }}
        
        Rules:
        - Dealers mention "showroom", "finance", "warranty", "exchange"
        - Owners provide personal details, single vehicle
        - HOT: Direct owner + <4 hours old + fresh contact possible
        - WARM: Owner + 4-24 hours old
        - COLD: >24 hours OR incomplete info
        """
        
        try:
            response = self.client.generate_content(prompt)
            import json
            text = response.text.strip()
            # Remove markdown code blocks if present
            if text.startswith("```"):
                text = text.split("```")[1]
                if text.startswith("json"):
                    text = text[4:]
            if text.endswith("```"):
                text = text[:-3]
            result = json.loads(text.strip())
            return result
        except Exception as e:
            return {
                "is_owner": False,
                "is_dealer": False,
                "lead_quality": "COLD",
                "confidence": 0,
                "reason": f"Error: {str(e)}",
                "seller_type": "unknown"
            }

    def extract_number_from_description(self, description: str) -> Optional[str]:
        """Extract mobile number from description using Gemini"""
        prompt = f"""
        Extract ONLY the mobile phone number from this text. 
        Return just the 10-digit number without country code or formatting.
        If no valid Indian mobile number found, return "NONE".
        
        Text: {description}
        """
        
        try:
            response = self.client.generate_content(prompt)
            number = response.text.strip()
            if number != "NONE" and len(number) == 10 and number.isdigit():
                return number
            return None
        except:
            return None

    def generate_message_template(self, seller_type: str, listing_type: str) -> str:
        """Generate human-like inquiry message"""
        prompt = f"""
        Generate a SHORT, natural inquiry message in Hindi-English mix (hinglish) 
        for a {listing_type} {seller_type}. Keep it 1-2 lines max.
        
        Examples style:
        - "Bhai, price fixed h? Owner direct bol na"
        - "Kya condition me h? Owner speak karega?"
        - "Kitne mein jyada discount mil sakta hai?"
        
        Return ONLY the message text, nothing else:
        """
        
        try:
            response = self.client.generate_content(prompt)
            return response.text.strip()
        except:
            return "Bhai, are you the owner? Direct contact share kar sakte ho?"

    async def analyze_image_ocr(self, image_path: str) -> dict:
        """Extract registration number from vehicle image using vision"""
        try:
            image_file = Path(image_path)
            if not image_file.exists():
                return {"reg_no": None, "confidence": 0, "error": "File not found"}
            
            # Read and encode image
            with open(image_file, "rb") as f:
                image_data = base64.standard_b64encode(f.read()).decode("utf-8")
            
            # Determine MIME type
            mime_type = "image/jpeg" if image_file.suffix.lower() in ['.jpg', '.jpeg'] else "image/png"
            
            prompt = f"""
            Extract the vehicle registration number (number plate) from this image.
            Format is typically: XX00AB0000 (2 letters, 2 digits, 2 letters, 4 digits)
            
            Return JSON:
            {{
                "reg_no": "extracted_number_or_null",
                "confidence": 0-100,
                "error": "error_message_or_null"
            }}
            """
            
            # Create content with image
            response = self.client.generate_content([
                {"text": prompt},
                {"mime_type": mime_type, "data": image_data}
            ])
            
            import json
            result = json.loads(response.text.strip())
            return result
        except Exception as e:
            return {"reg_no": None, "confidence": 0, "error": str(e)}
