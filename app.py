import streamlit as st
import pickle
import sklearn
# load model
model = pickle.load(open('model.pkl', 'rb'))

# create title
st.title('Sentiment Analysis Model')

review = st.text_input('Enter your review:')

submit = st.button('Predict')


if submit:
    prediction = model.predict([review])

    if prediction[0] == 'positive':
        st.success('Positive Review')
    else:
        st.warning('Negative Review')
    st.balloons()

