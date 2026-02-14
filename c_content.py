# service_c_content.py
from fastapi import FastAPI
from feature_store import save_song_feature

app = FastAPI()

@app.post("/song/{song_id}")
def analyze_song(song_id: str):
    song_feature = {
        "bpm": 120,
        "mood": "energetic",
        "energy_score": 0.9
    }

    save_song_feature(song_id, song_feature)
    return {"status": "song analyzed"}
