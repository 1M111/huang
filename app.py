from flask import Flask, jsonify, send_from_directory, render_template
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')

def get_hot_search():
    # 模拟热搜数据
    mock_data = [
        {
            "title": "今日新闻热点1",
            "description": "某科技公司发布重磅新品，引发行业关注"
        },
        {
            "title": "今日新闻热点2",
            "description": "国际体育赛事传来捷报，中国队获得金牌"
        },
        {
            "title": "今日新闻热点3",
            "description": "环保新政策出台，助力绿色发展"
        },
        {
            "title": "今日新闻热点4",
            "description": "教育部发布重要通知，关系千万学子"
        },
        {
            "title": "今日新闻热点5",
            "description": "新能源汽车市场持续升温，销量创新高"
        },
        {
            "title": "今日新闻热点6",
            "description": "医疗健康领域取得重大突破"
        },
        {
            "title": "今日新闻热点7",
            "description": "文化产业发展迎来新机遇"
        },
        {
            "title": "今日新闻热点8",
            "description": "数字经济助力传统产业转型升级"
        },
        {
            "title": "今日新闻热点9",
            "description": "乡村振兴战略实施成效显著"
        },
        {
            "title": "今日新闻热点10",
            "description": "航天技术创新取得重要进展"
        }
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
