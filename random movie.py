import requests #pip install requests. if using arch linux then sudo pacman -S python-requests.
import random #pip install random. if using arch linux then sudo pacman -S python-random

def get_random_movie(genre_id=None):
    api_key = "c7ed2d320b0a3654a8a7a61aaa983a7d"  # Replace with your TMDb API key. get it from their official site
    base_url = "https://api.themoviedb.org/3/discover/movie"

    if genre_id is not None:
        genre_ids = {
            1: 28,   # Action
            2: 10749,  # Rom-com
            3: 18,   # Slice of life
            4: 10749,  # Romance
            5: 35,   # Comedy
            6: 18,   # Drama
            7: 12,   # Adventure
            8: 27,   # Horror
            9: 18,   # Emotional
        }
        genre = genre_ids.get(genre_id, 28)  # Default to action if an invalid genre is provided
    else:
        genre = None

    params = {
        'api_key': api_key,
        'with_genres': genre,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'results' in data and data['results']:
        random_movie = random.choice(data['results'])
        return random_movie['title'], random_movie['overview']
    else:
        return None

def main():
    while True:
        print("Alright, choose the genre of movie you want:")
        print("1. Action")
        print("2. Rom-com")
        print("3. Slice of life")
        print("4. Romance")
        print("5. Comedy")
        print("6. Drama")
        print("7. Adventure")
        print("8. Horror")
        print("9. Emotional")
        print("10. Any random movie")

        while True:
            try:
                genre_choice = int(input("Type the number corresponding to your choice: "))
                if 1 <= genre_choice <= 10:
                    break
                else:
                    print("Oopsie, please type a number between 1 and 10.")
            except ValueError:
                print("Oopsie, please type a valid number.")

        if genre_choice == 10:
            movie_title, movie_description = get_random_movie()
        else:
            movie_title, movie_description = get_random_movie(genre_choice)

        if movie_title and movie_description:
            print(f"\nHere is a random movie for the genre you've chosen:")
            print(f"Title: {movie_title}")
            print("Description:")
            print(movie_description)
        else:
            print("Oopsie, something went wrong. Please try again later.")

        while True:
            user_input = input("Want me to suggest any other movie? (yes or no): ").lower()
            if user_input == "yes":
                break
            elif user_input == "no":
                print("Okay, alright. Now run the program again if you want any random movie suggestion.")
                return
            else:
                print('Just type "yes" or "no" nothing else.')

if __name__ == "__main__":
    main()
