import streamlit as st
import pandas as pd
from joblib import load
from sklearn.ensemble import RandomForestClassifier

# Load the trained model
model = load('model.joblib')

# Verify the loaded model is an instance of RandomForestClassifier
if not isinstance(model, RandomForestClassifier):
    st.error("Loaded model is not a RandomForest model.")
    st.stop()

# Setting up the title and form
st.title('Fault Type Prediction App')
with st.form(key='fault_form'):
    st.write("Please input the current and voltage measurements:")

    # User inputs for currents and voltages
    Ia = st.number_input('Current Ia (Amps)')
    Ib = st.number_input('Current Ib (Amps)')
    Ic = st.number_input('Current Ic (Amps)')
    Va = st.number_input('Voltage Va (Volts)')
    Vb = st.number_input('Voltage Vb (Volts)')
    Vc = st.number_input('Voltage Vc (Volts)')

    # Submit button
    submit_button = st.form_submit_button(label='Predict')

# If the user presses the submit button, make a prediction
if submit_button:
    # Create a DataFrame with the input data
    input_data = pd.DataFrame([[Ia, Ib, Ic, Va, Vb, Vc]],
                              columns=['Ia', 'Ib', 'Ic', 'Va', 'Vb', 'Vc'])

    # Predict the fault type using the trained model
    prediction = model.predict(input_data)


    # Output the prediction
    if prediction == 0:
        st.success("The predicted fault type is: No Fault")
    elif prediction == 1:
        st.error("The predicted fault type is: LLG Fault")
    elif prediction == 2:
        st.error("The predicted fault type is: LLLG Fault")

    elif prediction == 3:
        st.error("The predicted fault type is: LG Fault")

    elif prediction == 4:
        st.error("The predicted fault type is: LLL Fault")

    else:
        st.error("The predicted fault type is: LLG Fault")
    

# The above code needs to be saved in a Python script and run using Streamlit.
