import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()


class SupplyChainGraph:
    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        username = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")
        database = os.getenv("NEO4J_DATABASE", "neo4j")
        if not uri or not username or not password:
            raise ValueError("Missing Neo4j configuration. Copy .env.example to .env and set credentials.")
        self.database = database
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):
        with self.driver.session(database=self.database) as session:
            return [record.data() for record in session.run(query, parameters or {})]

    def create_constraints(self):
        queries = [
            "CREATE CONSTRAINT supplier_name IF NOT EXISTS FOR (s:Supplier) REQUIRE s.name IS UNIQUE",
            "CREATE CONSTRAINT component_name IF NOT EXISTS FOR (c:Component) REQUIRE c.name IS UNIQUE",
            "CREATE CONSTRAINT product_name IF NOT EXISTS FOR (p:Product) REQUIRE p.name IS UNIQUE",
            "CREATE CONSTRAINT plant_name IF NOT EXISTS FOR (p:Plant) REQUIRE p.name IS UNIQUE",
            "CREATE CONSTRAINT country_name IF NOT EXISTS FOR (c:Country) REQUIRE c.name IS UNIQUE",
            "CREATE CONSTRAINT shipment_id IF NOT EXISTS FOR (s:Shipment) REQUIRE s.id IS UNIQUE",
        ]
        for query in queries:
            self.run_query(query)

    def create_sample_graph(self):
        self.run_query("MATCH (n) DETACH DELETE n")
        query = """
        CREATE
          (india:Country {name: 'India'}), (china:Country {name: 'China'}), (germany:Country {name: 'Germany'}),
          (a:Supplier {name: 'Supplier A', risk: 'Low'}), (b:Supplier {name: 'Supplier B', risk: 'High'}),
          (c:Supplier {name: 'Supplier C', risk: 'Medium'}), (d:Supplier {name: 'Supplier D', risk: 'Low'}),
          (x:Component {name: 'Component X', criticality: 'High'}), (y:Component {name: 'Component Y', criticality: 'Medium'}),
          (z:Component {name: 'Component Z', criticality: 'High'}), (w:Component {name: 'Component W', criticality: 'Low'}),
          (alpha:Product {name: 'Product Alpha', category: 'Electronics'}),
          (beta:Product {name: 'Product Beta', category: 'Automotive'}),
          (gamma:Product {name: 'Product Gamma', category: 'Electronics'}),
          (delhi:Plant {name: 'Delhi Plant', capacity: 1000}),
          (pune:Plant {name: 'Pune Plant', capacity: 1500}),
          (chennai:Plant {name: 'Chennai Plant', capacity: 1200}),
          (s101:Shipment {id: '101', status: 'In Transit'}), (s102:Shipment {id: '102', status: 'Delivered'}),
          (s103:Shipment {id: '103', status: 'In Transit'}),
          (a)-[:LOCATED_IN]->(india), (b)-[:LOCATED_IN]->(china), (c)-[:LOCATED_IN]->(germany), (d)-[:LOCATED_IN]->(india),
          (a)-[:SUPPLIES]->(x), (a)-[:SUPPLIES]->(y), (b)-[:SUPPLIES]->(x), (b)-[:SUPPLIES]->(z),
          (c)-[:SUPPLIES]->(y), (c)-[:SUPPLIES]->(w), (d)-[:SUPPLIES]->(z),
          (x)-[:USED_IN]->(alpha), (x)-[:USED_IN]->(beta), (y)-[:USED_IN]->(alpha), (y)-[:USED_IN]->(gamma),
          (z)-[:USED_IN]->(beta), (z)-[:USED_IN]->(gamma), (w)-[:USED_IN]->(gamma),
          (alpha)-[:MANUFACTURED_AT]->(delhi), (alpha)-[:MANUFACTURED_AT]->(pune),
          (beta)-[:MANUFACTURED_AT]->(pune), (beta)-[:MANUFACTURED_AT]->(chennai),
          (gamma)-[:MANUFACTURED_AT]->(chennai),
          (s101)-[:CONTAINS]->(x), (s101)-[:DESTINED_FOR]->(delhi),
          (s102)-[:CONTAINS]->(y), (s102)-[:DESTINED_FOR]->(pune),
          (s103)-[:CONTAINS]->(z), (s103)-[:DESTINED_FOR]->(chennai),
          (b)-[:SUPPLIES_SUPPLIER]->(a)
        """
        self.run_query(query)

    def execute_traversal_queries(self):
        queries = [
            ("Q1 Single-hop: suppliers of Component X", "MATCH (s:Supplier)-[:SUPPLIES]->(c:Component {name: $name}) RETURN s.name AS supplier", {"name": "Component X"}),
            ("Q2 Single-hop: components supplied by Supplier A", "MATCH (s:Supplier {name: $name})-[:SUPPLIES]->(c:Component) RETURN c.name AS component", {"name": "Supplier A"}),
            ("Q3 Multi-hop: Supplier A -> Component -> Product", "MATCH (s:Supplier {name: $name})-[:SUPPLIES]->(:Component)-[:USED_IN]->(p:Product) RETURN DISTINCT p.name AS product", {"name": "Supplier A"}),
            ("Q4 Multi-hop: Supplier A -> Component -> Product -> Plant", "MATCH (s:Supplier {name: $name})-[:SUPPLIES]->(:Component)-[:USED_IN]->(p:Product)-[:MANUFACTURED_AT]->(pl:Plant) RETURN DISTINCT p.name AS product, pl.name AS plant ORDER BY product, plant", {"name": "Supplier A"}),
            ("Q5 Property filter: high-criticality components", "MATCH (s:Supplier)-[:SUPPLIES]->(c:Component {criticality: 'High'}) RETURN s.name AS supplier, c.name AS component", {}),
            ("Q6 Direction query: suppliers located in China", "MATCH (s:Supplier)-[:LOCATED_IN]->(country:Country {name: 'China'}) RETURN s.name AS supplier, country.name AS country", {}),
            ("Q7 Reverse direction: products using Component Z", "MATCH (p:Product)<-[:USED_IN]-(c:Component {name: 'Component Z'}) RETURN p.name AS product", {}),
            ("Q8 Aggregation: number of products per supplier", "MATCH (s:Supplier)-[:SUPPLIES]->(:Component)-[:USED_IN]->(p:Product) RETURN s.name AS supplier, count(DISTINCT p) AS product_count ORDER BY product_count DESC, supplier", {}),
            ("Q9 Aggregation: components per country", "MATCH (s:Supplier)-[:LOCATED_IN]->(country:Country), (s)-[:SUPPLIES]->(c:Component) RETURN country.name AS country, count(DISTINCT c) AS component_count ORDER BY component_count DESC", {}),
            ("Q10 Path query: Supplier B to Chennai Plant", "MATCH path = (s:Supplier {name: 'Supplier B'})-[:SUPPLIES]->(:Component)-[:USED_IN]->(:Product)-[:MANUFACTURED_AT]->(pl:Plant {name: 'Chennai Plant'}) RETURN [n IN nodes(path) | coalesce(n.name, toString(n.id))] AS path", {}),
            ("Q11 Variable-length traversal: Tier-2 supplier chain", "MATCH path = (s:Supplier {name: 'Supplier B'})-[:SUPPLIES_SUPPLIER*1..3]->(target:Supplier) RETURN [n IN nodes(path) | n.name] AS supplier_chain", {}),
            ("Q12 Variable-length mixed traversal: Supplier B to plants", "MATCH path = (s:Supplier {name: 'Supplier B'})-[:SUPPLIES|SUPPLIES_SUPPLIER|USED_IN|MANUFACTURED_AT*1..6]->(target:Plant) RETURN DISTINCT target.name AS plant, length(path) AS hops ORDER BY hops, plant", {}),
        ]
        for title, query, params in queries:
            print(f"\n--- {title} ---")
            for row in self.run_query(query, params):
                print(row)
