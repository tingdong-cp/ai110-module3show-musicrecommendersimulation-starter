import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

GENRE_WEIGHT = 2.0    # Reset
MOOD_WEIGHT = 1.5     # Keep same
ENERGY_WEIGHT = 1.0   # Reset
ACOUSTIC_WEIGHT = 0.5 # Keep same

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        scored = [(song, self._score_song(user, song)) for song in self.songs]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [song for song, score in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append(f"matches your favorite genre ({song.genre})")

        if song.mood == user.favorite_mood:
            reasons.append(f"matches your preferred mood ({song.mood})")

        energy_diff = abs(song.energy - user.target_energy)
        if energy_diff < 0.2:
            reasons.append(f"energy level ({song.energy:.1f}) is close to your target")

        if user.likes_acoustic and song.acousticness > 0.5:
            reasons.append("has the acoustic sound you like")
        elif not user.likes_acoustic and song.acousticness < 0.5:
            reasons.append("has the electronic sound you prefer")

        if reasons:
            return "Recommended because it " + ", and ".join(reasons) + "."
        else:
            return "This song partially matches your preferences."

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and converts numeric fields."""
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numeric fields from strings to proper types
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness']),
            }
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song based on user preferences and returns score with reasons."""

    score = 0.0
    reasons = []

    # Genre match (categorical)
    if song['genre'] == user_prefs['genre']:
        score += GENRE_WEIGHT
        reasons.append(f"genre match (+{GENRE_WEIGHT})")

    # Mood match (categorical)
    if song['mood'] == user_prefs['mood']:
        score += MOOD_WEIGHT
        reasons.append(f"mood match (+{MOOD_WEIGHT})")

    # Energy similarity (numerical - closer is better)
    energy_diff = abs(song['energy'] - user_prefs['energy'])
    energy_score = (1.0 - energy_diff) * ENERGY_WEIGHT
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    # Acoustic preference
    if user_prefs['likes_acoustic'] and song['acousticness'] > 0.5:
        score += ACOUSTIC_WEIGHT
        reasons.append(f"acoustic match (+{ACOUSTIC_WEIGHT})")
    elif not user_prefs['likes_acoustic'] and song['acousticness'] < 0.5:
        score += ACOUSTIC_WEIGHT
        reasons.append(f"non-acoustic match (+{ACOUSTIC_WEIGHT})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Returns top k songs ranked by score with explanations."""
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    # Sort by score (highest first)
    scored_songs.sort(key=lambda x: x[1], reverse=True)

    # Return top k
    return scored_songs[:k]
