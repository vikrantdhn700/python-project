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
            raise ValueError(
                "Missing Neo4j configuration. "
                "Copy .env.example to .env and set NEO4J_URI, "
                "NEO4J_USERNAME and NEO4J_PASSWORD."
            )

        self.database = database
        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password)
        )

        self.driver.verify_connectivity()

    def close(self):
        self.driver.close()

    def create_constraints(self):
        queries = [
            """
            CREATE CONSTRAINT supplier_name_unique IF NOT EXISTS
            FOR (s:Supplier)
            REQUIRE s.name IS UNIQUE
            """,
            """
            CREATE CONSTRAINT component_name_unique IF NOT EXISTS
            FOR (c:Component)
            REQUIRE c.name IS UNIQUE
            """,
            """
            CREATE CONSTRAINT product_name_unique IF NOT EXISTS
            FOR (p:Product)
            REQUIRE p.name IS UNIQUE
            """,
            """
            CREATE CONSTRAINT plant_name_unique IF NOT EXISTS
            FOR (p:Plant)
            REQUIRE p.name IS UNIQUE
            """,
            """
            CREATE CONSTRAINT country_name_unique IF NOT EXISTS
            FOR (c:Country)
            REQUIRE c.name IS UNIQUE
            """,
            """
            CREATE CONSTRAINT shipment_id_unique IF NOT EXISTS
            FOR (s:Shipment)
            REQUIRE s.id IS UNIQUE
            """
        ]

        with self.driver.session(database=self.database) as session:
            for query in queries:
                session.run(query).consume()

    def create_sample_graph(self):
        with self.driver.session(database=self.database) as session:
            session.run(
                """
                MERGE (c:Country {name: "India"})
                MERGE (c2:Country {name: "China"})
                MERGE (c3:Country {name: "Germany"})

                MERGE (s1:Supplier {name: "Supplier A"})
                MERGE (s2:Supplier {name: "Supplier B"})
                MERGE (s3:Supplier {name: "Supplier C"})
                MERGE (s4:Supplier {name: "Supplier D"})

                MERGE (x:Component {name: "Component X"})
                MERGE (y:Component {name: "Component Y"})
                MERGE (z:Component {name: "Component Z"})
                MERGE (w:Component {name: "Component W"})

                MERGE (pa:Product {name: "Product Alpha"})
                MERGE (pb:Product {name: "Product Beta"})
                MERGE (pg:Product {name: "Product Gamma"})

                MERGE (pd:Plant {name: "Plant Delhi"})
                MERGE (pp:Plant {name: "Plant Pune"})
                MERGE (pc:Plant {name: "Plant Chennai"})

                MERGE (sh1:Shipment {id: "Shipment 101"})
                MERGE (sh2:Shipment {id: "Shipment 102"})
                MERGE (sh3:Shipment {id: "Shipment 103"})

                MERGE (s1)-[:LOCATED_IN]->(c)
                MERGE (s2)-[:LOCATED_IN]->(c2)
                MERGE (s3)-[:LOCATED_IN]->(c3)
                MERGE (s4)-[:LOCATED_IN]->(c)

                MERGE (s1)-[:SUPPLIES]->(x)
                MERGE (s1)-[:SUPPLIES]->(y)
                MERGE (s2)-[:SUPPLIES]->(x)
                MERGE (s2)-[:SUPPLIES]->(z)
                MERGE (s3)-[:SUPPLIES]->(y)
                MERGE (s3)-[:SUPPLIES]->(w)
                MERGE (s4)-[:SUPPLIES]->(z)

                MERGE (x)-[:USED_IN]->(pa)
                MERGE (x)-[:USED_IN]->(pb)
                MERGE (y)-[:USED_IN]->(pa)
                MERGE (y)-[:USED_IN]->(pg)
                MERGE (z)-[:USED_IN]->(pb)
                MERGE (z)-[:USED_IN]->(pg)
                MERGE (w)-[:USED_IN]->(pg)

                MERGE (pa)-[:MANUFACTURED_AT]->(pd)
                MERGE (pa)-[:MANUFACTURED_AT]->(pp)
                MERGE (pb)-[:MANUFACTURED_AT]->(pp)
                MERGE (pb)-[:MANUFACTURED_AT]->(pc)
                MERGE (pg)-[:MANUFACTURED_AT]->(pc)

                MERGE (sh1)-[:CONTAINS]->(x)
                MERGE (sh1)-[:DESTINED_FOR]->(pd)
                MERGE (sh2)-[:CONTAINS]->(y)
                MERGE (sh2)-[:DESTINED_FOR]->(pp)
                MERGE (sh3)-[:CONTAINS]->(z)
                MERGE (sh3)-[:DESTINED_FOR]->(pc)

                // Tier-2 relationship: Supplier B supplies Supplier A.
                MERGE (s2)-[:SUPPLIES_SUPPLIER]->(s1)
                """
            ).consume()

    def _run(self, query, **params):
        with self.driver.session(database=self.database) as session:
            result = session.run(query, **params)
            return [record.data() for record in result]

    def products_depending_on_supplier(self, supplier_name):
        return self._run(
            """
            MATCH (s:Supplier {name: $supplier_name})
                  -[:SUPPLIES]->(c:Component)
                  -[:USED_IN]->(p:Product)
            RETURN DISTINCT
                s.name AS supplier,
                c.name AS component,
                p.name AS product
            ORDER BY product, component
            """,
            supplier_name=supplier_name
        )

    def plants_affected_by_component(self, component_name):
        return self._run(
            """
            MATCH (c:Component {name: $component_name})
                  -[:USED_IN]->(p:Product)
                  -[:MANUFACTURED_AT]->(plant:Plant)
            RETURN DISTINCT
                c.name AS component,
                p.name AS product,
                plant.name AS affected_plant
            ORDER BY affected_plant, product
            """,
            component_name=component_name
        )

    def suppliers_connected_to_product(self, product_name):
        return self._run(
            """
            MATCH (s:Supplier)
                  -[:SUPPLIES]->(c:Component)
                  -[:USED_IN]->(p:Product {name: $product_name})
            RETURN DISTINCT
                s.name AS supplier,
                c.name AS component,
                p.name AS product
            ORDER BY supplier, component
            """,
            product_name=product_name
        )

    def tier2_supplier_to_plants(self, supplier_name):
        return self._run(
            """
            MATCH (s:Supplier {name: $supplier_name})
                  -[:SUPPLIES_SUPPLIER]->(tier1:Supplier)
                  -[:SUPPLIES]->(c:Component)
                  -[:USED_IN]->(p:Product)
                  -[:MANUFACTURED_AT]->(plant:Plant)
            RETURN
                s.name AS tier2_supplier,
                tier1.name AS tier1_supplier,
                c.name AS component,
                p.name AS product,
                plant.name AS plant
            ORDER BY plant, product, component
            """,
            supplier_name=supplier_name
        )

    def components_from_country_used_in_products(self, country_name):
        return self._run(
            """
            MATCH (s:Supplier)-[:LOCATED_IN]->(country:Country {name: $country_name}),
                  (s)-[:SUPPLIES]->(c:Component)
                  -[:USED_IN]->(p:Product)
            RETURN DISTINCT
                country.name AS country,
                s.name AS supplier,
                c.name AS component,
                p.name AS product
            ORDER BY supplier, component, product
            """,
            country_name=country_name
        )

    def suppliers_of_component(self, component_name):
        return self._run(
            """
            MATCH (s:Supplier)-[:SUPPLIES]->(c:Component {name: $component_name})
            RETURN s.name AS supplier, c.name AS component
            ORDER BY supplier
            """,
            component_name=component_name
        )

    def components_with_multiple_suppliers(self):
        return self._run(
            """
            MATCH (s:Supplier)-[:SUPPLIES]->(c:Component)
            WITH c, count(DISTINCT s) AS supplier_count
            WHERE supplier_count > 1
            RETURN c.name AS component, supplier_count
            ORDER BY supplier_count DESC, component
            """
        )

    def single_supplier_components(self):
        return self._run(
            """
            MATCH (s:Supplier)-[:SUPPLIES]->(c:Component)
            WITH c, collect(DISTINCT s.name) AS suppliers
            WHERE size(suppliers) = 1
            RETURN c.name AS component, suppliers
            ORDER BY component
            """
        )

    def plants_dependent_on_supplier(self, supplier_name):
        return self._run(
            """
            MATCH (s:Supplier {name: $supplier_name})
                  -[:SUPPLIES]->(c:Component)
                  -[:USED_IN]->(p:Product)
                  -[:MANUFACTURED_AT]->(plant:Plant)
            RETURN DISTINCT
                s.name AS supplier,
                c.name AS component,
                p.name AS product,
                plant.name AS plant
            ORDER BY plant, product, component
            """,
            supplier_name=supplier_name
        )

    def shortest_dependency_path(self, supplier_name, plant_name):
        return self._run(
            """
            MATCH (s:Supplier {name: $supplier_name}),
                  (plant:Plant {name: $plant_name})
            MATCH path = shortestPath((s)-[*]-(plant))
            RETURN
                [n IN nodes(path) |
                    CASE
                        WHEN n:Supplier THEN n.name
                        WHEN n:Component THEN n.name
                        WHEN n:Product THEN n.name
                        WHEN n:Plant THEN n.name
                        WHEN n:Country THEN n.name
                        WHEN n:Shipment THEN n.id
                    END
                ] AS path
            """,
            supplier_name=supplier_name,
            plant_name=plant_name
        )
