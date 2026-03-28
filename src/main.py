"""
Command line runner for the Music Recommender Simulation.
Stress tests with diverse and adversarial user profiles.
"""

from recommender import load_songs, recommend_songs


def test_profile(name: str, user_prefs: dict, songs: list) -> None:
    """Test a single user profile and display top 5 results."""
    print(f"\n{'='*60}")
    print(f"👤 Profile: {name}")
    print(f"   Genre: {user_prefs['genre']} | Mood: {user_prefs['mood']}")
    print(f"   Energy: {user_prefs['energy']} | Acoustic: {user_prefs['likes_acoustic']}")
    print("-"*60)

    recommendations = recommend_songs(user_prefs, songs, k=5)

    for rank, (song, score, explanation) in enumerate(recommendations, 1):
        print(f"#{rank} {song['title']} — Score: {score:.2f}")
        print(f"    {explanation}")
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"📀 Loaded {len(songs)} songs\n")

    # Profile 1: High-Energy Pop
    test_profile("High-Energy Pop", {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.85,
        "likes_acoustic": False
    }, songs)

    # Profile 2: Chill Lofi
    test_profile("Chill Lofi", {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.3,
        "likes_acoustic": True
    }, songs)

    # Profile 3: Deep Intense Rock
    test_profile("Deep Intense Rock", {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.9,
        "likes_acoustic": False
    }, songs)

    # Profile 4: ADVERSARIAL - Conflicting preferences
    # High energy but sad mood - can the system handle this?
    test_profile("⚠️ Edge Case: High Energy + Sad", {
        "genre": "pop",
        "mood": "sad",
        "energy": 0.9,
        "likes_acoustic": False
    }, songs)


if __name__ == "__main__":
    main()
