from flask import Flask, render_template, request
import forecast
import food
import os
app = Flask(__name__)

@app.route("/")
def index():
	terms = request.values.get('terms')  ##Sets the terms object  = the terms value we get from index.html

	if terms:  ##If terms is set run the following
		term, city, state = terms.split(', ')
		address = "{}, {}".format(city, state)
		terms = food.yelp_Search(terms, address)  ##dictionary now set for terms which is used in the 
		# phone = food.format_phone(terms['phone'])
	else:
		terms = None
	return render_template('index.html', terms=terms)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	app.run()

# if __name__ == "__main__":
# 	port = int(os.environ.get("PORT", 5000))
# 	app.run(host="0.0.0.0", port=port)
