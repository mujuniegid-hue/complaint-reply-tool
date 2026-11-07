from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from google import genai
from google.genai import types

load_dotenv()

app = Flask(__name__)
client = genai.Client()

MODEL_NAME = "gemini-3.5-flash"

SYSTEM_PROMPT = """You help small businesses in Kampala reply to customer complaints on WhatsApp.

Write a reply the business owner can send as it is.

Rules:
- Be polite, warm, and professional.
- Start by thanking the customer or saying sorry for the experience, and show you understood their specific issue.
- Do NOT blame the customer, staff, or anyone else.
- Do NOT promise refunds, discounts, replacements, or exact times. Do not invent facts or policies.
- Give one clear next step, such as: we are checking this now and will update you, or please share your order number or photos so we can look into it.
- Keep it short, 3 to 5 sentences, in a natural WhatsApp tone.
- Reply in the same language as the customer's message.
- Never say "we will refund", "we will replace", or give any time like "today" or "within 24 hours"
- Never use placeholders in square brackets. If you don't know a detail, leave it out.
- Do not explain or guess the cause. Do not give excuses.
- Maximum 4 sentences. No subject line, no signature block.
- If the complaint is vague, apologise briefly and ask the customer for details such as what happened and their order number.
- If the customer mentions health, safety, or threatens to go public, stay calm and respectful, take it seriously, and say the owner will look into it personally. Make no promises.
- Output only the reply text. No titles, no explanations, no quotation marks."""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}
    complaint = data.get("complaint", "").strip()

    if not complaint:
        return jsonify({"error": "Please paste a complaint first."}), 400

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=complaint,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.4,
            ),
        )
        reply = (response.text or "").strip()
    except Exception as error:
        print("Gemini error:", error)
        return jsonify({"error": "Sorry, the reply could not be generated. Please try again."}), 500

    if not reply:
        return jsonify({"error": "No reply was produced. Please try again."}), 500

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)