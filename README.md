
# Web Quality Analyzer

Web Quality Analyzer is a Python-based tool designed to analyze and score the quality of web pages. It evaluates various features of a webpage, including its structure, content, readability, and sentiment, to categorize it as either "High Quality," "Medium Quality," or "Low Quality."

## Features

- **Structural Analysis**: Analyzes the structure of the webpage by counting sections, images, links, and headings.
- **Content Evaluation**: Measures the length of the content, text-to-HTML ratio, and presence of important meta tags like the viewport and description.
- **Readability Analysis**: Uses the `textstat` library to calculate the readability of the webpage's text content.
- **Sentiment Analysis**: Utilizes `TextBlob` to determine the sentiment of the text content on the webpage.
- **Scoring System**: A scoring system is applied to the features, and the webpage is categorized based on its total score.

## Project Structure

```
WebAnalyzer/
├── flask_app.py            # Flask server for the API
├── feature_extractor.py    # Script for feature extraction
├── train_model.py          # Script for training the model
├── predict_quality.py      # Script for predicting web quality
├── scoring.py              # Script for calculating the score based on extracted features
├── nlp_analysis.py         # Script for analyzing readability and sentiment
├── config.py               # Configuration file with centralized URL
├── web_quality_model.pkl   # The trained model file (generated after running train_model.py)
├── web-analyzer-env/       # Virtual environment directory
└── requirements.txt        # List of dependencies
```

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/pedroffeitosa/web-quality-analyzer.git
   cd web-quality-analyzer
   ```

2. **Set Up the Virtual Environment:**

   ```bash
   python3 -m venv web-analyzer-env
   source web-analyzer-env/bin/activate  # On Windows: web-analyzer-env\Scriptsctivate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Additional Dependencies:**

   After installing the dependencies, make sure to install `textblob` corpora:

   ```bash
   python -m textblob.download_corpora
   ```

## Usage

### Training the Model

1. **Train the Machine Learning Model:**

   Run the `train_model.py` script to train the model and generate the `web_quality_model.pkl` file:

   ```bash
   python train_model.py
   ```

### Running the Flask API

1. **Start the Flask Server:**

   Run the `flask_app.py` script to start the Flask server:

   ```bash
   python flask_app.py
   ```

   The server will start running on `http://127.0.0.1:5000/`.

2. **Test the API:**

   You can test the API using a web browser, Postman, or `curl`:

   ```bash
   curl "http://127.0.0.1:5000/predict?url=https://www.example.com"
   ```

   The API will return a JSON response with the quality analysis of the webpage.

## Example API Response

```json
{
  "quality": {
    "Quality Category": "High Quality",
    "Readability": -308.29,
    "Score": 90,
    "Sentiment": -0.042052967242849876
  }
}
```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
