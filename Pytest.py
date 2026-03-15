from Deque import Deque


def testing_push():
    d = Deque(2)
    d.push_back(7)
    d.push_front(3)
    print(d.to_list())


def testing_pop():
    d = Deque(2)
    d.push_back(10)
    d.push_back(20)

    print(d.pop_back())
    print(d.pop_front())
    print(d.pop_front())


def testing_peek():
    d = Deque(2)
    d.push_back(5)
    d.push_back(8)

    print(d.peek_front())
    print(d.peek_back())


def testing_empty_full_massive_size():
    d = Deque(2)

    print(d.is_empty())

    d.push_back(1)
    d.push_back(2)

    print(d.is_full())
    print(d.massive_size())


def testing_to_list():
    d = Deque(3)
    d.push_back(1)
    d.push_back(2)
    d.push_front(0)

    print(d.to_list())


def main():
    testing_push()
    testing_pop()
    testing_peek()
    testing_empty_full_massive_size()
    testing_to_list()


if __name__ == "__main__":
    main()
