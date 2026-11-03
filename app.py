from flask import Flask, render_template, request, jsonify
from live_monitor import get_live_metrics
import joblib
import pandas as pd

from troubleshooting import get_recommendation
from pcap_analyzer import analyze_pcap

app = Flask(__name__)

# Load the existing trained model
model = joblib.load("model.pkl")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = pd.DataFrame([{
            "latency": float(request.form["latency"]),
            "packet_loss": float(request.form["packet_loss"]),
            "jitter": float(request.form["jitter"]),
            "bandwidth": float(request.form["bandwidth"]),
            "cpu": float(request.form["cpu"]),
            "memory": float(request.form["memory"]),
            "error_rate": float(request.form["error_rate"])
        }])

        # Random Forest prediction
        prediction = model.predict(features)[0]

        probabilities = model.predict_proba(features)[0]
        confidence = float(max(probabilities) * 100)

        # Troubleshooting recommendation
        recommendation = get_recommendation(str(prediction))

        result = {
            "fault": str(prediction),
            "confidence": round(confidence, 2),
            "recommendation": recommendation
        }

        # Preserve entered values
        metrics = features.iloc[0].to_dict()

        return render_template(
            "index.html",
            result=result,
            metrics=metrics
        )

    except Exception as e:
        app.logger.exception("AI prediction failed")
        return f"AI Prediction Error: {str(e)}", 500


@app.route("/analyze-pcap")
def analyze_pcap_route():
    try:
        # Analyze your existing PCAP capture
        metrics = analyze_pcap("captures/netguard_live.pcapng")

        # These four values are placeholders, not extracted
        # measurements from the PCAP file.
        data = {
            "latency": metrics["latency"],
            "packet_loss": metrics["packet_loss"],
            "jitter": metrics["jitter"],
            "bandwidth": 100,
            "cpu": 30,
            "memory": 40,
            "error_rate": 0
        }

        # Run the existing Random Forest model
        features = pd.DataFrame([data])
        prediction = model.predict(features)[0]

        probabilities = model.predict_proba(features)[0]
        confidence = float(max(probabilities) * 100)

        # Get the troubleshooting recommendation
        recommendation = get_recommendation(prediction)

        result = {
            "fault": str(prediction),
            "confidence": round(confidence, 2),
            "recommendation": recommendation
        }

        # Send the real PCAP metrics and AI result to the dashboard
        return render_template(
            "index.html",
            metrics=metrics,
            result=result
        )

    except Exception as e:
        app.logger.exception("PCAP analysis failed")
        return f"PCAP analysis error: {e}", 500
    


@app.route("/api/live")
def live_network_api():
    try:
        metrics = get_live_metrics(duration=15)

        latency = metrics.get("latency", 0)
        packet_loss = metrics.get("packet_loss")
        successful = metrics.get("successful_replies", 0)

        # Classify faults using actual live measurements
        if metrics.get("status") != "Connected":
            fault = "Monitoring Connection Error"
            recommendation = "Check the connection between Flask and the GNS3 PC1 console."

        elif successful == 0:
            fault = "Link Failure"
            recommendation = "Check network links, interfaces, and device connectivity."

        elif packet_loss is not None and packet_loss > 10:
            fault = "Packet Loss"
            recommendation = "Inspect network cables, interfaces, congestion, and packet drops."

        elif latency > 100:
            fault = "High Latency"
            recommendation = "Investigate network congestion, routing delays, and link performance."

        else:
            fault = "Normal"
            recommendation = "Network is operating normally. Continue monitoring."

        metrics["fault"] = fault
        metrics["recommendation"] = recommendation

        return jsonify(metrics)

    except Exception as e:
        app.logger.exception("Live monitoring failed")
        return jsonify({
            "status": "Connection Error",
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)