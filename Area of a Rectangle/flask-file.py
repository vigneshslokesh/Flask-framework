# flask_rectangle.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/area', methods=['GET', 'POST'])
def area():
    """
    Endpoint to calculate the area of a rectangle.
    
    For GET requests: Expects 'width' and 'height' as query parameters.
    For POST requests: Expects JSON data with 'width' and 'height'.
    
    :return: JSON response containing the width, height, and area of the rectangle
    """
    try:
        if request.method == 'GET':
            # Get width and height from query parameters; default to 0 if not provided
            width = float(request.args.get('width', '0'))
            height = float(request.args.get('height', '0'))
        
        elif request.method == 'POST':
            # Parse JSON data from the request
            data = request.get_json()
            width = float(data.get('width', '0'))
            height = float(data.get('height', '0'))
        
        # Validate that width and height are positive numbers
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        
        # Calculate the area
        area = width * height
        
        # Return the result as a JSON response
        return jsonify({"width": width, "height": height, "area": area})
    
    except ValueError as e:
        # Return an error message in case of invalid input
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Return a general error message for unexpected issues
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
