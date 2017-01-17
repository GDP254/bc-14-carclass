class Car(object):
    
    speed = 0
    num_of_doors = 4
    num_of_wheels = 4
    top_speed = 1000.0
    max_throttle = 3.0
    throttle_response = 0
    
    #Constructor
    def __init__(self, name = 'General', model = 'GM', body_type = 'saloon'):
        #Clean all imput
        inpt = [name, model, body_type]
        for i in inpt:
          if not type(i) is str:
            raise ValueError("Invalid input on Car Creation")
      
        self.name = name
        self.model = model
        self.body_type = body_type

        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            self.num_of_doors = 2

        if self.body_type == 'trailer':
            self.num_of_wheels = 8
            self.top_speed = 77.0
            self.max_throttle = 7.0
        self.throttle_response = self.top_speed / self.max_throttle

    def is_saloon(self):
        if self.body_type == 'saloon':
            return True
        else:
            return False

    def drive(self, throttle):
        if type(throttle) is int:
            if throttle <= self.max_throttle and throttle > 0:
                self.speed = int(round(throttle * self.throttle_response))
            return self
        else:
            raise ValueError("Invalid input on drive")
