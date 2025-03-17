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
<b>Ava’s Bot</b> is a smart, multi-agent system designed to provide a seamless, efficient, and personalized experience for users interacting via WhatsApp. With the ability to handle text, images, and audio, Ava’s Bot leverages AI-powered NLP, memory management, and multimodal processing to deliver context-aware, human-like conversations.

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
  - Understanding Context – Extracts key details from user conversations to maintain contextual awareness.
  - Long-Term Memory – Utilizes Qdrant (vector database) to store current conversations and enhance personalized interactions over time.
  - Intelligent Prioritization – Identifies and classifies important information, ensuring relevant memories are stored while filtering out unnecessary data.
  - Efficient Retrieval – Enables Ava’s Bot to remember user preferences, past queries, and ongoing tasks, leading to smoother, more natural conversations.
  - Multi-Modal Memory Processing – Extracts meaningful insights from text, images, and audio, allowing Ava’s Bot to recall and reference past interactions across different formats.

### 2. Memory Injection
  The Flights Assistant is responsible for assisting users with flight bookings, availability checks, and flight-related queries.

#### Capabilities:
  - *Context-Aware Responses* – Retrieves relevant past conversations from SQLite (short-term memory) or Qdrant (long-term memory) to provide seamless, intelligent replies.
  - Personalized Interactions – Injects stored knowledge into conversations, ensuring Ava’s Bot remembers user preferences, past questions, and important details.
  - Multi-Modal Integration – Injects relevant text, image, and audio-based memory, allowing natural continuity across different conversation formats.
  - Dynamic Memory Retrieval – Uses AI-driven logic to decide when and what memory should be injected, preventing unnecessary or outdated responses.
  - Enhancing User Experience – Eliminates repetitive questioning by recalling past interactions, making conversations fluid and engaging.
  - Workflow Optimization – Works alongside the Memory Extraction and Workflow Decision agents to ensure the right information is used at the right time.
  - Adaptive Learning – Continuously updates and refines memory based on new user inputs, improving response accuracy over time.
  - Efficient Query Processing – Uses vector search (Qdrant) to find the most relevant stored memories and integrate them into conversations in real-time.
##### Tools:
  - Search: Queries available flights from the database based on user input (e.g., departure date, source, and destination).
  - Book: Allows flight booking by processing user preferences and providing confirmation details.
  - Update: Facilitates modification of flight bookings, such as changing travel dates, or seat preferences.
  - Cancel: Manages cancellation of flight bookings and provides options to the user, including refund or rebooking.
### 3. Car Rental Assistant
  The Car Rental Assistant handles car rental searches, bookings, and changes related to rental vehicles.

#### Capabilities:
  1. Car Rental Search: Retrieves available car rental options based on user preferences and location.
     - Example:
         - Europcar (Economy) in Basel from 2024-04-14 to 2024-04-11.
         - Avis (Luxury) in Basel from 2024-04-10 to 2024-04-20.
         - Hertz (Midsize) in Zurich from 2024-04-10 to 2024-04-07.
         - Sixt (SUV) in Bern from 2024-04-20 to 2024-04-26.
  2. Car Rental Booking: Facilitates car rental booking based on available options, allowing users to select vehicle type, pickup/dropoff locations, and rental dates.
  3. Car Rental Update: Users can request changes to an existing car rental, such as altering the rental period or car type.
  4. Car Rental Cancellation: Provides the ability to cancel a car rental reservation, either entirely or for specific dates.
##### Tools:
  1. Search: Allows users to search for car rental availability based on location, vehicle type, and rental dates.
  2. Book: Facilitates car rental bookings, ensuring availability and confirming reservation details.
  3. Update: Manages changes to existing reservations, such as modifying pickup dates or vehicle categories.
  4. Cancel: Handles cancellations for car rental bookings and initiates refund processes when applicable.

### 4. Hotel Assistant
  The Hotel Assistant helps users with hotel searches, availability, bookings, and modifications.

