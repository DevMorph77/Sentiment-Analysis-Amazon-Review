
# Amazon Product ReviewIQ

## Overview
The **Amazon Product ReviewIQ** project analyzes product reviews across various categories to evaluate sentiment using different classification approaches, including BERT, Naive Bayes, and SVM. The project includes a Streamlit dashboard for visualizing sentiment analysis results and provides performance evaluation of the classification models.

## Project Structure
The project consists of the following main folders:

1. **Analysed-Amazon-Review-Dataset**
   - This folder contains the processed CSV files with sentiment scores for different product categories:
     - `All_Beauty_with_Sentiment_1.csv`: Review data for beauty products, including sentiment analysis.
     - `Gift_Cards_with_sentiment.csv`: Review data for gift cards, including sentiment analysis.
     - `Cell_Phones_with_Sentiment.csv`: Review data for cell phones and accessories, including sentiment analysis.
     - `Appliances_with_Sentiment.csv`: Review data for appliances, including sentiment analysis.
   - Each CSV file includes the following columns:
     - `rating`: Rating given by the user.
     - `title`: Title of the review.
     - `text`: Text of the review.
     - `asin`: Amazon Standard Identification Number.
     - `parent_asin`: ASIN of the parent product (if applicable).
     - `user_id`: Unique identifier for the user.
     - `timestamp`: Time when the review was submitted.
     - `helpful_vote`: Number of users who found the review helpful.
     - `verified_purchase`: Indicates whether the purchase was verified.
     - `positive_sentiment`, `negative_sentiment`, `neutral_sentiment`: Sentiment scores calculated for the reviews.

2. **Performance-Evaluation-Codes**
   - This folder contains scripts used for evaluating the performance of different sentiment classification models:
     - `Bert.py`: Code for evaluating the BERT model's performance on sentiment analysis tasks.
     - `Naive-bayes.py`: Code for evaluating the Naive Bayes model's performance.
     - `Predicting.py`: Code for making predictions using the trained models.
     - `Sentiment.py`: General functions and utilities related to sentiment analysis.
     - `SVM.py`: Code for evaluating the SVM model's performance.
     - `Sentiment-analysis-bert.py`: Implementation details specific to sentiment analysis using the BERT model.

3. **streamlit-dashboard-Amazon-Products**
   - This folder contains the Streamlit application for visualizing sentiment analysis results:
     - `ReviewIQ.py`: The main Streamlit application file that provides the following functionalities:
       - Loads and preprocesses data from the CSV files.
       - Provides a sidebar for category selection and ASIN input.
       - Displays product-level sentiment analysis and top products by sentiment score.
       - Visualizes average sentiment scores by rating and sentiment trends over time.
       - Displays interactive charts comparing sentiment by verified purchase and user sentiment distribution.

4. **TweetEval-dataset**
   - This folder contains datasets used for performance evaluation of the models, specifically tailored for sentiment analysis tasks.
   - The dataset may include tweets labeled with sentiment scores, which can be used to train and evaluate sentiment classification models.

## Getting Started
To run the Streamlit application, follow these steps:

1. Ensure you have Python and the required packages installed. You can create a virtual environment and install the necessary packages using pip:
   ```bash
   pip install streamlit pandas plotly
   ```

2. Navigate to the `streamlit-dashboard-Amazon-Products` folder.

3. Run the Streamlit application:
   ```bash
   streamlit run ReviewIQ.py
   ```

4. Open the provided URL in your web browser to access the dashboard.

## Contributing
Contributions to the project are welcome. Please feel free to open issues or submit pull requests for improvements or new features.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Thank you to the creators of Streamlit, pandas, and Plotly for providing powerful tools for data analysis and visualization.
- Special thanks to the contributors of the datasets used in this project.

---

