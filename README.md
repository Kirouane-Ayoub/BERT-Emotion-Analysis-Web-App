# BERT Emotion-Analysis Web-App

## Project Overview

+ **Project Name**: Emotion Analysis Web App
+ **Description**: A web application that performs emotion analysis on text inputs using a fine-tuned **BERT-based** model.
+ **Model Used**: *BERT-Emotions-Classifier* [**https://huggingface.co/ayoubkirouane/BERT-Emotions-Classifier**]
+ **Model Task**: Multi-label Emotion classification

## Project Details

### Objective

The Emotion Analysis Web App is designed to help users analyze the emotional content of text inputs. It utilizes the **BERT-Emotions-Classifier** model to classify text into multiple emotion categories, including anger, anticipation, disgust, fear, joy, love, optimism, pessimism, sadness, surprise, and trust.

## Features

+ Supports **multi-label classification**, allowing the identification of multiple emotions in a single text.
+ Provides a user-friendly web interface for easy interaction.

### Input Format

The model expects text input in the form of a string.

### Output Format

+ The model provides a data frame of labels and associated scores, indicating the predicted emotions and their confidence scores.

## Limitations

+ **Limited Emotion Categories**: The BERT-Emotions-Classifier model is trained on a specific set of emotion categories. It may not accurately classify emotions that do not fall within these predefined categories.

+ **Model Performance**: The accuracy of emotion classification depends on the quality and diversity of the training data. The model's performance may vary for text inputs with uncommon or complex emotional expressions.

+ **Bias and Fairness**: Like any machine learning model, the BERT-Emotions-Classifier may exhibit bias in its predictions. Care should be taken to address and mitigate bias in real-world applications to ensure fairness and inclusivity.

+ **Input Length**: The model has limitations on the maximum input text length it can process effectively. Very long texts may be truncated or may not receive accurate classifications.

## Ethical Considerations

When using this app or model, it's essential to consider the ethical implications of emotion analysis. Ensure that the use of emotional data respects privacy and consent, and avoid making decisions that could have adverse effects based solely on emotion analysis.

## Usage

```
pip install -r requirements.txt
python app.py
```
**Check the demo from here**: **https://huggingface.co/spaces/ayoubkirouane/BERT-Emotions-Classifier**

![Screenshot at 2023-09-23 22-22-35](https://github.com/Kirouane-Ayoub/BERT-Emotion-Analysis-Web-App/assets/99510125/40df807b-c75d-4dd3-8e1b-c7cbe02e3315)
