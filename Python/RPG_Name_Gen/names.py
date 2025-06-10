import random
import json

"""
Just a simple name generator for personal use. Will generate names based on different genres.

In the future, I think I'll put it on my git website, but for now, it's just a personal project.
"""

def get_first_name(genre: str = 'Normal') -> str:
    """Get a first name based on the specified genre."""
    with open('first_names.json', 'r') as file:
        first_names = json.load(file)
    
    if genre not in first_names:
        raise ValueError(f"Genre '{genre}' not found in first names data.")
    
    return random.choice(first_names[genre])

def get_middle_name(genre: str = 'Normal') -> str:
    """Get a middle name based on the specified genre."""
    with open('middle_names.json', 'r') as file:
        middle_names = json.load(file)
    
    if genre not in middle_names:
        raise ValueError(f"Genre '{genre}' not found in middle names data.")
    
    return random.choice(middle_names[genre])

def get_last_name(genre: str = 'Normal') -> str:
    """Get a last name based on the specified genre."""
    with open('last_names.json', 'r') as file:
        last_names = json.load(file)
    
    if genre not in last_names:
        raise ValueError(f"Genre '{genre}' not found in last names data.")
    
    return random.choice(last_names[genre])

def get_full_name(genre: str = 'Normal', middle: bool = True) -> str:
    """Generate a full name based on the specified genre and whether to include a middle name."""
    genres = ['Normal', 'Fantasy', 'Cyberpunk', 'Sci-Fi']
    if genre == "Random":
        genre = random.choice(genres)

        first_name = get_first_name(genre)
        middle_name = get_middle_name(genre)
        last_name = get_last_name(genre)

    elif genre == "Super Random":
        first_name = get_first_name(random.choice(genres))
        middle_name = get_middle_name(random.choice(genres))
        last_name = get_last_name(random.choice(genres))

    else:
        first_name = get_first_name(genre)
        middle_name = get_middle_name(genre)
        last_name = get_last_name(genre)
    
    if not middle:
        return f"{first_name} {last_name}"

    return f"{first_name} {middle_name} {last_name}"

def test_get_full_name():
    """Test the get_full_name function with various genres and middle name options."""
    print("Testing get_full_name function with various genres and middle name options:")
    try:
        print(get_full_name('Normal', True))
        print(get_full_name('Fantasy', False))
        print(get_full_name('Cyberpunk', True))
        print(get_full_name('Sci-Fi', False))
        print(get_full_name('Random', True))
        print(get_full_name('Super Random', False))
    except ValueError as e:
        print(e)

def generate_names(num_names: int = 10, genre: str = 'Normal', middle: bool = True):
    """Generate a list of full names based on the specified genre and middle name option."""
    names = []
    for _ in range(num_names):
        names.append(get_full_name(genre, middle))
    return names

def main():
    genre = input("Enter the genre (Normal, Fantasy, Cyberpunk, Sci-Fi, Random, Super Random): ")
    middle = input("Include middle name? (yes/no): ").strip().lower() == 'yes'   

    try:
        names = generate_names(10, genre, middle)
        print(f"Generated {len(names)} names:")
        print("---------------------")
        for name in names:
            print(name)
        print("---------------------")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
    # Uncomment the line below to run the test function
    # test_get_full_name()