from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("imc.html")

@app.route("/imcresults", methods = ["GET"])
def imcresults():
    peso = float(request.args.get("peso"))
    altezza = float(request.args.get("altezza"))
    imc = peso/(altezza**2)
    if imc >= 18.50 and imc <= 24.99:
        return render_template("imcresults.html", stato = "normopeso", immagine = "/static/images/dietabilanciata.jpeg")
    elif imc <= 18.99:
        return render_template("imcresults.html", stato = "sottopeso", immagine = "/static/images/dietaingrassante.jpeg")
    else:
        return render_template("imcresults.html", stato = "sovrapeso", immagine = "/static/images/dietasovrapeso.jpg")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)