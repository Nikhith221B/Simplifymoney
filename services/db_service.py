#
# This service handles all database-related operations,
# abstracting them away from the main application logic.
#

import os
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
MONGO_CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING")

# --- MongoDB Initialization ---
try:
    client = MongoClient(MONGO_CONNECTION_STRING)
    db = client.simplify_money
    transactions_collection = db.transactions
    print("MongoDB connected successfully via db_service.py!")
except Exception as e:
    raise RuntimeError(f"Failed to connect to MongoDB: {e}")

# --- Database Operations ---

def save_purchase_transaction(user_id, amount=10):
    """
    Saves a digital gold purchase transaction to the MongoDB database.
    
    :param user_id: The unique ID of the user.
    :param amount: The amount of the gold purchase (hardcoded for this assignment).
    :return: The ID of the newly created transaction document.
    """
    transaction_data = {
        'user_id': user_id,
        'purchase_amount': amount,
        'timestamp': datetime.utcnow()
    }
    
    result = transactions_collection.insert_one(transaction_data)
    return str(result.inserted_id)

