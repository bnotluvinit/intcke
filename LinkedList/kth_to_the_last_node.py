import unittest


def kth_to_last_node(k, head):
    if k < 1:
        raise ValueError('Impossible to find less than first to last node')
    left_node = head
    right_node = head

    #Move right_node to the kth node

    for _ in range(k - 1):
    # But along the way, if a right_node doesn't have a next,
    # then k is greater than the length of the list and there
    # can't be a kth-to-last node! we'll raise an error

        if not right_node.next:
            raise ValueError(
                'k is larger than the length of the linked list: %s' % k
            )
        right_node = right_node.next

    while right_node.next:
        left_node = left_node.next
        right_node = right_node.next

        # Since left_node is k nodes behind right node
        # left node is now the kth to last node
    return left_node

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_first_to_last_node(self):
        actual = kth_to_last_node(1, self.first)
        expected = self.fourth
        self.assertEqual(actual, expected)

    def test_second_to_last_node(self):
        actual = kth_to_last_node(2, self.first)
        expected = self.third
        self.assertEqual(actual, expected)

    def test_first_node(self):
        actual = kth_to_last_node(4, self.first)
        expected = self.first
        self.assertEqual(actual, expected)

    def test_k_greater_than_linked_list_length(self):
        with self.assertRaises(Exception):
            kth_to_last_node(5, self.first)

    def test_k_is_zero(self):
        with self.assertRaises(Exception):
            kth_to_last_node(0, self.first)