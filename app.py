import gradio as gr
from transformers import pipeline
import pandas as pd

def analyze(text):
    classifier = pipeline("text-classification", model="ayoubkirouane/BERT-Emotions-Classifier", return_all_scores=True)
    results = classifier(text)
    
    # Extract and format the emotion labels and scores
    formatted_results = [{"Emotion": item['label'], "Score": item['score']} for item in results[0]]
    
    return pd.DataFrame(formatted_results)


examples = ["Walking alone in the dark forest, he couldn't shake the feeling of fear creeping over him." ,
            "Winning the championship brought tears of joy to the entire team."]

# Create a Gradio interface
iface = gr.Interface(fn=analyze, 
                     inputs="text", 
                     outputs=gr.outputs.Dataframe(type="pandas"),
                     allow_flagging=False ,
                     examples=examples , 
                     title="BERT Emotion Analysis App" , 
                     description="Enter a piece of text, and this app will analyze its emotional content using a BERT-Emotions-Classifier model.",
                     )
# Launch the app
iface.launch(debug=True)