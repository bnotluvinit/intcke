import unittest


def merge_lists(my_list, alices_list):

    # Set up our merged list

    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:
        is_my_list_done = current_index_mine >= len(my_list)
        is_alice_list_done = current_index_alices >= len(alices_list)

        if not is_my_list_done and (is_alice_list_done or my_list[current_index_mine] < alices_list[current_index_alices]):
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine +=1
        else:
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices +=1

        current_index_merged +=1

    return merged_list


class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)