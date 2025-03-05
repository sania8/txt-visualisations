import google.generativeai as genai
import os
import re
import sympy as sp
import plotly.graph_objects as go
from dotenv import load_dotenv

# Load environment variables (for local testing)
load_dotenv()

# Configure API Key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ GEMINI_API_KEY not found! Please set it in .env or environment variables.")
    exit()

genai.configure(api_key=api_key)

# -----------------------------
# 1️⃣ Extract Equation from Word Problem using Gemini
# -----------------------------
def extract_equation_from_word_problem(text):
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    You are a math assistant. Extract the clean mathematical equation from this word problem. 
    Respond only with the equation (no explanation, no text other than the equation).

    Example: 
    Input: A car rental company charges a base fee of ₹500 plus ₹20 per kilometer driven.
    Output: y = 20x + 500

    Here is the word problem: 
    {text}
    """

    response = model.generate_content(prompt)
    equation = response.text.strip()

    if "y =" not in equation and "=" not in equation:
        raise ValueError("No valid equation could be extracted from this text.")
    
    return equation

# -----------------------------
# 2️⃣ Clean the Equation (add missing multiplication signs)
# -----------------------------
def add_multiplication_signs(equation):
    equation = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation)  # 2x → 2*x
    equation = equation.replace("^", "**")  # Convert powers to Python format
    return equation

# -----------------------------
# 3️⃣ Parse into sympy Expression
# -----------------------------
def parse_equation(equation):
    equation = add_multiplication_signs(equation)
    lhs, rhs = equation.split('=')
    expr = sp.sympify(rhs.strip())
    return expr

# -----------------------------
# 4️⃣ Plot Equation using Plotly
# -----------------------------
def plot_equation(expr):
    x = sp.symbols('x')
    x_vals = [i / 10 for i in range(-100, 101)]
    y_vals = [float(expr.subs(x, val)) for val in x_vals]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='Graph'))
    fig.update_layout(title="Graph of Extracted Equation", xaxis_title="x", yaxis_title="y")
    fig.show()

# -----------------------------
# 🔥 Full Execution Flow
# -----------------------------
if __name__ == "__main__":
    text = "A car rental company charges a base fee of ₹500 plus ₹20 per kilometer driven. Write and plot the cost equation."

    try:
        # Step 1: Extract equation from the word problem
        equation = extract_equation_from_word_problem(text)
        print(f"✅ Extracted Equation: {equation}")

        # Step 2: Parse into sympy expression
        expression = parse_equation(equation)

        # Step 3: Plot the equation
        plot_equation(expression)

    except Exception as e:
        print(f"❌ Error: {e}")
