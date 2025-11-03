# Board Game Recommendation Graph API

A Flask-based REST API using Apache TinkerPop graph database to provide board game recommendations based on shared mechanics and designers.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Apache TinkerPop Gremlin Server
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd boardgame-graph
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   .venv\Scripts\Activate.ps1
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Gremlin Server** (see [SETUP_GUIDE.md](SETUP_GUIDE.md))
   ```bash
   # Navigate to your Gremlin Server directory
   cd apache-tinkerpop-gremlin-server-3.7.x
   
   # Windows
   .\bin\gremlin-server.bat conf\gremlin-server.yaml
   
   # Linux/Mac
   ./bin/gremlin-server.sh conf/gremlin-server.yaml
   ```

5. **Run the API**
   ```bash
   python app.py
   ```

6. **Access the API**
   - Home: http://127.0.0.1:5000
   - Swagger UI: http://127.0.0.1:5000/swagger

## 📚 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| POST | `/init` | Initialize sample data |
| GET | `/recommend/<game>` | Get similar games |
| GET | `/details/<game>` | Get game details |
| GET | `/swagger` | Interactive API docs |

## 🎮 Sample Games

- **Catan** - Trading, Strategy
- **Terraforming Mars** - Engine Building, Strategy
- **Everdell** - Worker Placement, Engine Building
- **Wingspan** - Engine Building, Card Drafting
- **Azul** - Pattern Building

## 📖 Documentation

- [Setup Guide](SETUP_GUIDE.md) - Detailed Gremlin Server setup
- [README](README.md) - Full project documentation

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** Apache TinkerPop / TinkerGraph
- **Query Language:** Gremlin
- **API Docs:** Swagger UI

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes.

## 📧 Support

For issues or questions, refer to the [SETUP_GUIDE.md](SETUP_GUIDE.md) or open an issue.
