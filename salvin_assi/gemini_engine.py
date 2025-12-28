from google import genai
import time

class GeminiEngine:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model="gemini-1.5-flash",
                contents=prompt,
                generation_config={
                    "max_output_tokens": 512,
                    "temperature": 0.6
                }
            )
            return response.text.strip()

        except Exception as e:
            error_msg = str(e)

            if "429" in error_msg:
                time.sleep(2)  
                return "⚠️ SALVIN is currently busy. Please wait a moment and try again."

            return f"⚠️ Gemini Error: {error_msg}"
