# 使用介绍

## 0. 目录结构

├── PyTest_Serverless
│   ├── ReadMe.md
│   ├── Test
│   │   ├── __pycache__
│   │   │   └── test_print.cpython-39-pytest-6.2.5.pyc
│   │   └── test_print.py
│   ├── docker-compose.yml
│   ├── dockerConnect
│   │   ├── Dockerfile
│   │   ├── ReadMe.md
│   │   └── app.py
│   ├── pytest.ini
│   └── requirements.txt

- `serverless`本质为'一套代码，多次使用，无需部署'.
- `app.py`为部署到`server`的后端代码.
- `test_print.py`为模拟`post`的前端请求代码.

## 1.安装
- `pip install -r requirements.txt`
- 阅读`dockerConnect`，下载`docker`
- `docker-compose up --force-recreate`利用`docker-compose`启动`aws lambda`感受`serverless`

## 2. 配置-[pytest.ini]
- addopts:附加

## 3. 测试运行结果
- `pytest`
