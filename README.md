# 搜索页面项目

这是一个模仿百度首页的搜索页面项目，包含搜索功能和热搜榜展示。

## 部署步骤

1. 准备工作
   - 购买一个云服务器（推荐使用Ubuntu或CentOS系统）
   - 购买一个域名（可选）

2. 服务器环境配置
   ```bash
   # 更新系统包
   sudo apt update && sudo apt upgrade -y  # Ubuntu系统
   # 或
   sudo yum update -y  # CentOS系统

   # 安装Python3和pip
   sudo apt install python3 python3-pip  # Ubuntu系统
   # 或
   sudo yum install python3 python3-pip  # CentOS系统

   # 安装git
   sudo apt install git  # Ubuntu系统
   # 或
   sudo yum install git  # CentOS系统
   ```

3. 部署应用
   ```bash
   # 克隆项目
   git clone [你的项目地址]
   cd hotSearch

   # 安装依赖
   pip3 install -r requirements.txt

   # 启动应用
   chmod +x start.sh
   ./start.sh
   ```

4. 配置Nginx（可选，但推荐）
   ```bash
   # 安装Nginx
   sudo apt install nginx  # Ubuntu系统
   # 或
   sudo yum install nginx  # CentOS系统

   # 配置Nginx
   sudo nano /etc/nginx/sites-available/hotsearch
   ```

   添加以下配置：
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;  # 替换为你的域名

       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

   ```bash
   # 创建符号链接
   sudo ln -s /etc/nginx/sites-available/hotsearch /etc/nginx/sites-enabled/

   # 测试配置
   sudo nginx -t

   # 重启Nginx
   sudo systemctl restart nginx
   ```

5. 配置SSL（可选，但推荐）
   ```bash
   # 安装certbot
   sudo apt install certbot python3-certbot-nginx  # Ubuntu系统
   # 或
   sudo yum install certbot python3-certbot-nginx  # CentOS系统

   # 获取SSL证书
   sudo certbot --nginx -d your-domain.com
   ```

## 维护说明

- 日志文件位于 `/var/log/nginx/` 目录下
- 可以使用 `systemd` 设置应用开机自启动
- 建议定期备份数据和更新系统

## 注意事项

- 确保服务器防火墙开放了80（HTTP）和443（HTTPS）端口
- 定期更新系统和依赖包以修复安全漏洞
- 建议使用supervisor或PM2等工具管理进程
- 建议配置监控和告警系统
