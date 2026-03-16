"""
Voice ChatGPT with Whisper & Python
Chatbot por voz usando Whisper (OpenAI) e ChatGPT
Projeto DIO Bradesco GenAI & Dados
Autor: Gabriel Demetrios Lafis
"""

import os
import sys
import logging
from dotenv import load_dotenv

from config import Config
from speech_to_text import SpeechToText
from chatgpt_handler import ChatGPTHandler
from text_to_speech import TextToSpeech

# Configuracao de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Carregar variaveis de ambiente
load_dotenv()


def main():
    """Funcao principal do chatbot por voz."""
    print("="*60)
    print("  Voice ChatGPT - Chatbot por Voz com Whisper & Python")
    print("  Projeto DIO Bradesco GenAI & Dados")
    print("="*60)
    print()

    # Verificar API Key
    config = Config()
    if not config.openai_api_key:
        logger.error("OPENAI_API_KEY nao encontrada. Configure o arquivo .env")
        sys.exit(1)

    # Inicializar modulos
    stt = SpeechToText(config)
    chat = ChatGPTHandler(config)
    tts = TextToSpeech(config)

    print("Chatbot iniciado! Fale algo ou digite 'sair' para encerrar.")
    print("-" * 60)

    conversation_history = []

    while True:
        try:
            # Capturar audio do microfone
            print("\nAguardando sua voz...")
            user_text = stt.listen_and_transcribe()

            if not user_text:
                print("Nao consegui entender. Tente novamente.")
                continue

            if user_text.lower() in ['sair', 'exit', 'quit', 'encerrar']:
                print("\nEncerrando chatbot. Ate mais!")
                break

            print(f"Voce disse: {user_text}")

            # Enviar para ChatGPT
            response = chat.get_response(user_text, conversation_history)
            print(f"ChatGPT: {response}")

            # Atualizar historico
            conversation_history.append({"role": "user", "content": user_text})
            conversation_history.append({"role": "assistant", "content": response})

            # Converter resposta em voz
            tts.speak(response)

        except KeyboardInterrupt:
            print("\nEncerrando chatbot. Ate mais!")
            break
        except Exception as e:
            logger.error(f"Erro: {e}")
            print(f"Ocorreu um erro: {e}")
            continue


if __name__ == "__main__":
    main()
