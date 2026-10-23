from google.genai import types

from src.config.ai_config import get_gemini_client, MODEL_NAME
from src.ai.prompt_rules import SYSTEM_RULES, build_landing_prompt


class ia_controller:
    def __init__(self):
        self.client = None
        self.init_error = None

        # Si falta la API Key, el servidor sigue funcionando sin la IA
        try:
            self.client = get_gemini_client()
        except ValueError as error:
            self.init_error = str(error)

# Método para generar el texto de la landing con Gemini
    def generate_landing(self, product_name, main_benefit, price):
        if self.client is None:
            return {"status": "ERROR", "data": self.init_error}

        prompt = build_landing_prompt(product_name, main_benefit, price)

        try:
            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_RULES,
                    thinking_config=types.ThinkingConfig(thinking_level="LOW"),
                ),
            )
            return {"status": "OK", "data": response.text}

        except Exception as error:
            return {"status": "ERROR", "data": str(error)}