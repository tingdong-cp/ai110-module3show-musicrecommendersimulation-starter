# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**


---

## 2. Intended Use  


This recommender suggests 5 songs from a small catalog based on a user's preferred genre, mood, energy level, and acoustic preference. 

It is designed for **classroom exploration** to understand how recommendation systems work — not for real music streaming users. The system assumes users know exactly what genre and mood they want.


---

## 3. How the Model Works  

The system compares each song to what the user says they like:

1. **Genre check**: Does this song's genre match the user's favorite? If yes, add 2 points.
2. **Mood check**: Does the mood match? If yes, add 1.5 points.
3. **Energy check**: How close is the song's energy level to what the user wants? The closer, the more points (up to 1 point).
4. **Acoustic check**: Does the song match the user's acoustic preference? If yes, add 0.5 points.

Then the system adds up all the points for every song and shows the top 5 highest-scoring songs.


---

## 4. Data  

The catalog contains **15 songs** with these genres: pop, lofi, rock, ambient, jazz, synthwave, indie pop, electronic, folk, and metal.

Moods include: happy, chill, intense, relaxed, moody, focused, energetic, and sad.

I added 5 songs to the original 10 to include more variety (electronic, folk, metal, and a sad song). The dataset mostly reflects mainstream Western music tastes — it doesn't include K-pop, reggaeton, classical, or non-English music.


---

## 5. Strengths  

- **Clear matches work well**: Users who want "chill lofi" get exactly that (Library Rain, Midnight Coding)
- **Transparent scoring**: Users can see exactly why a song was recommended ("genre match +2.0, mood match +1.5")
- **Different profiles get different results**: A workout user and a study user get completely different top 5 lists
- **Simple and fast**: No complex machine learning required


---

## 6. Limitations and Bias 


The system over-prioritizes genre because it's worth 2.0 points while energy similarity maxes out at 1.0 points. This means a user who asks for "high energy sad pop" will get a low-energy sad pop song (Heartbreak Avenue, energy: 0.38) instead of a high-energy song that isn't sad. The genre+mood combination (3.5 points) always beats perfect energy matching alone.

Additionally, lofi fans get 3 song options while jazz and folk fans only get 1 each — the dataset is imbalanced. The system also creates a "filter bubble" by never recommending songs outside the user's stated preferences, so a pop fan will never discover great rock songs even if they match on mood and energy.

---

## 7. Evaluation  

I tested four user profiles:
- **High-Energy Pop** (genre: pop, mood: happy, energy: 0.85)
- **Chill Lofi** (genre: lofi, mood: chill, energy: 0.3)  
- **Deep Intense Rock** (genre: rock, mood: intense, energy: 0.9)
- **Edge Case** (genre: pop, mood: sad, energy: 0.9) — conflicting preferences

Each profile got different #1 results, which felt correct. The edge case was interesting — Heartbreak Avenue won despite having low energy (0.38) because genre+mood points (3.5) beat energy similarity.

**Why "Gym Hero" keeps appearing**: Gym Hero has very high energy (0.93) and is pop genre, so it shows up for anyone wanting pop OR anyone wanting high energy. It ranked #2 for "High-Energy Pop" and appeared in the Rock user's list too because its energy level is close to what intense rock fans want.

When I doubled the energy weight in my experiment, the edge case became nearly tied (3.46 vs 3.44), showing how much weight choices matter.


---

## 8. Future Work  

- Add **tempo matching** so users can request "120 BPM workout music"
- Include a **diversity bonus** to avoid recommending 5 songs that all sound the same
- Let users specify **multiple genres** ("I like pop AND electronic")
- Add **negative preferences** ("anything but country")
- Add a "surprise me" mode that occasionally recommends outside the user's comfort zone

---

## 9. Personal Reflection  

**Biggest learning moment:** I realized that recommender systems aren't magic — they're just math comparing numbers. The "algorithm" is really just addition and sorting. But the *weight choices* (genre = 2.0, mood = 1.5) have huge consequences for what users see. A small tweak to one number completely changed my rankings.

**How AI tools helped:** Claude helped me debug path errors, generate the scoring logic, and understand why certain songs ranked higher. I had to double-check the import paths (the AI suggested paths that didn't match my folder structure) and verify that the weights were being applied correctly by manually calculating a few scores myself.

**What surprised me:** Even with only 15 songs and 4 preferences, the system "felt" like real recommendations. When I tested "Chill Lofi," getting Library Rain and Midnight Coding felt genuinely useful — not random. Simple algorithms create convincing results because they mirror how humans actually think about music (genre first, then vibe).

**What I'd try next:** I'd add tempo matching for workout playlists, let users pick multiple genres, and build a "discovery mode" that occasionally breaks the filter bubble by recommending songs the user wouldn't normally see. I'd also want to test with real users to see if my weight choices match what people actually prefer.