#### Capabilities:
  1. Hotel Search: Retrieves available hotels based on location, category (luxury, upscale, etc.), and dates.
      - Example:
         - Hilton Basel (Luxury) for 2024-04-22 to 2024-04-20.
         - Marriott Zurich (Upscale) for 2024-04-14 to 2024-04-21.
         - Hyatt Regency Basel (Upper Upscale) for 2024-04-02 to 2024-04-20.
         - Hotel Booking: Users can book rooms at selected hotels, choosing their room preferences (e.g., single, double, suite) and finalizing their reservation.
         - Hotel Update: Allows users to update existing reservations, such as changing check-in/check-out dates or room preferences.
         - Hotel Cancellation: Facilitates hotel reservation cancellation, and provides users with refund or rebooking options.
##### Tools:
1. Search: Retrieves hotel availability from the database, considering the location, dates, and hotel category preferences.
2. Book: Assists with hotel room reservations, confirming booking details.
3. Update: Handles updates for existing hotel reservations, such as modifying dates or room types.
4. Cancel: Manages cancellation of hotel bookings and processes refunds where applicable.

### 5. Excursion Assistant
  The Excursion Assistant allows users to explore and book excursions, activities, and tours at various locations.

#### Capabilities:
  1. Excursion Search: Retrieves details of available excursions based on location, type (landmark, history, art, etc.), and user preferences.
       - Example:
          - Basel Minster (landmark, history) in Basel.
          - Kunstmuseum Basel (art, museum) in Basel.
          - Zurich Old Town (history, architecture) in Zurich.
          - Lucerne Chapel Bridge (landmark, history) in Lucerne.
          - Excursion Booking: Enables users to book excursions or tours based on selected dates, locations, and activities.
          - Excursion Update: Users can modify bookings for excursions, such as changing the date or activity details.
          - Excursion Cancellation: Manages cancellation of excursion bookings, including refund options where necessary.
##### Tools:
  1. Search: Queries available excursions from the database based on user location and activity type.
  2. Book: Facilitates booking of excursions, including details of the activity, dates, and special requests.
  3. Update: Handles modifications to excursion bookings, including date changes or activity preferences.
  4. Cancel: Allows users to cancel their excursion bookings and processes refund requests when applicable.

### General Tools:
  1. Customer policy information
       - Customer Policy Information typically refers to the set of rules and guidelines that govern interactions between a service provider (e.g., airline, hotel,
          car rental company, excursion provider) and its customers.
  3. TavilySearch
       - TavilySearch seems to be a search service or tool that could be involved in searching for various travel-related offerings (flights, hotels,
          car rentals, excursions). This could be part of an API or platform providing a seamless search experience for users.
     
### Agent Architecture Diagrams

#### Deep multi Agent Work Flow
<img src="https://github.com/naveenkrishnan840/customer-support-bot/blob/main/graph.png"/>

*Multi Agent's workflow for comprehensive booking and content generation*
## Extract the aircraft information
### Populate information to database
  #### url https://storage.googleapis.com/benchmarks-artifacts/travel-db/travel2.sqlite
  This url is need to extract the information to create & insert the records.
  #### url https://storage.googleapis.com/benchmarks-artifacts/travel-db/swiss_faq.md
  This url is need to extract the information to create the retriever information
  
## Architecture

The system is built on a modern tech stack with three distinct agent types, each powered by:

1. **State Management**
   - LangGraph for maintaining agent message state
   - Handles complex navigation flows and decision making
   - Structured workflow management
    
2. **Content Processing**
   - RAG (Retrieval Augmented Generation) pipeline
   - Vector store integration for efficient information storage
   - Automatic content structuring and organization

3. **AI Decision Making**
   - Multiple LLM integration (Gemini, deepseek)
   - Context-aware navigation
   - Self-review mechanisms
   - Structured output generation


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
