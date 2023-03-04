from flask import Flask, render_template, jsonify

main = Flask(__name__)

JOBS = [
{
  'id':1,
  'position':'Analyst',
  'salary':'Rs 10000000',
  'location':'delhi'
},
{
  'id':2,
  'position':'Developer',
  'salary':'Rs 2000000',
  'location':'goa'
},
{
  'id':3,
  'position':'PS',
  'location':'mumbai'
},
{
  'id':4,
  'position':'Accountant',
  'salary':'Rs 56090000',
  'location':'punjab'
}
  
]

@main.route("/")
def hello_world():
  return render_template('home.html', jobs = JOBS , company_name='Grow')

@main.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
 main.run(host='0.0.0.0', debug = True)
  