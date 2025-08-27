# Simplify Money AI Workflow

## Project Overview
This project is a back-end emulation of the **Kuberi AI gold investment workflow**.
The solution consists of two core APIs that integrate a large language model (LLM) with a live database to provide a seamless user experience, from financial advice to a recorded transaction.

---

## Core Components & Technical Approach
The application is built using a modern, scalable, and modular approach with the following technologies:

- **API Framework**: Flask, a lightweight Python web framework, chosen for its simplicity and flexibility in building microservices and APIs.
- **AI Integration**: The Gemini API is used to power the "Kuberi AI" chatbot. The application uses a finely-tuned prompt to ensure the AI provides relevant information on gold investments and nudges the user towards a digital gold purchase.
- **Database**: MongoDB is used as a live, cloud-hosted database to store and verify all user transactions. This provides real-time data persistence, a crucial requirement for a financial application.
- **Project Structure**: Code is organized into a modular structure with separate files for the main application, AI service, and database service. This separation of concerns enhances readability, maintainability, and is a key indicator of professional software development.
- **Dependency Management**: All project dependencies are managed via a `requirements.txt` file. Sensitive information is managed securely using a `.env` file, which is ignored by Git to protect credentials.

---

## Solution Workflow
The **user journey** is designed to replicate the Kuberi AI experience:

1. **User Interaction**  
   A user visits the application's web interface and asks a question related to gold investments.

2. **LLM Processing (API 1)**  
   The user's question is sent to the `/ask_kuberi` API endpoint. This endpoint calls the Gemini API to get a factual, context-aware answer.

3. **AI Nudge**  
   The AI's response includes a call-to-action that encourages the user to purchase digital gold through the Simplify Money app.

4. **Transaction API (API 2)**  
   If the user accepts the nudge, a request is sent to the `/purchase_digital_gold` API endpoint. This API records a transaction in the MongoDB database.

5. **Confirmation & Verification**  
   The API returns a success message to the user, and the new transaction can be verified in real-time in the MongoDB Atlas console.

---

## Deployment & Execution

The application is designed for easy **local execution** and deployment to a cloud platform like Render.

### Prerequisites
- Python 3.8+ installed
- A MongoDB Atlas account with a live cluster
- A Gemini API key

### Setup and Execution
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Nikhith221B/Simplifymoney.git
   cd your-repo-name

2. **Install Dependencies**
   ```bash
   pip install Flask requests python-dotenv pymongo

3. **Configure Environment Variables**
   
     Create a .env file in the project root with the following:

     GEMINI_API_KEY="your-api-key-here"

     MONGO_CONNECTION_STRING="your-mongodb-connection-string-here"

4. **Run the Application**

    python app.py
