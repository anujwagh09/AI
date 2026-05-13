from flask import Flask, request, jsonify
import time
from google import genai

# ✅ Initialize API client
client = genai.Client()

app = Flask(__name__)

# ✅ Chat API (No DB, No UI)
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message") if data else None

    if not user_input:
        return jsonify({"reply": "❌ No message received"}), 400

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"You are a help desk assistant. Give short helpful answers.\nUser: {user_input}"
            )

            reply = response.text if response.text else "⚠️ No response from AI."

            return jsonify({"reply": reply})

        except Exception as e:
            print(f"Attempt {attempt+1} failed:", e)
            time.sleep(2)

    return jsonify({
        "reply": "⚠️ Server is busy. Please try again later."
    }), 200


# ▶️ Run app
if __name__ == "__main__":
    app.run(debug=True)

     # $env:GEMINI_API_KEY="AIzaSyBvbJEhP6HBVP3vCExleetOtXrNWRjZ9AM"