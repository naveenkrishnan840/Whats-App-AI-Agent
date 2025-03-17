# What's App AI Agent

<div align="center">
  <!-- Backend -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Qdrant-FF6F00?style=for-the-badge&logo=qdrant&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-FF4A00?style=for-the-badge&logo=groq&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white" />
  <img src="https://img.shields.io/badge/LangGraph-FF6B6B?style=for-the-badge&logo=graph&logoColor=white" />
  <img src="https://img.shields.io/badge/OpenAI_Whisper-412991?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/ElevenLabs-000000?style=for-the-badge&logo=elevenlabs&logoColor=white" />
  <img src="https://img.shields.io/badge/Together.AI-FF5733?style=for-the-badge&logo=togetherai&logoColor=white" />
  <img src="https://img.shields.io/badge/LLaMA_Text_Model-1877F2?style=for-the-badge&logo=meta&logoColor=white" />
  <img src="https://img.shields.io/badge/LLaMA_Vision_Model-1877F2?style=for-the-badge&logo=meta&logoColor=white" />
  <img src="https://img.shields.io/badge/Gemma_Model-4285F4?style=for-the-badge&logo=google&logoColor=white" />

  <!-- Frontend -->
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />

  <h3>Your Ava's Co-pilot for What's App AI agents Chat Bot 🚀</h3>

  <p align="center">
    <b> Memory Extraction Agent | Memory Injection Agent | Workflow Router Agent | Audio Agent | Image Agent | Summarize Conversation Agent </b>
  </p>
</div>

# Overview
<b>Ava’s Bot</b> is a smart, multi-agent system designed to provide a seamless, efficient, and personalized experience for users interacting via WhatsApp. With the ability to handle text, images, and audio, Ava’s Bot leverages AI-powered NLP, memory management to deliver context-aware, human-like conversations.

By integrating SQLite for short-term memory, Qdrant for long-term memory, and real-time workflow automation, Ava’s Bot ensures intelligent decision-making while enhancing user interactions. The bot can process text-to-text, text-to-image, image-to-text, text-to-audio, and audio-to-text requests, making it a powerful tool for advanced conversational AI applications.

By leveraging cutting-edge AI models, Ava’s Bot streamlines complex interactions, making AI-driven conversations smarter, more interactive, and highly personalized. 🚀

# Motivation
Efficiency meets innovation. With the power of intelligent AI, Ava’s Bot redefines seamless and personalized conversations. It doesn’t just process text, images, and audio—it enhances interactions, making them more intuitive, context-aware, and engaging.

Whether it’s understanding speech, generating images, or recalling past conversations, Ava’s Bot is your intelligent companion, streamlining complex interactions with effortless precision. With cutting-edge memory integration and AI capabilities, it ensures every conversation is smarter, more interactive, and deeply personalized.

Embrace the future of AI-driven conversations and experience the next evolution of intelligent assistance. 🚀

## Agents Features & Agent Types & Agent Informations

## Agent Capabilities
  ### 1. Memory Extraction
  The Memory Extraction is used to store chat information for both ava's and user chat to get seemless experiences.
#### Capabilities:
  - **Understanding Context** – Extracts key details from user conversations to maintain contextual awareness.
  - **Long-Term Memory** – Utilizes Qdrant (vector database) to store current conversations and enhance personalized interactions over time.
  - **Intelligent Prioritization** – Identifies and classifies important information, ensuring relevant memories are stored while filtering out unnecessary data.
  - **Efficient Retrieval** – Enables Ava’s Bot to remember user preferences, past queries, and ongoing tasks, leading to smoother, more natural conversations.
  - **Multi-Modal Memory Processing** – Extracts meaningful insights from text, images, and audio, allowing Ava’s Bot to recall and reference past interactions across different formats.

### 2. Memory Injection
  The Flights Assistant is responsible for assisting users with flight bookings, availability checks, and flight-related queries.

#### Capabilities:
  - **Context-Aware Responses** – Retrieves relevant past conversations from SQLite (short-term memory) or Qdrant (long-term memory) to provide seamless, intelligent replies.
  - **Personalized Interactions** – Injects stored knowledge into conversations, ensuring Ava’s Bot remembers user preferences, past questions, and important details.
  - **Multi-Modal Integration** – Injects relevant text, image, and audio-based memory, allowing natural continuity across different conversation formats.
  - **Dynamic Memory Retrieval** – Uses AI-driven logic to decide when and what memory should be injected, preventing unnecessary or outdated responses.
  - **Enhancing User Experience** – Eliminates repetitive questioning by recalling past interactions, making conversations fluid and engaging.
  - **Workflow Optimization** – Works alongside the Memory Extraction and Workflow Decision agents to ensure the right information is used at the right time.
  - **Adaptive Learning** – Continuously updates and refines memory based on new user inputs, improving response accuracy over time.
  - **Efficient Query Processing** – Uses vector search (Qdrant) to find the most relevant stored memories and integ
    
### 3. Workflow Router
  The workflow router is a decision-making system determines whether to process text, images, or audio. The system dynamically executes the right AI model for the given input.

