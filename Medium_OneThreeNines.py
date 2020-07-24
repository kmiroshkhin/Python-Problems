"""
Given an int, figure out how many ones, threes and nines you could fit into the number.
You must create a class. You will make variables(self.ones, self.threes, self.nines) to do this.
"""



class OneThreeNines:
        def Ones(self,number):
            entries = number/1
            return round(entries-0.5)
        def Three(self,number):
            entries = number/3
            return round(entries-0.5)
        def Nine(self,number):
            entries = number/9
            return round(entries-0.5)
