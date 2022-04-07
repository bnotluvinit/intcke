def contains_cycle(first_node):
    slow_runner = first_node
    fast_runner = first_node

    # Until we hit end of list
    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if fast_runner is slow_runner:
            return True

    return False