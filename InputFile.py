class TakeInput():
    ResultUrl1="https://msbte.org.in/DISRESLIVE2021CRSLDSEP/COV6139QS21LIVEResult/SeatNumber/"
    ResultUrl2="Marksheet.html"
    def FirstInput(self):
        self.SeatRangeStart=int(input('Enter the Seat No Starting Range:::'))
        self.SeatRangeEnd=int(input('Enter the Seat No Ending Range:::'))
        self.Validate()
    def Validate(self):
        print(self.SeatRangeStart,"---",self.SeatRangeEnd,"\n")
        Choice=input("This is the SeatNo Range, Validate this?? (Y/N) \n")
        # Choice='Y'
        if Choice.upper() !='Y': 
            print(Choice.title())
            self.FirstInput()

   
