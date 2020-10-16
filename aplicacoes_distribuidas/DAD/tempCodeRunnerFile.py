@app.route("/teste")
def teste():
    return "<h1>Teste - Página Flask</h1>"

@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)