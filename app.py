from crewai import Agent,Task,Crew,Process,LLM 
import os

#google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBtBqz8T0XB724Z1NeG49m6yeuYWu2rHII"

llm=LLM(
    model="google/gemini-2.5-flash",
    temperature=0.4
)
#User input
event_name="College Tech Fest"
budget="$3000"
guests=200

#Agent -Event Planner
Planner_agent=Agent(
    role="Event_Planner",
    goal="Create a Event Plan",
    backstory="Expert event organizer",
    verbose=True,
    llm=llm


)
planning_task=Task(
    description=f"""
    plan event:
    {event_name}
    Guests:{guests}
    Give:
    -Theme
    -Venue
    -Food
    """,
    expected_output="Simple event plan.",
    agent=Planner_agent
)
#crewai pipline
crew=Crew(
    agents=[
        Planner_agent
    ],
    tasks=[
        planning_task
    ],
    process=Process.sequential,
    verbose=True

)

#run pipeline

print("\n starting Ai event Automation")
result=crew.kickoff()
print("\n=============")
print("Final Event Report")
print("==============")
print(result)