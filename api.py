from flask import Flask, request, jsonify, render_template
import joblib

# Load trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")  # Fix: Load the vectorizer

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_url():
    data = request.get_json()
    url = data.get("url", "")

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # Transform URL using vectorizer
    url_vectorized = vectorizer.transform([url])  # Fix: Use the loaded vectorizer

    # Predict using the trained model
    prediction = model.predict(url_vectorized)[0]

    # Convert prediction to label
    result = "Phishing" if prediction == 1 else "Legitimate"

    return jsonify({"result": result})

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
