class vehicle:
    def __init__(self,maxspeed,mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage
modelX=vehicle(240,18)
print(modelX.maxspeed,modelX.mileage)