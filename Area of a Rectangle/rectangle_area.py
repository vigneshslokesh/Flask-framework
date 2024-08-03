# rectangle_area.py

def calculate_area(width, height):
    """
    Calculate the area of a rectangle given its width and height.
    
    :param width: The width of the rectangle
    :param height: The height of the rectangle
    :return: The area of the rectangle
    """
    return width * height

if __name__ == '__main__':
    # Default dimensions for demonstration
    width = 5
    height = 10
    
    # Calculate the area using the provided dimensions
    area = calculate_area(width, height)
    
    # Print the result
    print(f"The area of the rectangle with width {width} and height {height} is {area}.")
