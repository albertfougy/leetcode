class ListNode:
    """Definition for a singly-linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None


def to_int(node):
    """Create an integer from a linked list with the head representing
    the smallest digit."""
    placeholder = ""
    while node is not None:
        placeholder += str(node.val)
        node = node.next
    return int(placeholder[::-1])


def to_ListNode(s):
    """Take a number represented as a string and parse it back into a
    linked list with the head representing the smallest digit."""
    head = prev = ListNode(0)
    for char in s:
        head.next = ListNode(int(char))
        head = head.next
    return prev.next


def addTwoNumbers(l1, l2):
    """Given two non-empty linked lists representing two 
    non-negative integers. The digits are stored in reverse order and 
    each of their nodes contain a single digit. Add the two numbers and
    return it as a linked list."""
    added = to_int(l1) + to_int(l2)
    reverse_str = str(added)[::-1]
    return to_ListNode(reverse_str)


# Unit testing
def list_to_str(num_list):
    """Convert a list of non-negative numbers to a string."""
    str_list = [str(n) for n in num_list]
    return "".join(str_list)


def list_to_node(num_list):
    """Convert a list of non-neagtive numbers to a singly-linked list."""
    num_str = list_to_str(num_list)
    node = to_ListNode(num_str)
    return node


def isIdentical(node1, node2):
    """Check if two singly-linked lists are equivalent."""
    if node1 is None and node2 is None:
        return True
    if node1 is not None and node2 is not None:
        return node1.val == node2.val and isIdentical(node1.next, node2.next)
    return False


def test_1():
    given1 = list_to_node([2, 4, 3])
    given2 = list_to_node([5, 6, 4])
    expected = list_to_node([7, 0, 8])
    actual = addTwoNumbers(given1, given2)
    assert isIdentical(actual, expected)
    assert isinstance(actual, ListNode)

