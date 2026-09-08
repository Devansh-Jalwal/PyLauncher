
import os
import urllib.parse
import webbrowser

def open_google_weather(city_name):
    search_query = f"weather in {city_name}"
    encoded_query = urllib.parse.quote_plus(search_query)

    google_url = f"https://www.google.com/search?q={encoded_query}"

    print(f"Opening weather search for '{city_name}'...")

    if webbrowser.open(google_url, new=2):
        print("Search opened successfully!")
    else:
        print("Could not open the default browser.")


def main():
    print()
    print("===================================")
    print("       Welcome to Weather App")
    print("                 v1.0")
    print("===================================")
    print()

    choice = input(
        "This will open your default browser.\n"
        "Press 'y' to continue or 'n' to exit: "
    ).strip().lower()

    if choice != "y":
        print("See you!")
        return

    print()

    user_city = input("Enter a city name: ").strip()

    if not user_city:
        print("City name cannot be empty.")
        return

    open_google_weather(user_city)


if __name__ == "__main__":
    main()

