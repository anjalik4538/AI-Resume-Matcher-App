skills_list = [
"python","java","javascript",
"react","reactjs","nodejs","html","css",
"numpy","pandas","matplotlib","seaborn",
"tensorflow","pytorch","streamlit",
"sql","mysql","sqlite",
"data analysis","data cleaning","data preprocessing",
"git","github","pycharm","vscode","jupyter"
]


def extract_skills(text):

    text = text.lower()

    found = []

    for skill in skills_list:

        if skill in text:
            found.append(skill)

    return found