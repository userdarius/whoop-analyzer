import json
from whoop import WhoopClient

username = "EMAIL"
password = "PASSWORD"

start_date = "2024-08-10 23:59:59.999999"


def get_body_measurement(username, password):
    """
    Retrieves the body measurement data from the Whoop API for the given username and password.
    Saves the data to a JSON file named `body_measurement.json`.
    """
    print("Getting body measurement...")
    with WhoopClient(username, password) as client:
        body_measurement = client.get_body_measurement()

    with open("./data/body_measurement.json", "w") as f:
        json.dump(body_measurement, f, indent=4)

    print(f"Found body measurement and saved it to `body_measurement.json`")


def get_cycle_by_id(username, password, cycle_id):
    """
    Retrieves the cycle data with the specified ID from the Whoop API for the given username and password.
    Saves the data to a JSON file named `cycle.json`.
    """
    print(f"Getting cycle with id {cycle_id}...")
    with WhoopClient(username, password) as client:
        cycle = client.get_cycle_by_id(cycle_id)

    with open("./data/cycle.json", "w") as f:
        json.dump(cycle, f, indent=4)

    print(f"Found cycle and saved it to `cycle.json`")


def get_cycle_collection(username, password, start_date):
    """
    Retrieves the cycle collection data from the Whoop API for the given username and password, starting from the specified date.
    Saves the data to a JSON file named `cycles.json`.
    """
    print("Getting cycle collection...")
    with WhoopClient(username, password) as client:
        cycles = client.get_cycle_collection(start_date=start_date)

    with open("./data/cycles.json", "w") as f:
        json.dump(cycles, f, indent=4)

    print(f"Found {len(cycles)} cycles and saved them to `cycles.json`")


def get_workout_by_id(username, password, workout_id):
    """
    Retrieves the workout data with the specified ID from the Whoop API for the given username and password.
    Saves the data to a JSON file named `workout.json`.
    """
    print(f"Getting workout with id {workout_id}...")
    with WhoopClient(username, password) as client:
        workout = client.get_workout_by_id(workout_id)

    with open("./data/workout.json", "w") as f:
        json.dump(workout, f, indent=4)

    print(f"Found workout and saved it to `workout.json`")


def get_workout_collection(username, password, start_date):
    """
    Retrieves the workout collection data from the Whoop API for the given username and password, starting from the specified date.
    Saves the data to a JSON file named `workouts.json`.
    """
    print("Getting workout collection...")
    with WhoopClient(username, password) as client:
        workouts = client.get_workout_collection(start_date=start_date)

    with open("./data/workouts.json", "w") as f:
        json.dump(workouts, f, indent=4)

    print(f"Found {len(workouts)} workouts and saved them to `workouts.json`")


def get_recovery_for_cycle(username, password, cycle_id):
    """
    Retrieves the recovery data for the cycle with the specified ID from the Whoop API for the given username and password.
    Saves the data to a JSON file named `recovery.json`.
    """
    print(f"Getting recovery for cycle with id {cycle_id}...")
    with WhoopClient(username, password) as client:
        recovery = client.get_recovery_for_cycle(cycle_id)

    with open("./data/recovery.json", "w") as f:
        json.dump(recovery, f, indent=4)

    print(f"Found recovery and saved it to `recovery.json`")


def get_recovery_collection(username, password, start_date):
    """
    Retrieves the recovery collection data from the Whoop API for the given username and password, starting from the specified date.
    Saves the data to a JSON file named `recoveries.json`.
    """
    print("Getting recovery collection...")
    with WhoopClient(username, password) as client:
        recoveries = client.get_recovery_collection(start_date=start_date)

    with open("./data/recoveries.json", "w") as f:
        json.dump(recoveries, f, indent=4)

    print(f"Found {len(recoveries)} recoveries and saved them to `recoveries.json`")


def get_sleep_by_id(username, password, sleep_id):
    """
    Retrieves the sleep data with the specified ID from the Whoop API for the given username and password.
    Saves the data to a JSON file named `sleep.json`.
    """
    print(f"Getting sleep with id {sleep_id}...")
    with WhoopClient(username, password) as client:
        sleep = client.get_sleep_by_id(sleep_id)

    with open("./data/sleep.json", "w") as f:
        json.dump(sleep, f, indent=4)

    print(f"Found sleep and saved it to `sleep.json`")


def get_sleep_collection(username, password, start_date):
    """
    Retrieves the sleep collection data from the Whoop API for the given username and password, starting from the specified date.
    Saves the data to a JSON file named `sleeps.json`.
    """
    print("Getting sleep collection...")
    with WhoopClient(username, password) as client:
        sleeps = client.get_sleep_collection(start_date=start_date)

    with open("./data/sleeps.json", "w") as f:
        json.dump(sleeps, f, indent=4)

    print(f"Found {len(sleeps)} sleeps and saved them to `sleeps.json`")


def main():
    # Ask the user what function they want to run
    print("Choose a function to run:")
    print("1. Get body measurement")
    print("2. Get cycle by ID")
    print("3. Get cycle collection")
    print("4. Get workout by ID")
    print("5. Get workout collection")
    print("6. Get recovery for cycle")
    print("7. Get recovery collection")
    print("8. Get sleep by ID")
    print("9. Get sleep collection")

    choice = input("Enter the number of the function you want to run: ")

    if choice == "1":
        get_body_measurement(username, password)
    elif choice == "2":
        cycle_id = input("Enter the cycle ID: ")
        get_cycle_by_id(username, password, cycle_id)
    elif choice == "3":
        get_cycle_collection(username, password, start_date)
    elif choice == "4":
        workout_id = input("Enter the workout ID: ")
        get_workout_by_id(username, password, workout_id)
    elif choice == "5":
        get_workout_collection(username, password, start_date)
    elif choice == "6":
        cycle_id = input("Enter the cycle ID: ")
        get_recovery_for_cycle(username, password, cycle_id)
    elif choice == "7":
        get_recovery_collection(username, password, start_date)
    elif choice == "8":
        sleep_id = input("Enter the sleep ID: ")
        get_sleep_by_id(username, password, sleep_id)
    elif choice == "9":
        get_sleep_collection(username, password, start_date)
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
