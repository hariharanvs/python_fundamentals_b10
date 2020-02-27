class ipl:
    
    def __init__(self,team,city):
        self.team = team
        self.city = city
        
        print("Team Name and City mapped")
        
    def bat(self):
     print(f"{self.team.title()} is batting")
        
    def bowl(self):
        print(f"{self.team.title()} is bowling")