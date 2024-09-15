from flask import Flask
from flask_cors import CORS
from routes import faq_blueprint

app = Flask(__name__)

# Enabe CORS for all routes
CORS(app)

# Register the FAQ blueprint for API routes
app.register_blueprint(faq_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
