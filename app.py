import streamlit as st
import joblib

#load the trained model
model=joblib.load("sentiment-model.pkl")

#define sentiment labels
sentiment_labels={'1':'positive','0':'negative'}
 
 #create streamlite app
st.title("Sentimental Analysis")

#input text area
user_input=st.text_area("Enter your text here:")

#prediction button

if st.button("Predict"):
    print(user_input)
    predicted_sentiment=model.predict([user_input])[0]
    predicted_sentiment_label=sentiment_labels[str(predicted_sentiment)]
    
    st.info(f"Predicted Sentiment: {predicted_sentiment_label}")

