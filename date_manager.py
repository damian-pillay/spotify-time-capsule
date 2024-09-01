import os
import time
from datetime import datetime

CURRENT_YEAR = datetime.now().year

INTRO = f"Welcome to the Spotify Time Capsule!\n\nWhich year do you want to travel to?"

class DateManager():
    def __init__(self) -> None:
        self.date = None

    def is_valid_date(self, year, month, day):
            try:
                datetime(year, month, day)
                return True
            except ValueError:
                return False
    
    def get_date(self):
        while True:
            try:
                os.system("cls")
                print(INTRO)

                year = int(input("Type the year: "))
                if year not in range(1958, CURRENT_YEAR + 1):
                    os.system("cls")
                    print(f"{INTRO}\nERROR: Please Input A Valid Year")
                    time.sleep(1)
                    continue
            
                month = int(input("Type the month: ")) 
                if month not in range(1, 13):
                    os.system("cls")
                    print(f"{INTRO}\nERROR: Please Input A Valid Month")
                    time.sleep(1)
                    continue

                day = int(input("Type the day: "))
                if not self.is_valid_date(year, month, day):
                    os.system("cls")
                    print(f"{INTRO}\nERROR: Please Input A Valid Date") 
                    time.sleep(1)
                    continue   

                self.date = f"{year}-{month:02}-{day:02}"
                return self.date
            
            except ValueError:
                os.system('cls')
                print("Which year do you want to travel to?\n\nERROR: Please only type number inputs")
                time.sleep(2)
                pass

    