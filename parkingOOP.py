#OOP Parking Garage

class SomervilleParking():

    def __init__(self, arrive, space, ticket):
        self.arrive = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8", "I9", "J10"]
        self.space = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8", "I9", "J10"]
        self.ticket = { "False": "A1", "False": "B2", "False": "C3", "False": "D4", "False": "E5", 
                            "False": "F6", "False": "G7", "False": "H8", "False": "I9", "False": "J10"}
        
    #take ticket and enter
    def enter(self, arrive, space):
        print("Welcome to our parking garage! Please take a ticket and the corresponding space.")
        for arrive in self.arrive:
            self.arrive.remove(arrive)
        for space in self.space:
            self.space.remove(space)
    
    #leave garage
    def leave(self):
        if self.ticket:
            print("Thank you, please come back to Somerville")
        else:
            hours = input(int("How many hours were you parked for? "))
            rate = 10
            if hours > 0:
                cost = int(hours) * rate
                print("You owe: ", cost)
                response = input("To pay type 'y' ")
                if response.lower() == 'y':
                    print("Thank you for using Somerville Parking, please come again")
                    self.ticket["True"] = self.ticket.pop("False")
                else:
                    print("Error, please enter 'y', or 'n'.")
            else:
                print("Error, please enter 'y', or 'n'.")
        for arrive in self.arrive:
            self.arrive.append(arrive)
        for space in self.space:
            self.space.append(space)
    
    #calculate and take payment
    def pay(self):
        hours = input("How many hours were you parked for? ")
        if int(hours) > 0:
            cost = int(hours) * 10
            print(f"You owe $", cost)
            response = input("To pay type 'y' " )
            if response.lower() == 'y':
                print("Thank you, please leave the garage in the next 5 mins")
                self.ticket["True"] = self.ticket.pop("False")
            elif response.lower() == 'n':
                noResponse = input("No problem, its $10 per hour so feel free to stay longer. Otherwise type 'y' to pay")
                if noResponse.lower() == 'y':
                    print("Thank you, please leave the garage in the next 5 mins")
                    self.ticket["True"] = self.ticket.pop("False")
                elif noResponse == 'n':
                    print("Sorry, we're impounding your car. See our partners at Somerville Pound to retieve your car and pay the fine")
                    self.ticket["True"] = self.ticket.pop("False")
            else:
                print("Error, please enter 'y', or 'n'.")
        else:
            print("Maybe try your luck in Cambridge!")


class UI(SomervilleParking):
    def ___int__(self):
        super().__init__()

    def run():
        somervilleParking = SomervilleParking([], [], {})
        print("Welcome to Someville Parking, only $10 per hour!")
        while True:
            ticketResponse = input("Would you like to park in Somerville today? Type 'y' or 'n'. " )
            if ticketResponse.lower() == "y":
                somervilleParking.enter([], [])
                while True:
                    payResponse = input("Would you like to pay for your parking time and leave? Type 'y' or 'n'. ")
                    if payResponse.lower() == "y":
                        somervilleParking.pay()
                        while True:
                            leaveResponse = input("Would you like to leave? Type 'y' or 'n'.")
                            if leaveResponse.lower() == "y":
                                somervilleParking.leave()
                                break
                            elif leaveResponse.lower() == "n":
                                print("No problem, its $10 per hour so feel free to stay longer")
                                somervilleParking.pay()
                            else:
                                print("Error, please enter 'y', or 'n'.")
                    elif payResponse.lower() == "n":
                        print("No problem, its $10 per hour so feel free to stay longer")
                        somervilleParking.pay
                    else:
                        print("Error, please enter 'y', or 'n'.")
            elif ticketResponse.lower() == "n":
                print("Maybe try your luck in Cambridge!")
                break
            else:
                print("Error, please enter 'y', or 'n'.")

def main():
    UI.run()

if __name__ == "__main__":
    main()