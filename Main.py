from Deque import Deque

if __name__ == "__main__":
    d = Deque(7)
    d.push_front(14)
    d.push_back(3)

    print("peek_front =", d.peek_front())
    print("peek_back =", d.peek_back())
    print("pop_front =", d.pop_front())
    print("pop_back =", d.pop_back())
    print("is_empty =", d.is_empty())
    print("is_full =", d.is_full())
    print("massive_size =", d.massive_size())
    print("to_list =", d.to_list())