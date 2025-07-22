class Taxi:

    def __init__(self, pickup_location, drop_location, pickup_time, drop_time, earnings, taxiId, customerId, current_location = "A"):
        self.__drop_time = drop_time
        self.__taxiId = taxiId
        self.__current_location = current_location
        self.__pickup_location = pickup_location
        self.__drop_location = drop_location
        self.__pickup_time = pickup_time
        self.__earnings = earnings
        self.__customerId = customerId

    def get_taxiId(self):
        return self.__taxiId

    def set_taxiId(self, taxiId):
        self.__taxiId = taxiId

    def get_customerId(self):
        return self.__customerId

    def set_customerId(self, customerId):
        self.__customerId = customerId

    def get_current_location(self):
        return self.__current_location

    def set_current_location(self, current_location):
        self.__current_location=current_location

    def get_pickup_location(self):
        return self.__pickup_location

    def set_pickup_location(self, pickup_location):
        self.__pickup_location=pickup_location

    def get_drop_location(self):
        return self.__drop_location

    def set_drop_location(self, drop_location):
        self.__drop_location = drop_location

    def get_pickup_time(self):
        return self.__pickup_time

    def get_drop_time(self):
        return self.__drop_time

    def set_drop_time(self, time):
        self.__drop_time = time

    def set_pickup_time(self, pickup_time):
        self.__pickup_time = pickup_time

    def get_earnings(self):
        return self.__earnings

    def set_earnings(self, earnings):
        self.__earnings = earnings

    def string(self):
        return f" Taxi {self.__taxiId} \n Current location : {self.__current_location} \n Customer ID : {self.__customerId} \n Pickup location : {self.__pickup_location} \n Drop location {self.__drop_location} \n Pickup Time : {self.__pickup_time} \n Drop Time : {self.__drop_time} \n Earnings : {self.__earnings}"
