import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from dotenv import load_dotenv
from services.ai_service import get_ai_response
from services.db_service import save_purchase_transaction

# Load environment variables from the .env file
load_dotenv()

# --- Flask App Initialization ---
app = Flask(__name__, static_folder='static', template_folder='static')

# --- Configuration ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MONGO_CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING")

# Basic validation for credentials
if not GEMINI_API_KEY or not MONGO_CONNECTION_STRING:
    print("Error: Missing one or more environment variables. Please check your .env file.")
    exit(1)

# --- API Endpoints ---

@app.route('/')
def index():
    """Serves the main HTML page to the user."""
    return render_template('index.html')

@app.route('/ask_kuberi', methods=['POST'])
def ask_kuberi():
    """
    API 1: Handles user questions, interacts with the LLM, and provides a
    factual answer along with a digital gold purchase nudge.
    """
    data = request.get_json()
    user_question = data.get('question')

    # Basic server-side validation
    if not user_question:
        return jsonify({"error": "Missing 'question' in request body."}), 400

    try:
        # Call the AI service, which now includes retry logic
        response_text = get_ai_response(user_question, GEMINI_API_KEY)
        return jsonify({"message": "Success", "answer": response_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/purchase_digital_gold', methods=['POST'])
def purchase_digital_gold():
    """
    API 2: Handles the digital gold purchase, logs the transaction to MongoDB,
    and returns a success message.
    """
    data = request.get_json()
    user_id = data.get('user_id')

    # Basic server-side validation
    if not user_id:
        return jsonify({"error": "Missing 'user_id' in request body."}), 400

    try:
        # Call the database service
        transaction_id = save_purchase_transaction(user_id)
        return jsonify({
            "message": "Purchase successful! Your digital gold has been credited to your account.",
            "user_id": user_id,
            "purchase_amount": 10,
            "transaction_id": transaction_id
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Make sure the `services` directory is a Python package
    if not os.path.exists('services/__init__.py'):
        open('services/__init__.py', 'a').close()
    
    app.run(debug=True)
