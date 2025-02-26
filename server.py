from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Aktifkan CORS untuk semua request

@app.route('/send-location', methods=['POST'])
def receive_location():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Tidak ada data dikirim"}), 400

    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude is None or longitude is None:
        return jsonify({"error": "Data lokasi tidak valid"}), 400

    # Simpan ke file lokasi.txt
    with open("lokasi.txt", "a") as file:
        waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{waktu}, Latitude: {latitude}, Longitude: {longitude}\n")

    return jsonify({"message": "Lokasi berhasil disimpan!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
