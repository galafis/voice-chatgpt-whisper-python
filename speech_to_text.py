"""
Modulo de transcricao de voz para texto usando Whisper (OpenAI).
"""

import logging
import speech_recognition as sr
import openai
import tempfile
import os

logger = logging.getLogger(__name__)


class SpeechToText:
    """Classe para captura e transcricao de audio."""

    def __init__(self, config):
        self.config = config
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        openai.api_key = config.openai_api_key

        # Ajustar para ruido ambiente
        with self.microphone as source:
            logger.info("Calibrando microfone para ruido ambiente...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

    def listen_and_transcribe(self) -> str:
        """Captura audio do microfone e transcreve usando Whisper."""
        try:
            with self.microphone as source:
                logger.info("Ouvindo...")
                audio = self.recognizer.listen(
                    source,
                    timeout=self.config.audio_timeout,
                    phrase_time_limit=self.config.phrase_time_limit
                )

            # Salvar audio temporariamente
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
                tmp.write(audio.get_wav_data())
                tmp_path = tmp.name

            try:
                # Transcrever com Whisper API
                with open(tmp_path, "rb") as audio_file:
                    client = openai.OpenAI(api_key=self.config.openai_api_key)
                    transcript = client.audio.transcriptions.create(
                        model="whisper-1",
                        file=audio_file,
                        language=self.config.language[:2]  # pt
                    )
                return transcript.text.strip()
            finally:
                os.unlink(tmp_path)

        except sr.WaitTimeoutError:
            logger.warning("Timeout: nenhum audio detectado.")
            return None
        except sr.UnknownValueError:
            logger.warning("Audio nao reconhecido.")
            return None
        except Exception as e:
            logger.error(f"Erro na transcricao: {e}")
            return None
