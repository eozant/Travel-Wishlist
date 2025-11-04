places = ["Japan", "Iceland", "New Zealand", "Norway", "Canada"]

print(places)

places.append("Australia")

places.insert(1, "Italy")

places.pop()

places.remove("New Zealand")

places[2] = "South Korea"

places.sort()

places.reverse()

for place in places:

    print(f"- {place}")
