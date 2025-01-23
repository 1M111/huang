from flask import Flask, jsonify, send_from_directory, render_template
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')

def get_hot_search():
    # 模拟热搜数据
    mock_data = [
        {"title": "今日新闻热点1"},
        {"title": "今日新闻热点2"},
        {"title": "今日新闻热点3"},
        {"title": "今日新闻热点4"},
        {"title": "今日新闻热点5"},
        {"title": "今日新闻热点6"},
        {"title": "今日新闻热点7"},
        {"title": "今日新闻热点8"},
        {"title": "今日新闻热点9"},
        {"title": "今日新闻热点10"}
    ]
    return mock_data

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/hot-search')
def hot_search():
    hot_items = get_hot_search()
    return jsonify(hot_items)

if __name__ == '__main__':
    # 使用环境变量获取端口，如果没有则默认使用5000
    port = int(os.environ.get('PORT', 5000))
    # 监听所有网络接口
    app.run(host='0.0.0.0', port=port)
