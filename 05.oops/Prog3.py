class Student:
    def __init__(self,name,mathScore,phyScore,compScore):
        self.name=name
        self.mathScore=mathScore
        self.phyScore=phyScore
        self.compScore=compScore
    
    def total(self):
        return self.mathScore+self.phyScore+self.compScore
    
    def average(self):
        return self.total()/3

    def grade(self):
        avg = self.average() 
        if self.mathScore < 35 or self.phyScore < 35 or self.compScore < 35:
            return ("Grade is FAIL")
        elif avg >= 90:
            return ("Grade is outstanding")
        elif avg >= 70:
             return ("Grade is proficient")
        else:
             return ("Grade is aspirannt")
        
s1 = Student("Sukanya",100,90,80)
print("s1 is a student called {} and her total is {}, avg is {} and grade is {}.".format(s1.name,s1.total(),s1.average(),s1.grade()))
