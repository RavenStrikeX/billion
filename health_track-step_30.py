# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: HealthTrack
def load_profiles():
    profiles_path = "profiles.json"
    if os.path.exists(profiles_path):
        with open(profiles_path) as f:
            return json.load(f)
    return {"default": {"name": "Default", "age": 0, "height_cm": 175, "weight_kg": 75, "target_weight_kg": None, "notes": ""}}

def save_profiles(profiles):
    with open("profiles.json", "w") as f:
        json.dump(profiles, f)

def list_profiles():
    profiles = load_profiles()
    return [(name, data["age"], data["weight_kg"]) for name, data in profiles.items()]

def select_profile(name):
    profiles = load_profiles()
    if name not in profiles:
        print(f"Profile '{name}' not found. Available: {list(profiles.keys())}")
        return None
    profile = profiles[name]
    return {**profile, "active": True}

def add_profile(name, age=0, height_cm=175, weight_kg=75, target_weight_kg=None):
    profiles = load_profiles()
    if name in profiles:
        print(f"Profile '{name}' already exists.")
        return None
    new_profile = {"name": name, "age": age, "height_cm": height_cm, "weight_kg": weight_kg, "target_weight_kg": target_weight_g, "notes": ""}
    profiles[name] = new_profile
    save_profiles(profiles)
    return new_profile

def delete_profile(name):
    profiles = load_profiles()
    if name == "default" or not profiles.get(name):
        print("Cannot delete default profile.")
        return False
    del profiles[name]
    save_profiles(profiles)
    return True
