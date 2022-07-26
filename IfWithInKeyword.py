movies_watched = {"Inseption", "Sultan", "Anand"}
user_movie = input("Enter something you've watched recently: ")
print(user_movie)
if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")
