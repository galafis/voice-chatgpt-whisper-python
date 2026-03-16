"""
Modulo de configuracao do projeto.
"""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """Configuracoes do chatbot."""
    openai_api_key: str = None
    whisper_model: str = "base"
    gpt_model: str = "gpt-3.5-turbo"
    language: str = "pt-BR"
    max_tokens: int = 500
    temperature: float = 0.7
    tts_engine: str = "pyttsx3"  # pyttsx3 ou gtts
    audio_timeout: int = 5
    phrase_time_limit: int = 15

    def __post_init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY", self.openai_api_key)
        self.whisper_model = os.getenv("WHISPER_MODEL", self.whisper_model)
        self.gpt_model = os.getenv("GPT_MODEL", self.gpt_model)
        self.language = os.getenv("LANGUAGE", self.language)
        self.tts_engine = os.getenv("TTS_ENGINE", self.tts_engine)
