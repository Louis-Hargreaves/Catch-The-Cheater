import random

class cheater_game():
    def __init__(self):
        self.flips = 100
        self.points = 0
        self.blob = self.produce_new_blob()

    def add_flips(self):
        self.flips += 15

    def remove_flips(self):
        self.flips -= 30

    def add_points(self):
        self.points += 1

    def produce_new_blob(self):
        choice = str(random.choice(["Cheater", "Fair"]))
        return choice

    def flip_coin(self):
        if self.blob == "Cheater":
            head_probability = 0.75
        else:
            head_probability = 0.5
        flip_outcome = random.choices(["Head", "Tails"], weights=[head_probability, 1 - head_probability])
        return flip_outcome

def play():
    ongoing_game = cheater_game()
    while ongoing_game.flips > 0:
        decision = input('''
            Type a positive whole number in order to flip a coin a set amount of times.
            To call out a cheater, type "C". To call out a fair blob, type "F".
        :''')

        if (decision == "C" and ongoing_game.blob == "Cheater") or (decision == "F" and ongoing_game.blob == "Fair"):
            ongoing_game.add_flips()
            ongoing_game.add_points()
            print("Correct! You chose:", ongoing_game.blob)
            ongoing_game.blob = ongoing_game.produce_new_blob()
        elif (decision == "C" and ongoing_game.blob == "Fair") or (decision == "F" and ongoing_game.blob == "Cheater"):
            ongoing_game.remove_flips()
            print("Incorrect! You didn't choose:", ongoing_game.blob)
            ongoing_game.blob = ongoing_game.produce_new_blob()

        else:
            try:
                #Converts the decision into a number that can be processed by python
                #it also finds the modulus (remainder) when number of flips specified is divided by total flips available.
                decision = int(decision) % ongoing_game.flips
                ongoing_game.flips = ongoing_game.flips - decision
            except:
                print("You probably didn't enter a valid character.")
            for n in range(1, decision+1):
                print(ongoing_game.flip_coin())
        print("You have {0} point/points and {1} flip/flips remaining".format(ongoing_game.points, ongoing_game.flips))



play()