from flask import Flask , render_template,request,redirect,url_for,json,flash

app= Flask(__name__)

##FIRST PAGE
@app.route("/")
def firstPage():
    return redirect(url_for("mainpage"))

#MAIN PAGE
@app.route("/mainpage.html",methods=["GET","POST"])
def mainpage():
    if request.method=="POST":
        if request.form['submit_button']=='reservation':
            return redirect(url_for("reservation"))
    return render_template("/mainpage.html")


#RESERVATION PAGE
@app.route("/reservation.html",methods=["GET","POST"])
def reservation():

    return render_template("reservation.html")

#INDEX PAGE
@app.route("/index.html",methods=["GET","POST"])
def index():

    return render_template("index.html")


#TO RUN OUR PYTHON APP
if __name__ =="__main__":
    app.run(debug=True)