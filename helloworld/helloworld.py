from  flask import Flask, render_template


#Initialize app variable

app = Flask(__name__);


@app.route("/")
def home():
    return "This is my home attached to the root url /";

@app.route("/hello")
def hello():
    return "Hello World from Python Flask Web Framework!!"


@app.route("/hello/<string:name>/")
def hello_with_person_name(name):
    # The two lines below will work. But the second is more convenient as it
    # implicitly identifies whether the variable is a string or number, etc
    # return "Hello %s, greetings from Flask Framework!" % name
    return "Hello {}, greetings from Flask Framework!".format(name)

@app.route("/hello2/<string:name>/")
def hello_with_template(name):
    return render_template('hello.html',person_name=name);


@app.route("/hello3/<string:name>/")
def hello_with_layout(name):
    return render_template('hello-extend-layout.html', person_name=name)

if __name__  == "__main__":
    app.run();


