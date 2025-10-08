import random

def sigmer():
    text = """You're so skibidi fanum taxing in the sigma Patrick Bateman 🤡. Level 6 gyatt ong and on Kai Cenat's W rizz. Baby Gronk & Ice Spice doing the grimace shake challenge with smurf cat. Only in ohio does sussy baka peppino pizza tower on the Skibidi Toilet Titan Cameraman, TV Woman, Lankybox and Titan Speakerman. There's nothing we can do.. but me personally I wouldn't let that slide cuh. 🗿🍷 masteroogway, Speedmcqueen, manlikeisaac. Nathaniel B on that goth thug shaker fortnite roblox pass be on South Park, Family Guy and Subway surfers. Fr tho, can he beat American 📸 Sus. Goku? NickEh30 w/ opium bird & cg5. Mommy/daddy? Jit trippin, nahhh das crazy. Do the griddy with the biggest bird in Rainbow Friends and Huggy Wuggy. Doors be the most lightskin stare Travis Scott has ever seen with Drake. Blud got that 1, 2, buckle my shoe PACKGOD vs Leg w/ IShowSpeed on that Garten of Banban rizzler."""
    
    words = text.split()
    
    emojis = ["🔥", "💀", "😩", "🗿", "🚽", "👽", "🤯", "🐸", "🍷", "💅", "😈", "📸", "👻", "💥", "🦅", "🗣️", "🤌", "🙌", "💫"]
    
    random.shuffle(words)
    
    result = []
    for word in words:
        result.append(word)
        if random.random() < 0.3: 
            result.append(random.choice(emojis))
    
    return " ".join(result)

if __name__ == "__main__":
    print(sigmer())
