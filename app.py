from flask import Flask, render_template, jsonify
app = Flask(__name__)

job_data = [
  {
    "id": 1,
    "title": "Automation Engineer", 
    "location": "Lahore, Pakistan", 
    "salary": "PKR 10,00,000", 
  },  
  
  {
    "id": 2, 
    "title": "Software Engineer", 
    "location": "Karachi, Pakistan", 
    "salary": "PKR 12,00,000",
  },

  {
    "id": 3, 
    "title": "Data Engineer", 
    "location": "Islamabad, Pakistan",  
  },

  {
    "id": 4, 
    "title": "Web Developer", 
    "location": "Lahore, Pakistan", 
    "salary": "PKR 20,00,000", 
  },
]

@app.route('/')
def hello_world():
  return render_template('home.html', job_data=job_data, 
                        company_name='Faiziz')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(job_data)

if __name__ == '__main__':
  app.run(host = '0.0.0.0',  debug = True)
