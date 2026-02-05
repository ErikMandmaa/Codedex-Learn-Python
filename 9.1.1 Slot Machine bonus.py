import random

def Play():
    symbols = ["🍒", "🍇", "🍉", "7️⃣"]
    results = random.choices(symbols, k=3)
    print(" | ".join(results))
    if results.count("7️⃣") == 3:
        print("Jackpot! 💰")
    else:
        print("Thanks for playing!")

    while True:
        again = input("Do you want to play again? (Y/N): ").strip().upper()
        if again == 'Y':
            results = random.choices(symbols, k=3)
            print(" | ".join(results))
            if results.count("7️⃣") == 3:
                print("Jackpot! 💰")
            else:
                print("Thanks for playing!")
        elif again == 'N':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

Play()