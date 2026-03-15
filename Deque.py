class Deque:
    def __init__(self,capacity):
        self.capacity=capacity
        self.data=[None]*capacity
        self.front=0
        self.back=-1
        self.size=0

    def push_front(self,value):
        if self.size==self.capacity:
            print("Массив уже полный")
            return
        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.size += 1

    def push_back(self,value):
        if self.size==self.capacity:
            print("Массив уже полный")
            return
        self.back=(self.back + 1) % self.capacity
        self.data[self.back] = value
        self.size+=1

    def pop_front(self):
        if self.size==0:
            return None
        value=self.data[self.front]
        self.front=(self.front + 1) % self.capacity
        self.size-=1
        return value


    def pop_back(self):
        if self.size==0:
            return None
        value=self.data[self.back]
        self.back=(self.back - 1) % self.capacity
        self.size-=1
        return value


    def peek_front(self):
        if self.size==0:
            return None
        value=self.data[self.front]
        return value

    def peek_back(self):
        if self.size==0:
            return None
        value=self.data[self.back]
        return value



    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.size==self.capacity:
            return True
        else:
            return False

    def massive_size(self):
        return self.size


    def to_list(self):
        lst=[]
        for i in range(self.size):
            index = (self.front + i) % self.capacity
            lst.append(self.data[index])
        return lst






