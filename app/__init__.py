from flask import Flask

def create_app():
    app = Flask(__name__)

    # API 라우트 등록
    from app.routes import register_routes
    register_routes(app)

    return app

