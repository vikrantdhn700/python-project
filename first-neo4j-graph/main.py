import os

from dotenv import load_dotenv
from neo4j import GraphDatabase


load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI", "neo4j://localhost:7687")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")


class LearningPlatformGraph:

    def __init__(self, uri, username, password, database):
        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password)
        )

        self.database = database

    def close(self):
        self.driver.close()

    # --------------------------------
    # CONNECTION
    # --------------------------------

    def verify_connection(self):
        self.driver.verify_connectivity()
        print("Connected to Neo4j.")

    # --------------------------------
    # DELETE OLD DEMO DATA
    # --------------------------------

    def clear_demo_graph(self):

        query = """
        MATCH (n)
        WHERE n.demo = true
        DETACH DELETE n
        """

        with self.driver.session(
            database=self.database
        ) as session:

            session.run(query).consume()

        print("Demo graph cleared.")

    # --------------------------------
    # CREATE GRAPH
    # --------------------------------

    def create_graph(self):

        nodes = [

            # Students
            (
                "Student",
                {
                    "id": "S1",
                    "name": "Aarav",
                    "city": "Delhi"
                }
            ),

            (
                "Student",
                {
                    "id": "S2",
                    "name": "Priya",
                    "city": "Mumbai"
                }
            ),

            (
                "Student",
                {
                    "id": "S3",
                    "name": "Rahul",
                    "city": "Bengaluru"
                }
            ),

            (
                "Student",
                {
                    "id": "S4",
                    "name": "Neha",
                    "city": "Pune"
                }
            ),

            # Courses
            (
                "Course",
                {
                    "id": "C1",
                    "title": "Python Backend"
                }
            ),

            (
                "Course",
                {
                    "id": "C2",
                    "title": "React Development"
                }
            ),

            (
                "Course",
                {
                    "id": "C3",
                    "title": "AI Engineering"
                }
            ),

            (
                "Course",
                {
                    "id": "C4",
                    "title": "Database Design"
                }
            ),

            # Mentors
            (
                "Mentor",
                {
                    "id": "M1",
                    "name": "Anita Sharma"
                }
            ),

            (
                "Mentor",
                {
                    "id": "M2",
                    "name": "Rohit Mehta"
                }
            ),

            (
                "Mentor",
                {
                    "id": "M3",
                    "name": "Karan Singh"
                }
            ),

            # Skills
            (
                "Skill",
                {
                    "id": "SK1",
                    "name": "Python"
                }
            ),

            (
                "Skill",
                {
                    "id": "SK2",
                    "name": "FastAPI"
                }
            ),

            (
                "Skill",
                {
                    "id": "SK3",
                    "name": "React"
                }
            ),

            (
                "Skill",
                {
                    "id": "SK4",
                    "name": "Neo4j"
                }
            ),

            (
                "Skill",
                {
                    "id": "SK5",
                    "name": "PostgreSQL"
                }
            ),

            # Projects
            (
                "Project",
                {
                    "id": "P1",
                    "name": "Support Ticket API"
                }
            ),

            (
                "Project",
                {
                    "id": "P2",
                    "name": "E-Commerce Platform"
                }
            ),

            (
                "Project",
                {
                    "id": "P3",
                    "name": "AI Course Assistant"
                }
            ),

            # Companies
            (
                "Company",
                {
                    "id": "CO1",
                    "name": "TechNova"
                }
            ),

            (
                "Company",
                {
                    "id": "CO2",
                    "name": "DataWorks"
                }
            ),
        ]

        relationships = [

            # Student -> Course
            ("S1", "ENROLLED_IN", "C1"),
            ("S1", "ENROLLED_IN", "C3"),
            ("S2", "ENROLLED_IN", "C1"),
            ("S2", "ENROLLED_IN", "C2"),
            ("S3", "ENROLLED_IN", "C3"),
            ("S3", "ENROLLED_IN", "C4"),
            ("S4", "ENROLLED_IN", "C2"),
            ("S4", "ENROLLED_IN", "C4"),

            # Mentor -> Course
            ("M1", "TEACHES", "C1"),
            ("M1", "TEACHES", "C3"),
            ("M2", "TEACHES", "C2"),
            ("M3", "TEACHES", "C4"),

            # Course -> Skill
            ("C1", "TEACHES_SKILL", "SK1"),
            ("C1", "TEACHES_SKILL", "SK2"),
            ("C2", "TEACHES_SKILL", "SK3"),
            ("C3", "TEACHES_SKILL", "SK1"),
            ("C3", "TEACHES_SKILL", "SK4"),
            ("C4", "TEACHES_SKILL", "SK4"),
            ("C4", "TEACHES_SKILL", "SK5"),

            # Student -> Project
            ("S1", "BUILT", "P1"),
            ("S2", "BUILT", "P2"),
            ("S3", "BUILT", "P3"),
            ("S4", "BUILT", "P1"),

            # Project -> Skill
            ("P1", "USES", "SK1"),
            ("P1", "USES", "SK2"),
            ("P1", "USES", "SK4"),
            ("P2", "USES", "SK1"),
            ("P2", "USES", "SK3"),
            ("P2", "USES", "SK5"),
            ("P3", "USES", "SK1"),
            ("P3", "USES", "SK4"),

            # Student -> Company
            ("S1", "INTERESTED_IN", "CO1"),
            ("S2", "INTERESTED_IN", "CO2"),
            ("S3", "INTERESTED_IN", "CO1"),
            ("S4", "INTERESTED_IN", "CO2"),
        ]

        with self.driver.session(
            database=self.database
        ) as session:

            # Create nodes
            for label, properties in nodes:

                query = f"""
                CREATE (n:{label} $props)
                """

                session.run(
                    query,
                    props={
                        **properties,
                        "demo": True
                    }
                ).consume()

            # Create relationships
            for start_id, relationship, end_id in relationships:

                query = f"""
                MATCH (a {{id: $start_id, demo: true}})
                MATCH (b {{id: $end_id, demo: true}})
                CREATE (a)-[:{relationship}]->(b)
                """

                session.run(
                    query,
                    start_id=start_id,
                    end_id=end_id
                ).consume()

        print(
            f"Created {len(nodes)} nodes "
            f"and {len(relationships)} relationships."
        )

    # --------------------------------
    # READ GRAPH
    # --------------------------------

    def read_graph(self):

        query = """
        MATCH (a)-[r]->(b)
        WHERE a.demo = true
          AND b.demo = true

        RETURN
            labels(a) AS from_labels,
            a.name AS from_name,
            type(r) AS relationship,
            labels(b) AS to_labels,
            b.name AS to_name

        ORDER BY from_name, relationship, to_name
        """

        with self.driver.session(
            database=self.database
        ) as session:

            rows = session.run(query).data()

        print("\nGraph relationships:\n")

        for row in rows:

            print(
                f"{row['from_labels']} "
                f"{row['from_name']} "
                f"-[:{row['relationship']}]-> "
                f"{row['to_labels']} "
                f"{row['to_name']}"
            )

    # --------------------------------
    # COUNT GRAPH
    # --------------------------------

    def show_counts(self):

        query = """
        MATCH (n)
        WHERE n.demo = true

        OPTIONAL MATCH (n)-[r]->()

        RETURN
            count(DISTINCT n) AS nodes,
            count(r) AS relationships
        """

        with self.driver.session(
            database=self.database
        ) as session:

            result = session.run(query).single()

        print(
            f"Current demo graph: "
            f"{result['nodes']} nodes, "
            f"{result['relationships']} relationships."
        )

    # --------------------------------
    # UPDATE
    # --------------------------------

    def update_student(self):

        query = """
        MATCH (s:Student {
            id: $id,
            demo: true
        })

        SET
            s.city = $city,
            s.updated = true

        RETURN
            s.id AS id,
            s.name AS name,
            s.city AS city
        """

        with self.driver.session(
            database=self.database
        ) as session:

            result = session.run(
                query,
                id="S1",
                city="Hyderabad"
            ).single()

        print(
            f"Updated student: "
            f"{result['name']} "
            f"({result['id']}) -> "
            f"{result['city']}"
        )

    # --------------------------------
    # DELETE RELATIONSHIP
    # --------------------------------

    def delete_relationship(self):

        query = """
        MATCH (
            s:Student {
                id: $student_id,
                demo: true
            }
        )-[r:INTERESTED_IN]->(
            c:Company {
                id: $company_id,
                demo: true
            }
        )

        DELETE r

        RETURN count(r) AS deleted
        """

        with self.driver.session(
            database=self.database
        ) as session:

            result = session.run(
                query,
                student_id="S4",
                company_id="CO2"
            ).single()

        print(
            f"Deleted relationships: "
            f"{result['deleted']}"
        )

    # --------------------------------
    # DELETE NODE
    # --------------------------------

    def delete_node(self):

        query = """
        MATCH (p:Project {
            id: $id,
            demo: true
        })

        DETACH DELETE p

        RETURN count(p) AS deleted
        """

        with self.driver.session(
            database=self.database
        ) as session:

            result = session.run(
                query,
                id="P3"
            ).single()

        print(
            f"Deleted project nodes: "
            f"{result['deleted']}"
        )


def main():

    graph = LearningPlatformGraph(
        NEO4J_URI,
        NEO4J_USERNAME,
        NEO4J_PASSWORD,
        NEO4J_DATABASE
    )

    try:

        graph.verify_connection()

        print("\n--- CLEAR OLD DATA ---")
        graph.clear_demo_graph()

        print("\n--- CREATE ---")
        graph.create_graph()

        print("\n--- READ ---")
        graph.show_counts()
        graph.read_graph()

        print("\n--- UPDATE ---")
        graph.update_student()

        print("\n--- DELETE RELATIONSHIP ---")
        graph.delete_relationship()

        print("\n--- DELETE NODE ---")
        graph.delete_node()

        print("\n--- FINAL GRAPH ---")
        graph.show_counts()
        graph.read_graph()

    finally:

        graph.close()


if __name__ == "__main__":
    main()
