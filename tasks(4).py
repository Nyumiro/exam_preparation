class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


leaf = Node('leaf')
node_1 = Node('node1', left=leaf)
node_2 = Node('node2', left=node_1, right=Node('leaf2'))


def depth_first(tree):
    if tree is None:
        return
    print(tree.value)
    depth_first(tree.left)
    depth_first(tree.right)


''' Выводим поиск в глубину: '''
depth_first(node_2)
print('\n')


def breadth_first(tree):
    if tree is None:
        return
    queue = [tree]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


''' Выводим поиск в ширину: '''
breadth_first(node_2)
