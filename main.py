from flask import Flask, render_template, flash, redirect, url_for, request  
# Initialize the Flask application
app = Flask(__name__)

app.secret_key = 'your_super_secret_unpredictable_key'


# Define the route for the homepage
@app.route("/")
def home():
    return render_template('home.html', title="Home Page")

@app.route("/login/") 
def login():
    return render_template("login.html", title="login page")

@app.route("/signup/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Process the signup form data
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password != confirm_password:
            flash("Passwords do not match. Please try again.")
            # Handle the case where passwords do not match
            return render_template("signup.html", title="signup page", error="Passwords do not match")
        

        
        flash("Signup successful! You can now log in.")
        return redirect(url_for("login"))
    return render_template("signup.html", title="signup page")


if __name__ == "__main__":
    app.run(debug=True)
