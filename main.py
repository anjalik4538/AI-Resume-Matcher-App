from flask import Flask, render_template, request
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from resume_parser import extract_text
from skill import extract_skills

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"


@app.route("/")
def home():
    return render_template("matchresume.html")


@app.route("/matcher", methods=["POST"])
def matcher():

    job_description = request.form["job_description"]

    files = request.files.getlist("resumes")

    resumes = []
    filenames = []

    for file in files:

        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

        file.save(path)

        text = extract_text(path)

        resumes.append(text)

        filenames.append(file.filename)

    documents = [job_description] + resumes

    vectorizer = TfidfVectorizer().fit_transform(documents)

    vectors = vectorizer.toarray()

    job_vector = vectors[0]
    resume_vectors = vectors[1:]

    similarity = cosine_similarity([job_vector], resume_vectors)[0]

    scores = [round(i * 100, 2) for i in similarity]

    results = []

    for i in range(len(scores)):

        skills = extract_skills(resumes[i])

        results.append({
            "name": filenames[i],
            "score": scores[i],
            "skills": skills
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    labels = [r["name"] for r in results]
    chart_scores = [r["score"] for r in results]

    return render_template(
        "result.html",
        results=results,
        labels=labels,
        scores=chart_scores
    )



if __name__ == "__main__":

    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    app.run(debug=True)