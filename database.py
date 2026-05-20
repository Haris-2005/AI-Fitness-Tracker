import sqlite3

def get_conn():
    return sqlite3.connect("fitness.db")

def init_db():
    conn = sqlite3.connect("fitness.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY, name TEXT, age INTEGER,
        weight REAL, height REAL, goal TEXT, activity TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS nutrition (
        id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT,
        water REAL, calories REAL, protein REAL,
        carbs REAL, fibre REAL, probiotics TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT,
        exercise TEXT, sets INTEGER, reps INTEGER,
        weight REAL, duration INTEGER, calories_burned REAL, notes TEXT)""")
    conn.commit()
    conn.close()

def calculate_nutrition(weight, height, age, goal, activity):
    factors = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725
    }
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    tdee = bmr * factors.get(activity, 1.55)
    if goal == "Lose Weight":
        cal = tdee - 500
    elif goal == "Gain Muscle":
        cal = tdee + 300
    else:
        cal = tdee
    return {
        "calories": round(cal),
        "protein": round(weight * 2),
        "carbs": round((cal * 0.45) / 4),
        "fibre": 30,
        "water": round(weight * 0.033, 1),
        "probiotics": "1 serving/day"
    }