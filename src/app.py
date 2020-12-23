__author__ = "Cobbin"
from flask import Flask, render_template, request, url_for, flash, send_from_directory, send_file
import os, requests
from werkzeug.utils import redirect


app = Flask(__name__)
app.secret_key =  app.secret_key = "1234" # os.environ.get("SECRETE_KEY")

@app.route('/download/<path:url>/<string:filename>', methods=['GET', 'POST'])
def download(url=None, filename=None):
    return send_from_directory(directory=url, filename=filename, as_attachment=True)

def get_pdfs():
    path = 'src/static/pdfs'
    years = os.listdir(path)
    all_pdfs = []
    for year in years:
        new_path = path + '/' + year 
        sems_path = os.listdir(new_path) 
        for sem_path in sems_path:
            pdfs_path = os.listdir(new_path + '/' + sem_path)
            all_pdfs.append(pdfs_path)

    return all_pdfs

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pdfs')
def pdfs():
    all_pdfs = get_pdfs()
    first_year_first_sem = all_pdfs[0]
    first_year_second_sem = all_pdfs[1]
    second_year_first_sem = all_pdfs[2]
    second_year_second_sem = all_pdfs[3]
    third_year_first_sem = all_pdfs[4]
    third_year_second_sem = all_pdfs[5]
    fourth_year_first_sem = all_pdfs[6]
    fourth_year_second_sem = all_pdfs[7]
    return render_template('home.html', 
        _1001 = first_year_first_sem,
        _1002 = first_year_second_sem,
        _2001 = second_year_first_sem,
        _2002 = second_year_second_sem,
        _3001 = third_year_first_sem,
        _3002 = third_year_second_sem,
        _4001 = fourth_year_first_sem,
        _4002 = fourth_year_second_sem
    ) 

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        with open("messages.txt", 'r') as messages:
            content = messages.readlines()
            return render_template('messages.html', messages=content)

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    with open("messages.txt", 'a') as messages:
        messages.write(f" {name}    {email}      {message} \n")
        flash('Message Sent (:')
        return redirect(url_for('home'))
