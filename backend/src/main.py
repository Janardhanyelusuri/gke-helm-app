from flask import Flask, jsonify
from flask_cors import CORS
import os
import socket

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Backend is running successfully on GKE!',
        'service': 'backend',
        'version': '1.0.0',
        'hostname': socket.gethostname()
    })

@app.route('/api/info', methods=['GET'])
def info():
    """Application info endpoint"""
    return jsonify({
        'message': 'GKE Helm Deployment',
        'platform': 'Google Kubernetes Engine',
        'environment': os.getenv('ENV', 'production'),
        'deployment': 'Helm Charts',
        'ci_cd': 'GitHub Actions'
    })

@app.route('/', methods=['GET'])
def root():
    """Root endpoint"""
    return jsonify({
        'message': 'Backend API is running',
        'endpoints': {
            'health': '/api/health',
            'info': '/api/info'
        }
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
