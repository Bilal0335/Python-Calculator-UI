# Simple Calculator with Streamlit

Welcome to the **Simple Calculator** project, built with  **Streamlit** ! This application allows users to perform basic arithmetic operations through a clean and intuitive web interface.

### 📜 **Overview**

This calculator application supports the following operations:

* **Addition**
* **Subtraction**
* **Multiplication**
* **Division**

### 🔧 **Features**

* **User-Friendly Interface:** Input numbers and select the operation through dropdown menus.
* **Error Handling:** Displays an error message if division by zero is attempted.
* **Dynamic Result Display:** Shows the result only when valid inputs are provided.

### 🚀 **How to Use**

1. **Run the Application:**

   * Make sure you have Streamlit installed. If not, install it using `pip install streamlit`.
   * Run the app with the command: `streamlit run app.py`.
2. **Interact with the Calculator:**

   * Enter the numbers in the provided fields.
   * Select the desired operation from the dropdown menu.
   * The result will be displayed below the input fields.

   ### 💻 **Code Example**

   Here’s a snippet of the core code used for the calculator:

```

import streamlit as st

def main():
    st.title("Simple Calculator")

    st.write("This is a simple calculator built with Streamlit.")

    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

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
            result = None

    if result is not None:
        st.write(f"The result is: {result}")

if __name__ == "__main__":
    main()
```

### 📂 **Project Structure**

* **app.py:** Main script for running the Streamlit application.

### 📦 **Installation**

To get started with this project, follow these steps:

1. Clone the repository:
   ``` git clone https://github.com/Bilal0335/Python-Calculator-UI.git ```
2. Navigate to the project directory:
   ``` cd Python-Calculator-UI ```
3. Install the required packages:
   ``` pip install -r requirements.txt ```

## 📝 **License**

This project is licensed under the MIT License. See the [LICENSE]() file for more details.

## 🤝 **Contributing**

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are always welcome!

## 🌐 **Links**

* **Live Application:** [Streamlit Calculator](https://calculator-py.streamlit.app/)
* **Source Code:** [GitHub Repository](https://github.com/Bilal0335/Python-Calculator-UI)
