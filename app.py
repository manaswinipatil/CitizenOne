from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/citizen")
def citizen_dashboard():
    return render_template("citizen_dashboard.html")

@app.route("/submit")
def submit_issue():
    return render_template("submit_issue.html")

@app.route("/submitted")
def submitted_issues():
    return render_template("submitted_issue.html")

@app.route("/issue")
def issue_details():
    return render_template("issue_details.html")

@app.route("/admin")
def admin_login():
    return render_template("admin_login.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)