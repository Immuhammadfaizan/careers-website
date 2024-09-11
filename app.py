from flask import Flask, render_template, jsonify, request
from database import load_the_jobs, show_the_jobs, final_data

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

@app.route('/api/<id>')
def throw_job_page(id):
  jobs = show_the_jobs(id)
  if not jobs:
    return "Not Found", 404 
  return render_template('jobpage.html', 
                         job=jobs)

@app.route('/api/job/<id>')
def throw_json(id):
   jobs = show_the_jobs(id)
   return jsonify(jobs)

@app.route('/job/<id>/apply', methods=['POST'])
def apply_for_the_job(id):
  apply = request.form
  jobs = show_the_jobs(id)
  final_data(id, apply)
  
  return render_template('application_submitted.html', 
                         application=apply, 
                         job=jobs)

if __name__ == '__main__':
  app.run(host = '0.0.0.0',  debug=True)
