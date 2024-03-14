class obj:
    def __init__(self, signature):
        self.signature = signature
    
    def __repr__(self)-> str:
        return str(self.signature)
class_list = []

for i in range(10):
    class_list.append(obj(i))

print (class_list) #outputs [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]