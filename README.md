# 🤖 AI Resume Matcher App

## 📌 Overview

AI Resume Matcher App is a web-based application that analyzes and compares multiple resumes with a given job description. It uses Natural Language Processing (NLP) techniques to calculate similarity scores and helps recruiters identify the best candidates efficiently.

---

## 🚀 Features

* 📄 Upload multiple resumes (PDF/DOCX)
* 📝 Enter job description
* 📊 Calculate similarity score using AI (TF-IDF + Cosine Similarity)
* 🧠 Extract key skills from resumes
* 📈 Display ranked results with scores
* 📉 Visual chart representation of results

---

## 🛠️ Tech Stack

**Frontend:**

* HTML
* CSS
* JavaScript

**Backend:**

* Python (Flask)

**Machine Learning / NLP:**

*BERT
*Sentence Transformers
*spaCy
*NLTK
* Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)

**Other Tools:**

* Git & GitHub

---

## ⚙️ How It Works

1. User enters a job description
2. Uploads multiple resumes
3. System extracts text from resumes
4. Converts text into vectors using TF-IDF
5. Calculates similarity using cosine similarity
6. Displays ranked results with scores and extracted skills

---

## 📂 Project Structure

```
AI-Resume-Matcher/
│── app.py
│── resume_parser.py
│── skill.py
│── templates/
│    ├── matchresume.html
│    ├── result.html
│── uploads/
│── static/
│── requirements.txt
```

---

## 🧪 Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/AI-Resume-Matcher-App.git
cd AI-Resume-Matcher-App
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

### 3️⃣ Activate virtual environment

* Windows:

```
venv\Scripts\activate
```


### 4️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 5️⃣ Run the application

```
python app.py
```

### 6️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Example Output

* Resume 1 → 85%
* Resume 2 → 72%
* Resume 3 → 60%

---

## 🔮 Future Improvements

* 🔐 User authentication system
* 💳 Payment integration for premium features
* 📬 Email notifications
* 🤖 Advanced NLP models (BERT, LLMs)
* 🌐 Deploy on cloud (AWS/Render)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙋‍♀️ Author

**Anjali Kumari**

* 💼 Aspiring Full Stack & AI Developer
  

---

## ⭐ Show Your Support

If you like this project, please give it a ⭐ on GitHub!
