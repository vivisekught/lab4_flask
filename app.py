from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    title = 'Car Shop Home'
    featured_cars = [
        {'name': 'Car 1', 'description': 'Description of car 1', 'price': '$10,000', 'image': 'car.jpg'},
        {'name': 'Car 2', 'description': 'Description of car 2', 'price': '$15,000', 'image': 'car.jpg'},
        {'name': 'Car 3', 'description': 'Description of car 3', 'price': '$20,000', 'image': 'car.jpg'},
        {'name': 'Car 4', 'description': 'Description of car 4', 'price': '$10,000', 'image': 'car.jpg'},
        {'name': 'Car 5', 'description': 'Description of car 5', 'price': '$15,000', 'image': 'car.jpg'},
        {'name': 'Car 6', 'description': 'Description of car 6', 'price': '$20,000', 'image': 'car.jpg'},
        {'name': 'Car 7', 'description': 'Description of car 7', 'price': '$10,000', 'image': 'car.jpg'},
        {'name': 'Car 8', 'description': 'Description of car 8', 'price': '$15,000', 'image': 'car.jpg'},
    ]
    year = 2023
    return render_template('home.html', title=title, featured_cars=featured_cars, year=year)


@app.route('/offers')
def offers():
    title = 'Товари та послуги'
    offers = [
        {'name': 'Offer 1', 'description': 'Description 1', 'price': '$10,000', 'image': 'offer.jpg'},
        {'name': 'Offer 2', 'description': 'Description 2', 'price': '$15,000', 'image': 'offer.jpg'},
        {'name': 'Offer 3', 'description': 'Description 3', 'price': '$20,000', 'image': 'offer.jpg'},
        {'name': 'Offer 4', 'description': 'Description 1', 'price': '$10,000', 'image': 'offer.jpg'},
        {'name': 'Offer 5', 'description': 'Description 2', 'price': '$15,000', 'image': 'offer.jpg'},
        {'name': 'Offer 6', 'description': 'Description 3', 'price': '$20,000', 'image': 'offer.jpg'},
        {'name': 'Offer 7', 'description': 'Description 1', 'price': '$10,000', 'image': 'offer.jpg'},
        {'name': 'Offer 8', 'description': 'Description 2', 'price': '$15,000', 'image': 'offer.jpg'},
    ]
    year = 2023
    return render_template('offers.html', title=title, offers=offers, year=year)


@app.route('/contact')
def contact():
    return render_template('contact.html', year=2023)

@app.route('/prices')
def prices():
    cars = [
        {'brand': 'Toyota', 'model': 'Camry', 'price': '$25,000'},
        {'brand': 'Honda', 'model': 'Civic', 'price': '$22,000'},
        {'brand': 'Ford', 'model': 'Mustang', 'price': '$35,000'},
        {'brand': 'Chevrolet', 'model': 'Cruze', 'price': '$20,000'},
        {'brand': 'BMW', 'model': '3 Series', 'price': '$40,000'},
        {'brand': 'Toyota', 'model': 'Camry', 'price': '$25,000'},
        {'brand': 'Honda', 'model': 'Accord', 'price': '$23,500'},
        {'brand': 'Ford', 'model': 'Mustang', 'price': '$35,000'},
        {'brand': 'Chevrolet', 'model': 'Camaro', 'price': '$32,500'},
        {'brand': 'BMW', 'model': 'X5', 'price': '$45,000'},
        {'brand': 'Toyota', 'model': 'Camry', 'price': '$25,000'},
        {'brand': 'Honda', 'model': 'Accord', 'price': '$23,500'},
        {'brand': 'Ford', 'model': 'Mustang', 'price': '$35,000'},
        {'brand': 'Chevrolet', 'model': 'Camaro', 'price': '$32,500'},
        {'brand': 'BMW', 'model': 'X5', 'price': '$45,000'},
    ]
    return render_template('prices.html', title='Car Shop - Prices', cars=cars, year=2023)

@app.route('/contact', methods=['GET', 'POST'])
def contact_company():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Process the form submission (e.g., send an email, store the message in a database, etc.)

        # Return a success message or redirect to a thank you page
        return render_template('contact.html', name=name)
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()
