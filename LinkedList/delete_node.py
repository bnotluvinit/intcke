def delete_node(node_to_delete):
    # Get the input node's next node, the one we want to skip to

    next_node = node_to_delete.next

    if next_node:
        # Replace the input node's value and pointer with the next nodes value and pointer.
        # The previous node is now effecively skips over the input

        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next

    else:
        raise Exception