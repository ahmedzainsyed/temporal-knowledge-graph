from app.db.neo4j import execute_query

def reconstruct_entity_state(entity_id, timestamp):

    query = '''
    MATCH (e:Entity {id: $entity_id})-[:HAS_EVENT]->(ev:Event)
    WHERE ev.timestamp <= datetime($timestamp)
    RETURN ev
    ORDER BY ev.timestamp ASC
    '''

    records = execute_query(
        query,
        {
            "entity_id": entity_id,
            "timestamp": timestamp
        }
    )

    state = {}

    for record in records:

        payload = record["ev"]["payload"]

        for key, value in payload.items():
            state[key] = value

    return state