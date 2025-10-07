from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
app = Flask(__name__)
CORS(app)

# Nebula API configuration
NEBULA_BASE_URL = "https://nebula.cs.vu.nl/api/"
NEBULA_API_KEY = os.getenv("NEBULA_API_KEY")
NEBULA = OpenAI(base_url=NEBULA_BASE_URL, api_key=NEBULA_API_KEY)
MODEL = "levi-chatbot"

@app.route("/health", methods=["GET"])
def health():
    return {"status": "healthy"}, 200

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    def generate():
        messages = [{"role": "user", "content": user_message}]

        params = {
            "model": MODEL,
            "messages": messages,
            "stream": True,
        }

        stream = NEBULA.chat.completions.create(**params)

        thinking = False

        for chunk in stream:

            if chunk.choices and len(chunk.choices) > 0:
                delta = chunk.choices[0].delta.content

                if delta is not None:
                    if "<think>" in delta:
                        thinking = True
                    if "</think>" in delta:
                        thinking = False
                        continue

                    if not thinking and "<think>" not in delta:
                        yield f"data: {json.dumps({'content': delta})}\n\n"

        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={
            "X-Accel-Buffering": "no"
        }
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)

