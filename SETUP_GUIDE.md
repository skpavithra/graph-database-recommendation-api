# 🚀 Gremlin Server Setup Guide

## Prerequisites
Before running the Flask API, you need to set up and start the Gremlin Server.

## Step 1: Download Apache TinkerPop

1. Visit the Apache TinkerPop downloads page:
   **https://tinkerpop.apache.org/downloads.html**

2. Download the latest **Gremlin Server** (version 3.7.x recommended):
   - Look for: `apache-tinkerpop-gremlin-server-3.7.x-bin.zip`
   - Or use this direct link: https://dlcdn.apache.org/tinkerpop/3.7.2/apache-tinkerpop-gremlin-server-3.7.2-bin.zip

3. Extract the zip file to a convenient location (e.g., `D:\Graphdb\`)

## Step 2: Start Gremlin Server

### On Windows (PowerShell):

```powershell
# Navigate to the extracted directory
cd D:\Graphdb\apache-tinkerpop-gremlin-server-3.7.x

# Start the server with the default configuration
.\bin\gremlin-server.bat conf\gremlin-server.yaml
```

### On Linux/Mac:

```bash
# Navigate to the extracted directory
cd /path/to/apache-tinkerpop-gremlin-server-3.7.x

# Make the script executable (first time only)
chmod +x bin/gremlin-server.sh

# Start the server
./bin/gremlin-server.sh conf/gremlin-server.yaml
```

## Step 3: Verify Server is Running

You should see output similar to:
```
[INFO] GremlinServer - Gremlin Server configured with worker thread pool of 1, gremlin pool of 4 and boss thread pool of 1.
[INFO] GremlinServer - Channel started at port 8182.
```

The server is now accessible at: **ws://localhost:8182/gremlin**

## Step 4: Start Flask API

In a **new terminal window**:

```powershell
# Navigate to the project directory
cd D:\Graphdb\boardgame-graph

# Activate virtual environment
.venv\Scripts\Activate.ps1

# Start Flask application
python app.py
```

## Step 5: Test the API

1. Open your browser and go to: **http://127.0.0.1:5000**
2. Access Swagger UI: **http://127.0.0.1:5000/swagger**
3. Initialize sample data:
   ```powershell
   curl -X POST http://127.0.0.1:5000/init
   ```

## Troubleshooting

### Issue: "Connection refused" error
- **Solution**: Make sure Gremlin Server is running on port 8182
- Check if another process is using port 8182: `netstat -ano | findstr :8182`

### Issue: Gremlin Server won't start
- **Solution**: Check Java is installed: `java -version`
- Apache TinkerPop requires Java 8 or higher

### Issue: Flask app can't find modules
- **Solution**: Make sure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

## Configuration

The default configuration uses:
- **Gremlin Server**: ws://localhost:8182/gremlin
- **Flask Server**: http://0.0.0.0:5000

To change these settings, edit:
- `graph_utils.py` - Update `GREMLIN_URL`
- `app.py` - Update `app.run()` parameters

## Next Steps

Once both servers are running:
1. Initialize the graph database with sample data
2. Test the recommendation endpoints
3. Explore the API using Swagger UI
4. Add your own board games and relationships!

## Available Games in Sample Data

- **Catan** (Trading, Strategy)
- **Terraforming Mars** (Engine Building, Strategy)
- **Everdell** (Worker Placement, Engine Building)
- **Wingspan** (Engine Building, Card Drafting)
- **Azul** (Pattern Building)
