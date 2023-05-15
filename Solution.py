from decimal import Decimal
import cmath

def num_of_digits(n): #function declaration that accepts input
    """
    This function calculates the number of digits in the integer part of a number.

    Args:
        n: The number to calculate the number of digits for.

    Returns:
        int: The number of digits in the integer part of the number.
    """
    
    # 1- Convert the number to a string to check all edge test cases
    str_n = str(n)
    
    # 2- Check if the number is negative
    if str_n[0] == '-':
        str_n = str_n[1:]
        
    # 3- Check if the number is complex 'contains j'
    if 'j' in str_n:
        # If complex, split into real and imaginary parts and count digits
        parts = str_n.replace('j', '').split('+') if '+' in str_n else str_n.replace('j', '').split('-')
        return sum(len(part) for part in parts)
    
    # Split the number into integer and decimal parts
    parts = str_n.split('.')
    
    # 4- The number of digits in the integer part is the length of the first part
    return len(parts[0])


#Test function to test different inputs and test cases
def test_num_of_digits():

    #writing test cases for all possible types of inputs also writing the respective statement If a test case failed
    assert num_of_digits(100) == 3, "Test case 1 failed"
    assert num_of_digits(999) == 3, "Test case 2 failed"
    assert num_of_digits(-10) == 2, "Test case 3 failed"
    assert num_of_digits(3.1415) == 1, "Test case 4 failed"
    assert num_of_digits(0) == 1, "Test case 5 failed"
    assert num_of_digits(-0.5) == 1, "Test case 6 failed"
    assert num_of_digits(Decimal('10.5')) == 2, "Test case 7 failed"
    assert num_of_digits(cmath.sqrt(-1)) == 1, "Test case 8 failed"
    print("All test cases passed")

# Testing the function
test_num_of_digits()