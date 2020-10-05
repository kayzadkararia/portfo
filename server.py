from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):                                              #Refer: video 'buiilding a portfolio 6' of andreii
	with open ("database.text", mode ="a") as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):                                              #Refer: video 'buiilding a portfolio 7' of andreii
	with open ("database.csv", newline = '', mode ="a") as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=",", quotechar=" ",quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
    	    data = request.form.to_dict()
    	    write_to_csv(data)
    	    return redirect('/thankyou.html')
    	except:
    		return 'something went wrong...not saved to the database'
    else:
    	'Something went Wrong. Try Again'

    #render_template('login.html', error=error)




    