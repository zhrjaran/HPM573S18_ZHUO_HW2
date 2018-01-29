import HUI3 as eq

print("Score for ", [1, 1, 2, 4, 5, 3, 3, 4])
print(eq.getScore(vision=1, hearing=1, speech=2, ambulation=4, dexterity=5, emotion=3, cognition=3, pain=4))


print("Score for ", [1, 1, 2, 4, 7, 3, 3, 4])
print(eq.getScore(vision=1, hearing=1, speech=2, ambulation=4, dexterity=7, emotion=3, cognition=3, pain=4))
