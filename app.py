
from langchain.chat_models import init_chat_model
from langchain.tools import tool 
from langchain.agents import create_agent 
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
import os
import requests
load_dotenv()


GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
SERPAPI_KEY=os.getenv("SERPAPI_KEY")
# Step 1: Initialize the Model
model = init_chat_model(
    "gemini-3.8-flash",
    model_provider="google_genai",
    api_key=GOOGLE_API_KEY
)

# Step 2: Create Destination Research Tool (Tavily)
destination_research_tool =TavilySearch(
    max_results=5,
    search_depth="advanced",
    tavily_api_key=TAVILY_API_KEY
)


# Step 3: Create Flight Search Tool
def search_flights(origin: str, destination: str, date: str) -> list:
    """Search for flights using SerpAPI Google Flights. Date should be in YYYY-MM-DD format like '2026-12-15'."""
    url=f"https://serpapi.com/search.json?engine=google_flights&departure_id={origin}&arrival_id={destination}&currency=USD&type=2&outbound_date=2026-09-30"
    response = requests.get(url, params={
        "engine": "google_flights",
        "departure_id": origin,
        "arrival_id": destination,
        "currency": "USD",
        "type": "2",
        "outbound_date": date,
        "api_key": SERPAPI_KEY
    })
    data=response.json()
    flights = []

    for flight in data.get("best_flights", []) + data.get("other_flights", []):
        f = flight["flights"][0]

        flights.append({
            "airline": f["airline"],
            "flight_number": f["flight_number"],
            "departure": f["departure_airport"]["time"],
            "arrival": f["arrival_airport"]["time"],
            "duration_minutes": f["duration"],
            "price_usd": flight["price"],
            "travel_class": f["travel_class"]
        })

    return flights
system_prompt="""You are a TravelBuddy assistant that helps travelers plan trips.
You have access to these tools:
- destination_research_tool: Research attractions, culture, and travel tips
- search_flights: Find flight options (use IATA codes: HYD=Hyderabad, GOI=Goa, BOM=Mumbai, DEL=Delhi, BLR=Bangalore)
Help the traveler by researching destinations and finding flights.
Present results in a clean, readable format with clear sections.
Don't use markdown format."""

agent=create_agent(
    model=model,
    tools=[destination_research_tool,search_flights],
    system_prompt=system_prompt
)
# Step 4: Define System Prompt
result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Find flights from VTZ to DEL on 2026-12-15"
        }
    ]
})

print(result["messages"][-1].content[0]["text"])

# Step 5: Create and Run the Agent

