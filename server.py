from flask import Flask, request, jsonify
import GPG

# 创建 Flask 应用
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'

@app.route('/gpg', methods=['post'])
def gpg():
    data = request.json
    start = data['start']
    end = data['end']
    time_budget = data['time_budget']
    path = GPG.execute(start, end, time_budget)
    return jsonify({'path': path})

# 如果直接运行该脚本，则启动 Flask 服务
if __name__ == '__main__':
    # 启动 Flask 应用，监听 8001 端口
    app.run(host='0.0.0.0', port=8001)
