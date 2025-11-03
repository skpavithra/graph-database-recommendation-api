from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
from graph_utils import add_sample_data, get_similar_games, get_game_details

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Welcome to Board Game Recommendation API",
        "endpoints": {
            "POST /init": "Load sample data into the graph",
            "GET /recommend/<game>": "Get game recommendations",
            "GET /details/<game>": "Get details for a specific game",
            "GET /swagger": "API documentation"
        }
    })

@app.route('/init', methods=['POST'])
def init_data():
    """Initialize the graph database with sample board game data"""
    try:
        add_sample_data()
        return jsonify({
            "message": "Sample data added successfully!",
            "games_added": ["Catan", "Terraforming Mars", "Everdell", "Wingspan", "Azul"]
        }), 200
    except Exception as e:
        return jsonify({
            "error": "Failed to initialize data",
            "details": str(e)
        }), 500

@app.route('/recommend/<game>', methods=['GET'])
def recommend(game):
    """Get recommendations for similar games"""
    try:
        results = get_similar_games(game)
        return jsonify({
            "game": game,
            "recommendations": results,
            "count": len(results)
        }), 200
    except Exception as e:
        return jsonify({
            "error": "Failed to get recommendations",
            "details": str(e)
        }), 500

@app.route('/details/<game>', methods=['GET'])
def details(game):
    """Get detailed information about a specific game"""
    try:
        game_details = get_game_details(game)
        if not game_details:
            return jsonify({
                "error": "Game not found",
                "game": game
            }), 404
        return jsonify({
            "game": game,
            "details": game_details
        }), 200
    except Exception as e:
        return jsonify({
            "error": "Failed to get game details",
            "details": str(e)
        }), 500
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swagger_bp = get_swaggerui_blueprint(
    SWAGGER_URL, 
    API_URL, 
    config={'app_name': "Board Game Graph API"}
)
app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    print("=" * 60)
    print("Board Game Recommendation API Server")
    print("=" * 60)
    print("Server starting on http://127.0.0.1:5000")
    print("")
    print("Available endpoints:")
    print("  - GET  /              : Home (API info)")
    print("  - POST /init          : Initialize sample data")
    print("  - GET  /recommend/<game> : Get recommendations")
    print("  - GET  /details/<game>   : Get game details")
    print("  - GET  /swagger       : API documentation")
    print("")
    print("Make sure Gremlin Server is running on ws://localhost:8182")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
