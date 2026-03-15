from Deque import Deque

print("testing push_front and push_back")

d=Deque(2)
d.push_back(7)
d.push_front(3)
print(d.to_list())

deq=Deque(2)
deq.push_back(9)
deq.push_front(4)
deq.push_back(23)
print(deq.to_list())


print("testing pop_back and pop_front")


deq.pop_back()
deq.pop_back()
deq.pop_front()
d.pop_front()
print(deq.to_list())
print(d.to_list())


print("testing peek_front and peek_back")

print(deq.peek_front())
print(deq.peek_back())
print(d.peek_front())
print(d.peek_back())

print("testing is_empty and is_full and massive_size")

print(deq.is_empty())
print(d.is_full())
print(deq.massive_size())
print(d.massive_size())

print("testing to_list")
print(d.to_list())
