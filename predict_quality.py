import pickle
import requests
from feature_extractor import extract_features
from scoring import calculate_score, categorize_score
from nlp_analysis import analyze_text
from config import URL

def load_model():
    with open('web_quality_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def predict_quality(url):
    model = load_model()
    features = extract_features(url)
    quality_score = calculate_score(features)
    quality_category = categorize_score(quality_score)

    # Optionally, integrate NLP analysis
    response = requests.get(url)
    readability, sentiment = analyze_text(response.text)

    # Return combined results
    return {
        "Quality Category": quality_category,
        "Score": quality_score,
        "Readability": readability,
        "Sentiment": sentiment,
    }

if __name__ == "__main__":
    quality = predict_quality(URL)
    print(f"Predicted Quality for {URL}: {quality}")
