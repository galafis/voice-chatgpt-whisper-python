"""
Modulo de integracao com ChatGPT (OpenAI GPT API).
"""

import logging
from openai import OpenAI

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """Voce e um assistente virtual inteligente e amigavel.
Responda de forma clara, concisa e em portugues brasileiro.
Seja util e informativo nas suas respostas."""


class ChatGPTHandler:
    """Classe para interacao com a API do ChatGPT."""

    def __init__(self, config):
        self.config = config
        self.client = OpenAI(api_key=config.openai_api_key)
        self.system_prompt = SYSTEM_PROMPT

    def get_response(self, user_message: str, conversation_history: list = None) -> str:
        """Envia mensagem para o ChatGPT e retorna a resposta."""
        try:
            messages = [{"role": "system", "content": self.system_prompt}]

            # Adicionar historico de conversas
            if conversation_history:
                messages.extend(conversation_history[-10:])  # Ultimas 10 msgs

            messages.append({"role": "user", "content": user_message})

            response = self.client.chat.completions.create(
                model=self.config.gpt_model,
                messages=messages,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            logger.error(f"Erro ao obter resposta do ChatGPT: {e}")
            return "Desculpe, ocorreu um erro ao processar sua pergunta."
