def main(a):
    """
    If the number is positive, increase it to 1,if the number is negative decrease it to 2.
    If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    if a>0:
        return a+1
    elif a<0:
        return a-2
    else:
        return 10
print(main(-9))
print(main(3))
print(main(0))