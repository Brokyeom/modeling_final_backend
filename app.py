from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')  # 'name'이라는 쿼리 파라미터를 가져옵니다. 기본값은 'Guest'입니다.
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
