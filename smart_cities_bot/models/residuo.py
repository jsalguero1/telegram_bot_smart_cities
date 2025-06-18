import datetime
class Residuo:
    
    def __init__(self, file_id, latitude, longitude):
        current_date = datetime.datetime.now()
        self.date = current_date.date()
        self.time = current_date.time()
        self.file_id = file_id
        self.latitude = latitude
        self.longitude = longitude
        #self.plastic_bottle = plastic_bottle
    
    #def toggle_plastic_bottle(self):
    #    self.plastic_bottle = not self.plastic_bottle