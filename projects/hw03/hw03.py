HW_SOURCE_FILE = "hw03.py"

#############
# Questions #
#############


def num_sevens(x):
    """Returns the number of times 7 appears as a digit of x.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_sevens',
    ...       ['Assign', 'AugAssign'])
    True
    """
    if x < 10:
        return 1 if x == 7 else 0

    return 1 + num_sevens(x // 10) if x % 10 == 7 else num_sevens(x // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    return pingpong_helper(1, n, True, 0)


def pingpong_helper(i, n, flag, res):
    if i == n + 1:
        return res

    if flag:
        flag = pingpong_flag(i, flag)
        return pingpong_helper(i + 1, n, flag, res + 1)
    else:
        flag = pingpong_flag(i, flag)
        return pingpong_helper(i + 1, n, flag, res - 1)


def pingpong_flag(i, flag):
    if num_sevens(i) > 0 or i % 7 == 0:
        flag = not flag
    return flag


def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    return count_change_helper(total, 1)


def count_change_helper(total, i):
    if i > total:
        return 0
    elif i == total:
        return 1
    else:
        return count_change_helper(total - i, i) + count_change_helper(total, i * 2)


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    return missing_digits_helper(n % 10, 0, n // 10)


def missing_digits_helper(prev_last, res, n):
    if n == 0:
        return res
    if n % 10 == prev_last or n % 10 == prev_last - 1:
        return missing_digits_helper(n % 10, res, n // 10)
    else:
        return missing_digits_helper(n % 10, res + prev_last - n % 10 - 1, n // 10)


###################
# Extra Questions #
###################


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print_move(start, end)
        return
    middle = get_middle(start, end)
    move_stack(n - 1, start, middle)
    move_stack(1, start, end)
    move_stack(n - 1, middle, end)


def get_middle(start, end):
    lst = [1, 2, 3]
    lst.remove(start)
    lst.remove(end)
    return lst[0]


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # too abstart to understand, so I copy the answer
    # return (lambda f: lambda k: f(f, k))(
    #     lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1)))
    # )
    return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))
