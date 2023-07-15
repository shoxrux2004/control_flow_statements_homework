def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>9 and a<100 and a%2==1:
        return "two-digit odd number"
    if a>9 and a<100 and a%2==0:
        return "two-digit even number"
    if a>99 and a<1000 and a%2==1:
        return "three-digit odd number"
    if a>99 and a<1000 and a%2==0:
        return "three-digit even number"
print(main(57))
print(main(242))