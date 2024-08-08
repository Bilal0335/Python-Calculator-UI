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
   * 

   ### 💻 **Code Example**

   Here’s a snippet of the core code used for the calculator:

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


### 📂 **Project Structure**

* **app.py:** Main script for running the Streamlit application.

### 📦 **Installation**

To get started with this project, follow these steps:

1. Clone the repository:
   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copy code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git clone https://github.com/Bilal0335/Python-Calculator-UI.git
   </code></div></div></pre>
2. Navigate to the project directory:
   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copy code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">cd Python-Calculator-UI
   </code></div></div></pre>
3. Install the required packages:
   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>bash</span><div class="flex items-center"><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" class="icon-sm"><path fill="currentColor" fill-rule="evenodd" d="M7 5a3 3 0 0 1 3-3h9a3 3 0 0 1 3 3v9a3 3 0 0 1-3 3h-2v2a3 3 0 0 1-3 3H5a3 3 0 0 1-3-3v-9a3 3 0 0 1 3-3h2zm2 2h5a3 3 0 0 1 3 3v5h2a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1h-9a1 1 0 0 0-1 1zM5 9a1 1 0 0 0-1 1v9a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-9a1 1 0 0 0-1-1z" clip-rule="evenodd"></path></svg>Copy code</button></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
   </code></div></div></pre>

## 📝 **License**

This project is licensed under the MIT License. See the [LICENSE]() file for more details.

## 🤝 **Contributing**

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and contributions are always welcome!

## 🌐 **Links**

* **Live Application:** [Streamlit Calculator](https://calculator-py.streamlit.app/)
* **Source Code:** [GitHub Repository](https://github.com/Bilal0335/Python-Calculator-UI)
