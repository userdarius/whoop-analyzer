from flask import Flask, request, jsonify
from get_data import (
    get_body_measurement,
    get_cycle_by_id,
    get_cycle_collection,
    get_workout_by_id,
    get_workout_collection,
    get_recovery_for_cycle,
    get_recovery_collection,
    get_sleep_by_id,
    get_sleep_collection,
    start_date,
)

app = Flask(__name__)


def get_credentials():
    user_email = request.args.get("user_email")
    user_password = request.args.get("user_password")
    if not user_email or not user_password:
        return jsonify({"error": "Missing credentials"}), 400
    return user_email, user_password


@app.route("/body-measurement", methods=["GET"])
def body_measurement():
    credentials = get_credentials()
    if isinstance(credentials, tuple):
        user_email, user_password = credentials
    else:
        return credentials

    get_body_measurement(user_email, user_password)
    return (
        jsonify({"message": "Body measurement data saved to body_measurement.json"}),
        200,
    )


@app.route("/cycle/<cycle_id>", methods=["GET"])
def cycle(cycle_id):
    credentials = get_credentials()
    if isinstance(credentials, tuple):
        user_email, user_password = credentials
    else:
        return credentials

    get_cycle_by_id(user_email, user_password, cycle_id)
    return (
        jsonify({"message": f"Cycle data for ID {cycle_id} saved to cycle.json"}),
        200,
    )


@app.route("/cycles", methods=["GET"])
def cycles():
    credentials = get_credentials()
    if isinstance(credentials, tuple):
        user_email, user_password = credentials
    else:
        return credentials

    get_cycle_collection(user_email, user_password, start_date)
    return jsonify({"message": "Cycle collection data saved to cycles.json"}), 200


@app.route("/workout/<workout_id>", methods=["GET"])
def workout(workout_id):
    credentials = get_credentials()
    if isinstance(credentials, tuple):
        user_email, user_password = credentials
    else:
        return credentials

    get_workout_by_id(user_email, user_password, workout_id)
    return (
        jsonify({"message": f"Workout data for ID {workout_id} saved to workout.json"}),
        200,
    )


@app.route("/workouts", methods=["GET"])
def workouts():
    credentials = get_credentials()
    if isinstance(credentials, tuple):
        user_email, user_password = credentials
    else:
        return credentials

    get_workout_collection(user_email, user_password, start_date)
    return jsonify({"message": "Workout collection data saved to workouts.json"}), 200


@app.route("/recovery/<cycle_id>", methods=["GET"])
def recovery(cycle_id):
    credentials = get_credentials()
    if isinstance(credentials, tuple):
        user_email, user_password = credentials
    else:
        return credentials

    get_recovery_for_cycle(user_email, user_password, cycle_id)
    return (
        jsonify(
            {"message": f"Recovery data for cycle ID {cycle_id} saved to recovery.json"}
        ),
        200,
    )


@app.route("/recoveries", methods=["GET"])
def recoveries():
    credentials = get_credentials()
    if isinstance(credentials, tuple):
        user_email, user_password = credentials
    else:
        return credentials

    get_recovery_collection(user_email, user_password, start_date)
    return (
        jsonify({"message": "Recovery collection data saved to recoveries.json"}),
        200,
    )


@app.route("/sleep/<sleep_id>", methods=["GET"])
def sleep(sleep_id):
    credentials = get_credentials()
    if isinstance(credentials, tuple):
        user_email, user_password = credentials
    else:
        return credentials

    get_sleep_by_id(user_email, user_password, sleep_id)
    return (
        jsonify({"message": f"Sleep data for ID {sleep_id} saved to sleep.json"}),
        200,
    )


@app.route("/sleeps", methods=["GET"])
def sleeps():
    credentials = get_credentials()
    if isinstance(credentials, tuple):
        user_email, user_password = credentials
    else:
        return credentials

    get_sleep_collection(user_email, user_password, start_date)
    return jsonify({"message": "Sleep collection data saved to sleeps.json"}), 200


if __name__ == "__main__":
    app.run(debug=True)
