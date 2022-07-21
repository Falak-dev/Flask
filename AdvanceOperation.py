friends = {"Bob", "Rolf", "Anne"}
Aboad =  {"Bob", "Anne"}

local_friends = friends.difference(Aboad)
print(local_friends)

local_friends = friends.intersection(Aboad)
print(local_friends)

fr = {"Anne"}
Ab =  {"Bob"}

local = fr.union(Ab)
print(local)

