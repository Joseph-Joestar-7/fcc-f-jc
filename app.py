from flask import Flask, render_template,jsonify

app= Flask(__name__)

JOBS=[
    {
        "id":1,
        "title":'Data Analyst',
        'location':"Bengaluru",
        'salary':'10000'
    },
    {
        "id":2,
        "title":'Game dev',
        'location':"Kolkata",
        'salary':'10000'
    }
]

@app.route("/")
def hello():
    return render_template("home.html",
                           jobs=JOBS,
                           company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)  
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)