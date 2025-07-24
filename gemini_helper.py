import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
# ---------- Gemini API Setup ----------
def init_gemini(api_key):
    genai.configure(api_key=api_key)

# Initialize Gemini when module is imported
init_gemini(os.getenv("GEMINI_API_KEY"))

# ---------- Retention Suggestion Function ----------
def get_retention_suggestion(user_data):
    try:
        prompt = f"""
        You are a customer success strategist at a telecom company.
        A customer with the following profile is at risk of churning.

        Customer Profile:
        {user_data}

        Suggest 2-3 concrete strategies the company can use to retain this customer.
        Be specific and realistic based on their attributes.
        """


        model = genai.GenerativeModel(model_name="gemini-2.5-pro")
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        print("Gemini error:", e)
        return None
