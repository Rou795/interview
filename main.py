class Stek:

    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, el):
        self.elements.insert(0, el)

    def pop(self):
        return self.elements.pop(0)

    def peek(self):
        return self.elements[0]

    def size(self):
        return len(self.elements)

    def get_els(self):
        return self.elements


def is_balance(elements: list) -> bool:
    stek = Stek()
    open_close_dict = {')': '(', '}': '{', ']': '['}
    for el in elements:
        if el in ['(', '{', '[']:
            stek.push(el)
        else:
            if stek.is_empty():
                return False
            else:
                if stek.pop() != open_close_dict[el]:
                    return False
    return True


def test():
    primers_good = ['(((([{}]))))', '[([])((([[[]]])))]{()}',
                    '{{[()]}}']

    primers_bad = ['}{}', '{{[(])]}}', '[[{())}]']

    for primer in primers_good:
        assert is_balance(list(primer)) == True

    for primer in primers_bad:
        assert is_balance(list(primer)) == False


if __name__ == '__main__':
    test()
