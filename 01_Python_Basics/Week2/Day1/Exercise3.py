print("Exercise 3 :  Who’s the song producer?")


# Step 1: Create the Song Class
class Song:
    """
    Represents a song and holds its lyrics as a list of strings.
    """
    def __init__(self, lyrics):
        # The 'lyrics' attribute holds the list of strings
        self.lyrics = lyrics

    def sing_me_a_song(self):
        """
        Prints the lyrics line by line.
        """
        print("\n--- Starting to Sing ---")
        for line in self.lyrics:
            print(line)
        print("--- End of Song ---\n")


# Step 2: Instantiate Song Objects and Call the Method


# 1. Example from the instructions (Led Zeppelin)
stairway_lyrics = [
    "There's a lady who's sure",
    "all that glitters is gold",
    "and she's buying a stairway to heaven"
]
stairway = Song(stairway_lyrics)

print("Song 1: Stairway to Heaven")
stairway.sing_me_a_song()



# 3. Example with short, punchy lyrics
robot_lyrics = ["Beep boop", "I am a robot", "Processing data"]
robot_song = Song(robot_lyrics)

print("Song 3: Robot Song")
robot_song.sing_me_a_song()





