from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///prodinfo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ProdInfo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    prodname = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method=='POST':
        prodname = request.form['prodname']
        brand = request.form['brand']
        quantity = request.form['quantity']
        prod = ProdInfo(prodname=prodname, brand=brand, quantity=quantity)
        db.session.add(prod)
        db.session.commit()
        return redirect(url_for('home'))

    allProd = ProdInfo.query.all()
    return render_template('index.html', allProd=allProd)


if __name__ == '__main__':
    app.run(debug=True)