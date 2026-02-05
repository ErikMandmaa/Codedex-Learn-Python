import random

def Play():
    symbols = ["🍒", "🍇", "🍉", "7️⃣"]
    results = random.choices(symbols, k=3)
    print(" | ".join(results))
    if results.count("7️⃣") == 3:
        print("Jackpot! 💰")
    else:
        print("Thanks for playing!")

Play()