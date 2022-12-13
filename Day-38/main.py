import requests
from datetime import datetime
from env import API_KEY, APP_ID, BEARER_TOKEN

GENDER = "male"
WEIGHT_KG = 68
HEIGHT_CM = 170.5
AGE = 21

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/f6f74973eea049e2d2a9af69dbb0982a/workoutTracking/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input("Exercise: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(EXERCISE_ENDPOINT, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": BEARER_TOKEN
    }
    sheet_response = requests.post(
        SHEET_ENDPOINT,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
