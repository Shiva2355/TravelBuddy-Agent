# ✈️ TravelBuddy Agent

TravelBuddy Agent is an AI-powered travel assistant built with **LangChain, Gemini, Tavily, and SerpApi**.

It helps travelers research destinations and find flight options using external tools. The AI agent decides which tool to use based on the user's request and presents the results in a clean format.

## 🚀 Features

* 🤖 AI-powered travel assistant using Gemini
* 🔎 Destination research using Tavily Search
* ✈️ Flight search using SerpApi Google Flights
* 🧠 Agent-based tool selection using LangChain
* 🌍 Destination attractions, culture, and travel-tip research
* 📅 Flight search based on origin, destination, and travel date
* 🔐 API keys managed through environment variables

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
               ┌─────────────┐
               │   Gemini    │
               │    Agent    │
               └──────┬──────┘
                      │
             Decides which tool
                to use
             ┌────────┴────────┐
             ▼                 ▼
    ┌─────────────────┐ ┌─────────────────┐
    │ Tavily Search   │ │    SerpApi      │
    │                 │ │ Google Flights  │
    └────────┬────────┘ └────────┬────────┘
             │                   │
             ▼                   ▼
      Destination Info      Flight Options
             │                   │
             └─────────┬─────────┘
                       ▼
                  Gemini Agent
                       │
                       ▼
                 Final Response
```

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **LangGraph** through LangChain Agent
* **Google Gemini**
* **Tavily Search**
* **SerpA**
