from flask import Flask,request,render_template
import requests
app = Flask(__name__,static_folder='static')



@app.route('/')
def home():
    if request.method=='post':
        return render_template('shop.html')
    return render_template('index2.html')

@app.route('/shop',methods=['POST','GET'])
def shop():
    if request.method=='POST':
        city = request.form['city']
        api = "https://api.openweathermap.org/data/2.5/weather?q=+"+city+"&appid=99e738e563f95294065a3ad292a42cc4"
        response = requests.get(api)
        data = response.json()
        if len(data)<5:
            mes = "please enter valid city name"
            return render_template('shop.html',message=mes)
        else:
            d = int(data['main']['temp'])
            res = int(d-273.15)
            country=data['sys']['country']
            print(data)
            return render_template('shop.html',temp=res,country=country,city=city)
    return render_template('shop.html')
@app.route('/index')
def index2():
    return render_template('index2.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/cart')
def cart():
    return render_template('cart.html')
@app.route('/contact')
def contact():
    return render_template('contact-us.html')




if __name__=="__main__":
    app.run(debug=True)