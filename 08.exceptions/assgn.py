
class NegativeSeatCountException(Exception):
    pass

class NotEnoughSeatsException(Exception):
    pass

class Train:
    def __init__(self,maxSeats):
        self.maxSeats=maxSeats
        self.seatsFilled=0

    def availableSeats(self):
        return (self.maxSeats-self.seatsFilled)

    def reserve(self,seatsCount):
        if seatsCount<0:
            raise NegativeSeatCountException
        if self.availableSeats()<seatsCount :
            raise NotEnoughSeatsException
        self.seatsFilled+=seatsCount

train = Train(60)
print("Bal Seats: {}",train.availableSeats())

shallContinue = True

while shallContinue:
    choice = input("Choose (r/q): ")

    try:
        if choice=="r" or choice=="R":
            seatsCount = int(input("Enter required seats: "))
            train.reserve(seatsCount)
        else:
            print("Unknown choice")
    except NotEnoughSeatsException as e:
        print("Sorry, We do not have thpse many seats! Avail-Seats:{}",train.availableSeats())
    except NegativeSeatCountException:
        print("seats-count entered cannot be in negative")

