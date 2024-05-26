from flask import Flask, request, render_template 

app = Flask(__name__)
global_msg = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global global_msg
    if request.method == "POST":
       # getting input with name = fname in HTML form
       msg = request.form.get("message")
       global_msg = msg
    #    return f"Your msg is {msg}."
    return render_template("./form.html")


@app.route('/msg', methods=['GET'])
def get_global_msg():
    global global_msg
    # Return header
    return {"global_msg": global_msg}

# Set the global message to None
@app.route('/reset', methods=['POST'])
def reset_global_msg():
    global global_msg
    global_msg = None
    return {"state": global_msg}

if __name__ == '__main__':
    app.run(debug=True)
    
# Run the server.py script and open the browser to http://