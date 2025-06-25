Fake News Detection

This project is a machine learning-based solution to detect whether a given news article is real or fake. Using a Passive Aggressive Classifier and TF-IDF vectorization, the system is trained on a labeled dataset to achieve high accuracy and reliable performance.

Features

- Loads and merges real and fake news datasets  
- Cleans and prepares the text for ML processing  
- Uses TF-IDF to convert text into numeric vectors  
- Trains a Passive Aggressive Classifier  
- Evaluates model with classification report and accuracy metrics

Dataset

Dataset Source: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset  
Files used: `Fake.csv` and `True.csv`  
Labels assigned:  
- 0 = Fake News  
- 1 = Real News  

Built With

Python 3.10+  
Pandas, NumPy  
Scikit-learn  
TfidfVectorizer (for NLP)  
PassiveAggressiveClassifier
Demo link youtube  :https://youtu.be/UgvOAtOPU7I

Model Performance

| Metric     | Score     |
|------------|-----------|
| Accuracy   | 99.45%    |
| Precision  | 99%+      |
| Recall     | 99%+      |
| F1-Score   | 99%+      |

Sample Classification Report:
              precision    recall  f1-score   support  
           0       0.99      1.00      0.99      4733  
           1       0.99      0.99      0.99      4247  

Conclusion:  
The model is highly accurate in distinguishing fake news from real news. It performs well on both classes with minimal overfitting, thanks to the efficiency of Passive Aggressive learning and robust feature extraction.


License

This project is licensed under the MIT License — feel free to use, modify, and share with credit.

About the Creator

Created by Monisa R, a student passionate about using technology and AI to build meaningful tools that solve real-world challenges.

LinkedIn: https://www.linkedin.com/in/monisa-r-17a41228b/  
Email: monisa4606@gmail.com


