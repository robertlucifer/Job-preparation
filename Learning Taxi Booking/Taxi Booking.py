from Taxi import Taxi

class TaxiBooking:
    taxilist = []  # Static list to store taxis
    taxibookinghistory = []  # Static list to store booking history
    taxi_limit = 4  # Maximum number of taxis
    id_generator = 1  # For generating unique customer IDs

    @classmethod
    def booking(cls, pickup_location, drop_location, pickup_time):
        # Create new taxis if below limit
        if len(cls.taxilist) < cls.taxi_limit:
            cls.taxilist.append(Taxi(pickup_location, drop_location, pickup_time, 0, 0, len(cls.taxilist) + 1,0))

        min_distance = float('inf')
        taxi_ready = None

        # Find the nearest available taxi
        for taxi in cls.taxilist:
            if (taxi.get_drop_time() <= pickup_time and
                    abs(ord(pickup_location) - ord(taxi.get_current_location())) <= min_distance):

                if abs(ord(pickup_location) - ord(taxi.get_current_location())) == min_distance:
                    # If distances are equal, choose taxi with lower earnings
                    if taxi_ready is not None and taxi.get_earnings() < taxi_ready.get_earnings():
                        taxi_ready = taxi

                else:
                    taxi_ready = taxi
                    min_distance = abs(ord(pickup_location) - ord(taxi.get_current_location()))

        if taxi_ready is not None:
            # Update taxi details
            taxi_ready.set_customer_id(cls.id_generator)
            cls.id_generator += 1
            taxi_ready.set_pickup_time(pickup_time)
            taxi_ready.set_pickup_location(pickup_location)
            taxi_ready.set_drop_location(drop_location)
            taxi_ready.set_current_location(drop_location)

            # Calculate drop time and earnings
            distance = abs(ord(drop_location) - ord(pickup_location))
            taxi_ready.set_drop_time(pickup_time + distance)
            taxi_ready.set_earnings(taxi_ready.get_earnings() + (distance * 15 - 5) * 10 + 100)
            taxi_ready.set_taxi_id(cls.taxilist.index(taxi_ready) + 1)

            # Add to history (create a new instance to simulate clone)
            cls.taxibookinghistory.append(
                Taxi(
                    taxi_ready.get_pickup_location(),
                    taxi_ready.get_drop_location(),
                    taxi_ready.get_pickup_time(),
                    taxi_ready.get_drop_time(),
                    taxi_ready.get_earnings(),
                    taxi_ready.get_taxi_id(),
                    taxi_ready.get_current_location()
                )
            )

            return f"Taxi number {taxi_ready.get_taxi_id()} is booked!"

        return "Taxis not available"

    @staticmethod
    def display():
        print("-----------------")
        for taxi in TaxiBooking.taxibookinghistory:
            print(str(taxi))
            print("-----------------")