#### Capabilities:
  - **Task Decision Engine** – Determines whether the input is text, image, or audio and routes it to the appropriate processing pipeline.
  - **Seamless Multi-Modal Handling** – Directs text queries to NLP models, images to vision models, and audio to speech processing for efficient execution.
  - **Real-Time Processing** – Ensures low-latency routing, making decisions instantly to provide quick responses.
  - **Memory Integration** – Works alongside Memory Extraction & Injection to enhance responses with stored knowledge.
  - **Memory Integration** – Works alongside Memory Extraction & Injection to enhance responses with stored knowledge.
    
### 4. Audio Agent
  The audio agent is used to interact with elevanlabs to get model response to ava's voice as seemless experience. 

#### Capabilities:
  - **Text-to-Speech Generation** – Uses **ElevenLabs.io** to generate realistic, human-like audio responses.
  - **English-Language Support** – Enables Ava’s Bot to understand and respond in multiple languages, making interactions more accessible.
  - **Seamless Workflow Integration** – Works with the Workflow Router to determine when to process audio inputs or generate speech responses.
  - **Noise Reduction & Optimization** – Ensures clean and high-quality audio processing, even in noisy environments.
    
### 5. Conversation
  Uses LLaMA, Gemma, and other LLMs to generate high-quality, human-like text responses.

#### Capabilities:
  - **Advanced NLP Processing** – Uses LLaMA, Gemma, and other LLMs to generate high-quality, human-like text responses.
  - **Context-Aware Responses** – Leverages Memory Extraction & Injection via Qdrant to maintain conversational flow and recall past interactions.
  - **Multi-Turn Dialogue Handling** – Supports long-form conversations, allowing seamless, intelligent discussions over multiple messages.

### 6. summarize conversation 
  This agents is used to summarize the previous memory and feed into model to get appropriate response.
  
### Agent Architecture Diagrams

#### Deep multi Agent Work Flow
<img src="https://github.com/naveenkrishnan840/Whats-App-AI-Agent/blob/main/backend/graph.png"/>

## Project Structure 
```
ai-hedge-fund/
├── src/
│   ├── assistant/                           # Agent definitions and workflow
│   │   ├── __init__.py                      # init file
│   │   ├── primary_assistant.py             # primary assistant agent
│   │   ├── hotel_assistant.py               # hotel_assistant agent
│   │   ├── flight_assistant.py              # flight assistant agent
│   │   ├── car_rental_assistant.py          # Car rental agent
│   │   ├── excursion_assistant.py           # Car rental agent
|   ├── database                             # To store the vector files
│   ├── tools/                               # Agent tools
│   │   ├── __init__.py                      # init file
|   |   ├── car_rental.py                    # To handle the search, update, cancel things
|   |   ├── flights.py                       # To handle the search, update, cancel things
|   |   ├── hotels.py                        # To handle the search, update, cancel things
|   |   ├── excursions.py                    # To handle the search, update, cancel things
|   |   ├── lookup_policies_search_tool.py   # To retrieve the policy content
│   ├── build_graph.py                       # building the graph
|   ├── question.py
|   ├── request_validate.py                  # request validation
|   ├── utilities.py 
│────── .env # If you want
│────── data_insertion.py # customer related records insert to mysql db
│────── pyproject.toml # create virtual env using poetry
│────── main.py # Main entry point
├── pyproject.toml
├── ...
```

## Setup Instructions

### Backend Setup

1. Clone the repository
   ```bash
   git clone https://github.com/naveenkrishnan840/customer-support-bot.git
   cd customer-support-bot
   cd backend
   ```

2. Install Poetry (if not already installed)

   Mac/Linux:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
   Windows:
   ```bash
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

3. Set Python version for Poetry
   ```bash
   poetry env use python3.12
   ```

4. Activate the Poetry shell:
   For Unix/Linux/MacOS:
   ```bash
   poetry shell
   # or manually
   source $(poetry env info --path)/bin/activate
   ```
   For Windows:
   ```bash
   poetry shell
   # or manually
   & (poetry env info --path)\Scripts\activate
   ```

5. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

6. Set up environment variables in `.env`:
   ```bash
    GOOGLE_API_KEY="Your api key"
    TAVILY_API_KEY="Your api key"
    COHERE_API_KEY="Your api key"
    MYSQL_HOST="Your host url"
    MYSQL_USER="Your user"
    MYSQL_PASSWORD="your password"
    MYSQL_DB="your database name"
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
    LANGCHAIN_API_KEY="your api key"
    LANGCHAIN_PROJECT="your project name"
   ```

7. Run the backend:

   Make sure you are in the backend folder

    ```bash
    uvicorn app.main:app --reload --port 8000 
    ```

   For Windows User:

    ```bash
    uvicorn app.main:app --port 8000
    ```

8. Access the API at `http://localhost:8000`

### Frontend Setup

1. Open a new terminal and make sure you are in the WebRover folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the frontend:
   ```bash
   npm run dev
   ```

4. Access the frontend at `http://localhost:3000`

For mac users: 

Try running http://localhost:3000 on Safari browser. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [@naveenkrishnan840](https://github.com/naveenkrishnan840)
