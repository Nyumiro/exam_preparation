class LinkedItem:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


a = LinkedItem(10)
b = LinkedItem(11, a)
c = LinkedItem(12, b)

q = c.next


def print_linked(elem):
    while elem is not None:
        print(elem.value)
        elem = elem.next


def to_LinkedList(s):
    l = None
    for i in range(len(s) - 1, -1, -1):
        l = LinkedItem(s[i], l)
    return l


string = 'Надежда'
item = to_LinkedList(string)
print_linked(item)


def removeLinked(items):
    if items is None:
        return items
    end = removeLinked(items.next)
    if items.value in 'ауоыэяюёиеАУОЫЭЯЮЁИЕ':
        return end
    return LinkedItem(items.value, end)


new_item = removeLinked(to_LinkedList(string))
print_linked(new_item)


# 10 задача

def list3_to2(one, two, three):
    queue = []
    for i in range(len(one)):
        queue.append(one[i])
        queue.append(two[i])
        queue.append(three[i])

    list_one = []
    list_two = []

    while len(queue) > 0:
        list_one.append(queue.pop(0))
        if len(queue) > 0:
            list_two.append(queue.pop(0))
    return list_one, list_two


print(list3_to2([1, 2, 3], ['a', 'b', 'c'], ['!', '&', '.']))
