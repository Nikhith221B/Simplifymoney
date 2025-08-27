#
# This service handles all interactions with the Gemini AI model.
# It includes a robust retry mechanism with exponential backoff.
#

import requests
import json
import time

# The Gemini API endpoint
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent"

def get_ai_response(user_question, api_key, max_retries=3, initial_delay=1):
    """
    Gets a response from the Gemini AI model with a retry mechanism.
    
    :param user_question: The question from the user.
    :param api_key: The Gemini API key.
    :param max_retries: Maximum number of retries for the API call.
    :param initial_delay: Initial delay in seconds before the first retry.
    :return: The formatted AI response text.
    """
    prompt = (
        "You are Kuber AI, a friendly financial advisor specializing in gold investments "
        "for the Simplify Money app. Your primary goal is to provide a concise, factual "
        "answer to the user's question about gold and then gently guide them to "
        "invest in digital gold. Be encouraging and helpful.\n\n"
        "Here's an example:\n"
        "User: 'Why is gold a good investment?'\n"
        "Kuber AI: 'Gold is often considered a safe haven asset because its value tends to "
        "rise during times of economic uncertainty and inflation. It can be a great way "
        "to diversify your portfolio.'\n"
        "Nudge: 'For a seamless and secure investment, you can start with digital gold "
        "on the Simplify Money app. Are you ready to start your investment journey?'\n\n"
        f"Now, answer the following question from the user:\n"
        f"User: '{user_question}'"
    )

    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": prompt}]}
        ]
    }
    
    headers = {
        'Content-Type': 'application/json'
    }

    # Implement exponential backoff for retries
    for attempt in range(max_retries):
        try:
            response = requests.post(f"{GEMINI_API_URL}?key={api_key}", headers=headers, data=json.dumps(payload), timeout=10)
            response.raise_for_status()

            gemini_data = response.json()
            answer = gemini_data['candidates'][0]['content']['parts'][0]['text']

            nudge = "For a seamless and secure investment, you can start with digital gold on the Simplify Money app. Are you ready to start your investment journey?"
            return f"{answer.strip()}\n\n{nudge}"
        
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                delay = initial_delay * (2 ** attempt)
                print(f"Request failed: {e}. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise RuntimeError(f"Failed to get response from Gemini API after {max_retries} attempts.") from e
