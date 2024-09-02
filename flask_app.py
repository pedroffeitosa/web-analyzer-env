from flask import Flask, request, jsonify
from predict_quality import predict_quality

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    url = request.args.get('url')
    if url:
        quality = predict_quality(url)
        return jsonify({'quality': quality})
    else:
        return jsonify({'error': 'URL is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
