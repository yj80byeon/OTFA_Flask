from flask import jsonify

def register_routes(app):

    @app.route("/", methods=["GET"])
    def index():
        return jsonify({
            "message"   : "Flask server is running!",
            "status"    : "success"
        })

    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({
            "status"    : "healthy"
        })

    @app.route("/api/hello", methods=["GET"])
    def hello():
        return jsonify({
            "message"   : "Hellow, World!",
            "python"    : "3.12.3",
            "framework" : "Flask"
        })