"""
Name: Abe Weber
Date: 11/6/24
Topic: Functions with parameters
"""

def sunny_message():
    print("On a sunny day, sandals are appropriate footwear")
def rainy_message():
    print("On a rainy day, galoshes are appropriate footwear")
def snowy_message():
    print("On a snowy day, boots are appropriate footwear")

def main():
    user_weather = input("What is the weather? (sunny,rainy,snowy): ")

    if user_weather == "sunny":
        sunny_message()
    elif user_weather == "rainy":
        rainy_message()
    elif user_weather == "snowy":
        snowy_message()


if __name__ == '__main__':
    main()
