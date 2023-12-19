from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, f1_score
from joblib import load

app = Flask(__name__)

model = load('model.bin')

def map_strength_label(prediction):
    if prediction == 0:
        return 'Low strength'
    elif prediction == 1:
        return 'Moderate strength'
    elif prediction == 2:
        return 'High strength'
    else:
        return 'Unable to detect'

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text_data = data['text']

        prediction = model.predict([text_data])[0]
        
        strength_label = map_strength_label(prediction)

        return jsonify({'You password strength is': strength_label})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
