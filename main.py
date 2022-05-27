from flask import Flask, render_template, redirect, flash
app = Flask('app')

app.config['SECRET_KEY'] = 'HAglkjlttjglfA'

@app.route('/')
def index():
  return redirect('/hello/joao')

@app.route('/hello/<name>')
def hello(name):
  flash(f'Bem-vindo, {name}!', 'success')
  return render_template('hello.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)