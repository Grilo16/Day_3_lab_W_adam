chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]


def getEggs(banana):
    bubbles = 0

    for ducky in banana:
        bubbles += ducky["eggs"]
        ducky["eggs"] = 0 # eggs have been collected

    return f"{bubbles} eggs collected, and no chickens were severely harmed in the process"


print(getEggs(chickens))