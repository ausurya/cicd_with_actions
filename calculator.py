
def calculate(operation: str, x: int, y: int) -> int:
    """Function to perform an operation between 2 integers

    Args:
        operation (str): can be addition, subtraction, multiplication, division
        x (int): first integer to perform operation on
        y (int): second integer to perform operation on

    Returns:
        int: result of the oepration performed on 2 integers
    """
    if operation == "addition":
        return x+y
    
    if operation == "subtraction":
        return x-y
    
    if operation == "multiplication":
        return x*y
    
    if operation == "division":
        return x/y


    
    