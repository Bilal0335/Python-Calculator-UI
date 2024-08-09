import streamlit as st

def main():
    # Basic HTML and CSS styling
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f2f6;
            font-family: Arial, sans-serif;
        }
        .emoji {
            text-align: center;
            font-size: 48px;
            margin-bottom: 10px;
        }
        .main-title {
            color: #2c3e50;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .sub-title {
            color: #3498db;
            text-align: center;
            font-size: 20px;
            margin-bottom: 40px;
        }
        .quote {
            color: #555555;
            font-style: italic;
            text-align: center;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #3498db;
            color: white;
            border-radius: 5px;
            font-size: 16px;
            padding: 8px 16px;
        }
        .stButton>button:hover {
            background-color: #2980b9;
        }
        .result {
            font-size: 24px;
            color: #2c3e50;
            font-weight: bold;
            margin-top: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Emoji
    st.markdown("<div class='emoji'>📊</div>", unsafe_allow_html=True)  # Professional chart emoji

    # Title and Subtitle
    st.markdown("<div class='main-title'>Simple Calculator</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Created by Engr. Bilal Hussain</div>", unsafe_allow_html=True)


    st.write("This is a simple calculator built with Streamlit.")

    # Input fields for numbers
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    # Dropdown for selecting operation
    operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

    # Button to calculate the result
    if st.button("Calculate"):
        # Perform calculation based on selected operation
        result = None
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero")
                result = None  # Ensure result is None if there's an error

        # Display result if valid
        if result is not None:
            st.markdown(f"<div class='result'>The result is: {result}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
