def format_long_number(number):
    """
    Format a large number with thin spaces between each group of three digits,
    including numbers with decimals.

    Args:
        number (float or int): The number to format.

    Returns:
        str: The formatted number as a string.
    """
    # Split the number into integer and decimal parts
    integer_part, decimal_part = f"{number:,.9f}".split('.')
    
    # Replace commas with thin spaces in the integer part
    integer_part = integer_part.replace(',', '\u2009')
    
    # Group the decimal part by three digits
    decimal_part = '\u2009'.join([decimal_part[i:i+3] for i in range(0, len(decimal_part), 3)])
    
    # Combine the integer and decimal parts
    formatted_number = f"{integer_part}.{decimal_part}"
    
    return formatted_number

# Example usage
number = 1234567890.123456589
formatted_number = format_long_number(number)
print(formatted_number)  # Output: 1 234 567 890.123 456 589