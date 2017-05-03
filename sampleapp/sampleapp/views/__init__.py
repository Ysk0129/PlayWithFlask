from sampleapp import app
from sampleapp.models.count import Counter 
from flask import render_template

@app.route('/')
def index():
    counter = Counter()
    counter.incrCount()
    count = counter.getCount()
    return render_template('index.html', message=count)
