import json
from whoop import WhoopClient
import json
from whoop import WhoopClient

username = "EMAIL"
password = "PASSWORD"

start_date = "2022-10-12 23:59:59.999999"


def get_workout_collection(username, password, start_date):
    """
    Retrieves the workout collection data from the Whoop API for the given username and password, starting from the specified date.
    Saves the data to a JSON file named `workouts.json`.
    """
    print("Getting workout collection...")
    with WhoopClient(username, password) as client:
        workouts = client.get_workout_collection(start_date=start_date)

    with open("workouts.json", "w") as f:
        json.dump(workouts, f, indent=4)

    print(f"Found {len(workouts)} workouts and saved them to `workouts.json`")
