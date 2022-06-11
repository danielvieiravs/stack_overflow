rooms = {
   "Patio": {"East": "Main Lobby"},
   "Main Lobby": {
       "North": "Vegetas Study",
       "West": "Patio", "South":
       "Trunks Bedroom", "East":
       "Research Room #1",
   },
   "Vegetas Study": {"East": "Backyard", "South": "Main Lobby"},
   "Backyard": {"West": "Vegetas Study"}, 
   "Trunks Bedroom": {"North": "Main Lobby", "East": "Playroom"},
   "Playroom": {"West": "Trunks Bedroom"},
   "Research Room #1": {"West": "Main Lobby", "North": "Research Room #2"},
   "Research Room #2": {"South": "Research Room #2"}
}

current_room = rooms["Patio"]

print("Frieza Attacks!")
print("Move commands: go North, go East, go South, go West")
print("--------------------")
print("You are on the Patio")

while True:
    direction = input("Which direction do you want to go?")

    match direction:

        case "go North":
            print("Not implemented")

        case "go East":
            room_key = current_room["East"]

            current_room = rooms[room_key]

            print(f"You are in the {room_key}")

        case "go South":
            print("Not implemented")

        case "go West":
            print("Not implemented")

        case "Exit":
            print("Thanks for playing!")

            break

        case _:
            print('Invalid direction')

