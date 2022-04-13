class Time:
    def __add__(self,obj):
        temp = Time()
        temp.hr = self.hr +obj.hr
        temp.min = self.min+obj.min
        while(temp.min>=60):
            temp.hr = temp.hr+1
            temp.min = temp.min-60
        print(temp.hr,"Hours",temp.min,"Minutes")
    def __init__(self,min=0,hr=0):
         self.min = min
         self.hr = hr
T1 = Time(41,1)
T2 = Time(21,1)
T3 = T1+T2
