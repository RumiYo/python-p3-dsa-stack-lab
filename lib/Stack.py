class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stach is full. Cannot push more items.")

    def pop(self):
        if len(self.items) > 0 :
            return self.items.pop()
        else: 
            return None

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        i = len(self.items) - 1

        while i >= 0:
            if self.items[i] == target: 
                return len(self.items) - i - 1
            else:
                if i > 0:
                    i -= 1
                else: 
                    return -1
            
