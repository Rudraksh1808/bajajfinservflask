from flask import Flask, request, jsonify

app = Flask(__name__)

# Helper function to process the data
def process_data(data):
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    lowercase_alphabets = [item for item in alphabets if item.islower()]
    highest_lowercase_alphabet = sorted(lowercase_alphabets)[-1:] if lowercase_alphabets else []
    
    return numbers, alphabets, highest_lowercase_alphabet

# POST method
@app.route('/bfhl', methods=['POST'])
def post_bfhl():
    try:
        data = request.json.get('data')
        if not data or not isinstance(data, list):
            return jsonify({"is_success": False, "message": "Invalid input"}), 400

        numbers, alphabets, highest_lowercase_alphabet = process_data(data)
        
        response = {
            "is_success": True,
            "user_id": "rudraksh18",  
            "email": "rudraksh.mathuria2021@vitstudent.ac.in",         
            "roll_number": "21BBS0126",        
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

# GET method
@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
