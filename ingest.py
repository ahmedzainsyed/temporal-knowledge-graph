from app.db.neo4j import execute_query

def temporal_neighbors(entity_id, hops):

    query = f'''
    MATCH path=(e:Entity {{id: $entity_id}})-[*1..{hops}]-(n)
    RETURN DISTINCT n.id AS neighbor
    LIMIT 100
    '''

    records = execute_query(
        query,
        {
            "entity_id": entity_id
        }
    )

    return [record["neighbor"] for record in records]