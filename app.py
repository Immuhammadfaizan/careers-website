from flask import Flask, render_template, jsonify
from database import load_the_jobs

app = Flask(__name__)

@app.route('/')
def hello_world():
  jobs = load_the_jobs()
  return render_template('home.html', job_data=jobs, 
                        company_name='Faiziz')

@app.route('/api/jobs')
def list_jobs():
  jobs = load_the_jobs()
  return jsonify(jobs)

if __name__ == '__main__':
  app.run(host = '0.0.0.0',  debug = True)
