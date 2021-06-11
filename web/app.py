from flask import Flask, render_template, Response

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', nickname=name)


@app.route('/list.txt')
def mylist():
    my_file = 'out_list.txt'
    o = ''
    with open(my_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            o += line + '\n'
    return Response(o, status=200, mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
