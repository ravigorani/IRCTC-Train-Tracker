import requests
class IRCTC:
    def __init__(self):
        user=input("""How would you proceed?
        1. Enter 1 Check Trains From Your Station
        2. Enter 2 Check PNR
        3. Enter 3 Check Station of Your Train\n""")
        if user=="1":
            station_code=input("Enter the Station Code ")
            self.train_search(station_code)
        elif user=="2":
            pnr_no=input("Enter the PNR No. ")        
            self.pnr_check(pnr_no)
        else:
            train_no=input("Enter the Train No. ")        
            self.train_dtl(train_no)

    def train_search(self,station_code):
        data=requests.get("https://indianrailapi.com/api/v2/AllTrainOnStation/apikey/0d91d93fe6537f7c13c34d1d8733cb16/StationCode/{}".format(station_code)).json()
        for i in data["Trains"]:
            print("Train No.:",i["TrainNo"]," | Train Name:",i["TrainName"]," | Arrival Time:",i["ArrivalTime"],"| Departure Time:",i["DepartureTime"],"\n")
            
    def pnr_check(self,pnr_no):
        data=requests.get("https://indianrailapi.com/api/v2/PNRCheck/apikey/0d91d93fe6537f7c13c34d1d8733cb16/PNRNumber/{}".format(pnr_no)).json()
        print(data["Message"])
    
    def train_dtl(self,train_no):
        data=requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/0d91d93fe6537f7c13c34d1d8733cb16/TrainNumber/{}".format(train_no)).json()
        for i in data["Route"]:
            print(i["StationName"],"| Arrival Time:",i["ArrivalTime"],"| Departure Time:",i["DepartureTime"],"| Distance Travelled:",i["Distance"],"\n")
obj=IRCTC()
obj