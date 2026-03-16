# Voice ChatGPT with Whisper & Python

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-Whisper%20%26%20GPT-green.svg)](https://openai.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Sobre o Projeto

Chatbot interativo por voz que utiliza **Whisper** (OpenAI) para transcrição de áudio e **ChatGPT** para geração de respostas inteligentes em linguagem natural. Projeto desenvolvido como parte do bootcamp **Bradesco GenAI & Dados** na plataforma **DIO**.

## Arquitetura

```
Usuário (Voz) → Whisper (Speech-to-Text) → ChatGPT (Processamento) → TTS (Text-to-Speech) → Resposta por Voz
```

## Tecnologias Utilizadas

- **Python 3.8+**
- **OpenAI Whisper** - Transcrição de áudio para texto
- **OpenAI GPT API** - Processamento de linguagem natural
- **pyttsx3 / gTTS** - Síntese de voz (Text-to-Speech)
- **SpeechRecognition** - Captura de áudio do microfone
- **PyAudio** - Interface de áudio

## Funcionalidades

- Captura de voz em tempo real via microfone
- Transcrição de áudio utilizando Whisper da OpenAI
- Processamento de perguntas e respostas com ChatGPT
- Resposta por voz com Text-to-Speech
- Suporte a múltiplos idiomas (pt-BR, en-US)
- Histórico de conversas

## Instalação

```bash
# Clone o repositório
git clone https://github.com/galafis/voice-chatgpt-whisper-python.git
cd voice-chatgpt-whisper-python

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

## Configuração

1. Obtenha uma API Key da OpenAI em [platform.openai.com](https://platform.openai.com)
2. Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_api_aqui
```

## Como Usar

```bash
python main.py
```

O chatbot irá:
1. Aguardar sua entrada de voz
2. Transcrever o áudio usando Whisper
3. Enviar a transcrição ao ChatGPT
4. Retornar a resposta por voz

## Estrutura do Projeto

```
voice-chatgpt-whisper-python/
├── main.py                 # Script principal
├── speech_to_text.py       # Módulo de transcrição (Whisper)
├── chatgpt_handler.py      # Integração com ChatGPT API
├── text_to_speech.py       # Módulo de síntese de voz
├── config.py               # Configurações e variáveis de ambiente
├── requirements.txt        # Dependências do projeto
├── .env.example            # Exemplo de variáveis de ambiente
├── LICENSE
└── README.md
```

## Autor

**Gabriel Demetrios Lafis**

- LinkedIn: [gabriel-demetrios-lafis](https://www.linkedin.com/in/gabriel-demetrios-lafis/)
- GitHub: [galafis](https://github.com/galafis)

---

> Projeto desenvolvido durante o bootcamp **Bradesco GenAI & Dados** - [DIO](https://www.dio.me/)
