Here’s a **catchy and well-formatted README.md** for your project, designed to stand out on GitHub or any repository platform. It has **emojis/icons**, clear sections, and highlights your project’s unique features.  

---

# 📊 Intelligent Math Visualizer

> ✨ A smart AI-powered math assistant that reads word problems, extracts equations using **Gemini 1.5 Flash**, and generates beautiful **interactive plots** using **Plotly**.

---

## 🚀 What is SolWise?

SolWise is your **AI Math Buddy**!  
Simply provide a word problem like:

> *"A car rental company charges a base fee of ₹500 plus ₹20 per kilometer driven. Write and plot the cost equation."*

✅ SolWise will:
1. Extract the **correct equation** using **Gemini 1.5 Flash**.
2. Automatically **convert it into a plot-friendly format**.
3. **Generate a stunning interactive plot** using **Plotly**.
4. Display the graph directly in your notebook or web app!

---

## 🔗 How It Works

| Step | Action |
|---|---|
| 🧠 Step 1 | Extract equation using Google Gemini 1.5 Flash |
| ✨ Step 2 | Preprocess equation for sympy (adds missing operators) |
| 📊 Step 3 | Parse equation into **sympy expression** |
| 📉 Step 4 | Generate a beautiful interactive plot using Plotly |

---

## 🛠️ Tech Stack

| Tech 💻 | Purpose 🎯 |
|---|---|
| Python 🐍 | Core Language |
| Gemini 1.5 Flash 🌐 | AI Model for Equation Extraction |
| SymPy ➕➖✖️➗ | Mathematical Parsing |
| Plotly 📈 | Interactive Plot Generation |
| dotenv 📦 | Load API Key Securely |

---

## 📦 Folder Structure

```plaintext
/
|-- app.py                # Main Flask app (if embedding into UI)
|-- plotter.py             # This standalone script (current file)
|-- .env                    # Your API key (GEMINI_API_KEY=...)
|-- README.md               # This file!
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/solwise-math-visualizer.git
cd solwise-math-visualizer
```

### 2️⃣ Create `.env` File
Create a file called `.env` in the root folder and add your Gemini API key:
```
GEMINI_API_KEY=your-google-api-key-here
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Script
```bash
python plotter.py
```

---

## 🎥 Demo Example
**Input Word Problem:**
> A car rental company charges a base fee of ₹500 plus ₹20 per kilometer driven.

**Extracted Equation:**  
✅ `y = 20x + 500`

**Generated Plot:**  
📊 (The Plot will open automatically using Plotly!)

---

## 🛠️ Requirements.txt (for easy install)

```text
google-generativeai
python-dotenv
plotly
sympy
```

---

## 🏅 Why SolWise?

✅ No manual equation typing  
✅ Gemini-powered math understanding  
✅ Instant interactive graphs  
✅ Easy to extend into a web app (just embed this into Flask!)

---

## 📧 Contact

For any queries or contributions, feel free to reach out:

🔗 [LinkedIn](https://www.linkedin.com/in/sania-verma-146514231/)  
📬 Email: saniav2711@gmail.com
