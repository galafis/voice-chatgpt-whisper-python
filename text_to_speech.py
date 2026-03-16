"""
Modulo de sintese de voz (Text-to-Speech).
"""

import logging
import os
import tempfile

logger = logging.getLogger(__name__)


class TextToSpeech:
    """Classe para converter texto em voz."""

    def __init__(self, config):
        self.config = config
        self.engine_type = config.tts_engine

        if self.engine_type == "pyttsx3":
            import pyttsx3
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', 180)
            self.engine.setProperty('volume', 0.9)
            # Tentar configurar voz em portugues
            voices = self.engine.getProperty('voices')
            for voice in voices:
                if 'brazil' in voice.name.lower() or 'portuguese' in voice.name.lower():
                    self.engine.setProperty('voice', voice.id)
                    break

    def speak(self, text: str):
        """Converte texto em voz e reproduz."""
        try:
            if self.engine_type == "pyttsx3":
                self._speak_pyttsx3(text)
            elif self.engine_type == "gtts":
                self._speak_gtts(text)
            else:
                logger.warning(f"Engine TTS desconhecida: {self.engine_type}")
        except Exception as e:
            logger.error(f"Erro no TTS: {e}")

    def _speak_pyttsx3(self, text: str):
        """Sintese de voz usando pyttsx3."""
        self.engine.say(text)
        self.engine.runAndWait()

    def _speak_gtts(self, text: str):
        """Sintese de voz usando gTTS."""
        from gtts import gTTS
        import playsound

        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
            tts = gTTS(text=text, lang=self.config.language[:2])
            tts.save(tmp.name)
            playsound.playsound(tmp.name)
            os.unlink(tmp.name)
