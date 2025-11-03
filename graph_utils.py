from gremlin_python.driver import client

GREMLIN_URL = "ws://localhost:8182/gremlin"
client_conn = None

def get_client():
    """Lazy initialization of the Gremlin client"""
    global client_conn
    if client_conn is None:
        client_conn = client.Client(GREMLIN_URL, 'g')
    return client_conn

def add_sample_data():
    """Add sample board game data with mechanics and designers"""
    client = get_client()
    games = [
        ("Catan", ["Trading", "Strategy"], ["Klaus Teuber"]),
        ("Terraforming Mars", ["Engine Building", "Strategy"], ["Jacob Fryxelius"]),
        ("Everdell", ["Worker Placement", "Engine Building"], ["James Wilson"]),
        ("Wingspan", ["Engine Building", "Card Drafting"], ["Elizabeth Hargrave"]),
        ("Azul", ["Pattern Building"], ["Michael Kiesling"])
    ]

    try:
        client.submit("g.V().drop()").all().result()
    except Exception as e:
        print(f"Warning clearing data: {e}")

    for name, mechanics, designers in games:
        client.submit(
            f"g.addV('game').property('name','{name}').next()"
        ).all().result()
        
        for mechanic in mechanics:
            client.submit(
                f"g.V().has('mechanic','name','{mechanic}').fold().coalesce(unfold(), addV('mechanic').property('name','{mechanic}')).next()"
            ).all().result()
            
            client.submit(
                f"g.V().has('game','name','{name}').as('g').V().has('mechanic','name','{mechanic}').coalesce(__.inE('has_mechanic').where(outV().as('g')), addE('has_mechanic').from('g')).next()"
            ).all().result()
        
        for designer in designers:
            client.submit(
                f"g.V().has('designer','name','{designer}').fold().coalesce(unfold(), addV('designer').property('name','{designer}')).next()"
            ).all().result()
            
            client.submit(
                f"g.V().has('game','name','{name}').as('g').V().has('designer','name','{designer}').coalesce(__.inE('designed_by').where(outV().as('g')), addE('designed_by').from('g')).next()"
            ).all().result()

def get_similar_games(game_name):
    """Find similar games based on shared mechanics or designers"""
    client = get_client()
    query = f"""
        g.V().has('game','name','{game_name}').as('g1')
        .out('has_mechanic', 'designed_by')
        .in('has_mechanic', 'designed_by')
        .hasLabel('game')
        .where(neq('g1'))
        .dedup()
        .values('name')
    """
    try:
        results = client.submit(query).all().result()
        return [r for r in results]
    except Exception as e:
        print(f"Error getting similar games: {e}")
        return []

def get_game_details(game_name):
    """Get detailed information about a specific game"""
    client = get_client()
    query = f"g.V().has('game','name','{game_name}').valueMap(true)"
    try:
        results = client.submit(query).all().result()
        if results:
            cleaned_results = []
            for result in results:
                cleaned = {}
                for key, value in result.items():
                    if isinstance(value, list) and len(value) == 1:
                        cleaned[key] = value[0]
                    elif isinstance(value, list):
                        cleaned[key] = value
                    else:
                        cleaned[key] = value
                cleaned_results.append(cleaned)
            return cleaned_results
        return []
    except Exception as e:
        print(f"Error getting game details: {e}")
        return []
