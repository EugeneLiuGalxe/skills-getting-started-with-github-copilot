"""
Mergington High School Management System API

This FastAPI application allows students to view available extracurricular activities
and sign up for them.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

# Initialize the FastAPI app
app = FastAPI(
    title="Mergington High School API",
    description="API for managing extracurricular activities at Mergington High School"
)

# Mount the static files directory for serving frontend assets
current_dir = Path(__file__).parent
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(current_dir, "static")),
    name="static"
)

# In-memory database for activities
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments.",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects.",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Participate in physical education and sports activities.",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the soccer team and compete in matches.",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice and play basketball games.",
        "schedule": "Wednesdays and Fridays, 3:00 PM - 4:30 PM",
        "max_participants": 15,
        "participants": ["james@mergington.edu", "lucas@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore your creativity through painting and drawing.",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["mia@mergington.edu", "amelia@mergington.edu"]
    },
    "Drama Club": {
        "description": "Participate in theater productions and acting workshops.",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["harper@mergington.edu", "evelyn@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and prepare for competitions.",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["elijah@mergington.edu", "logan@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts.",
        "schedule": "Fridays, 3:00 PM - 4:30 PM",
        "max_participants": 12,
        "participants": ["avery@mergington.edu", "scarlett@mergington.edu"]
    }
}


@app.get("/")
def redirect_to_homepage():
    """
    Redirect the root URL to the static homepage.
    """
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def list_activities():
    """
    Retrieve the list of all available activities.
    """
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """
    Sign up a student for a specific activity.

    Args:
        activity_name (str): The name of the activity.
        email (str): The email of the student signing up.

    Returns:
        dict: A success message if the signup is successful.

    Raises:
        HTTPException: If the activity does not exist or the student is already signed up.
    """
    # Check if the activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Retrieve the activity details
    activity = activities[activity_name]

    # Check if the student is already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up for this activity")

    # Add the student to the participants list
    activity["participants"].append(email)
    return {"message": f"Successfully signed up {email} for {activity_name}"}
