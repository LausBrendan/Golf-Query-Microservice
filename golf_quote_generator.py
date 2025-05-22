import json
import random

# Load quotes from JSON file
with open("/mnt/data/golf_quotes.json", "r") as f:
    quotes = json.load(f)

def display_random_quote():
    key = random.choice(list(quotes.keys()))
    print(f"\nRandom Quote:\n{quotes[key]}\n")

def filter_by_golfer(name):
    print(f"\nQuotes by '{name}':")
    found = False
    for quote in quotes.values():
        if quote.lower().startswith(name.lower() + ":"):
            print(f"- {quote}")
            found = True
    if not found:
        print("No quotes found for that golfer.")

def filter_by_keyword(keyword):
    print(f"\nQuotes containing '{keyword}':")
    found = False
    for quote in quotes.values():
        if keyword.lower() in quote.lower():
            print(f"- {quote}")
            found = True
    if not found:
        print("No quotes found containing that word.")

def main():
    while True:
        print("\nGolf Quote Generator Menu:")
        print("1. Display a random quote")
        print("2. Filter quotes by golfer")
        print("3. Search quotes by keyword")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            display_random_quote()
        elif choice == "2":
            name = input("Enter golfer's name: ").strip()
            filter_by_golfer(name)
        elif choice == "3":
            keyword = input("Enter a word or phrase from the quote: ").strip()
            filter_by_keyword(keyword)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

# Save the script file for the user
script_path = "/mnt/data/golf_quote_generator.py"
with open(script_path, "w") as f:
    f.write(
        f"import json\nimport random\n\nquotes = {json.dumps(quotes, indent=4)}\n\n"
        + display_random_quote.__code__.co_code.decode(errors='ignore')
        + filter_by_golfer.__code__.co_code.decode(errors='ignore')
        + filter_by_keyword.__code__.co_code.decode(errors='ignore')
        + main.__code__.co_code.decode(errors='ignore')
    )

script_path
