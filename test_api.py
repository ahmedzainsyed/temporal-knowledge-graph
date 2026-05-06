from neo4j import GraphDatabase

URI = "bolt://neo4j:7687"
USERNAME = "neo4j"
PASSWORD = "password"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

def execute_query(query, parameters=None):

    with driver.session() as session:

        result = session.run(query, parameters)

        return [record for record in result]