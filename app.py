from flask import Flask, request, jsonify

from os import getenv
import digitalocean

app = Flask(__name__)

DO_TOKEN = getenv("DO_TOKEN", None)
DOMAIN = getenv("DOMAIN", None)
PASSWORD = getenv("PASSWORD", None)

if any(x is None for x in [DO_TOKEN, DOMAIN, PASSWORD]):
    raise Exception(
        "The app has been incorrectly configured. Set DO_TOKEN, DOMAIN, and PASSWORD as environment variables."
    )

if PASSWORD == "":
    raise Exception('PASSWORD can not be set to ""')

domain = digitalocean.Domain(token=DO_TOKEN, name=DOMAIN)


@app.route("/", methods=["POST"])
def create_dns_record():
    data = request.json
    if data is None:
        return jsonify({"error": "no payload sent"}), 400
    if data.get("password", "") != PASSWORD:
        return jsonify({"error": "incorrect password"}), 403

    if all(x in data for x in ["ip", "name"]) is False:
        return jsonify({"error": "missing either name or IP address"}), 400

    try:
        new_record = domain.create_new_domain_record(
            type="A", name=data["name"], data=data["ip"]
        )
        return new_record
    except Exception as e:
        return jsonify({"error": str(e)}), 400
