# class abc:
#     def __init__(self,number):
#         self.number=number
#     def largest(self):
#         return max(self.number,default=None)
# number=[23,56,78,89,45]
# processor=abc(number)
# print(processor.largest())


class abc:
    def __init__(self,number):
        self.number=number
    def odd(self):
        odd=[num for num in self.number if num %2!=0]
        print(odd)
    def even(self):
        even=[num for num in self.number if num%2==0]
        print(even)
number=[1,2,3,4,5,6,7,8,9,10]
processor=abc(number)
processor.odd()
processor.even()