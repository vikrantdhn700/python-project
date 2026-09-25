import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()


class Neo4jDatabase:
    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        username = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")
        self.database = os.getenv("NEO4J_DATABASE", "neo4j")

        if not uri or not username or not password:
            raise ValueError(
                "Missing Neo4j environment variables. "
                "Configure .env using .env.example."
            )

        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password),
        )

    def verify_connection(self):
        self.driver.verify_connectivity()

    def close(self):
        self.driver.close()

    def create_student(self, name, age, city):
        query = """
        CREATE (s:Student {
            name: $name,
            age: $age,
            city: $city
        })
        RETURN elementId(s) AS id,
               s.name AS name,
               s.age AS age,
               s.city AS city
        """
        records, _, _ = self.driver.execute_query(
            query,
            name=name,
            age=age,
            city=city,
            database_=self.database,
        )
        return records[0].data()

    def create_friendship(self, student1_name, student2_name):
        query = """
        MATCH (s1:Student {name: $student1_name})
        MATCH (s2:Student {name: $student2_name})
        CREATE (s1)-[r:FRIEND_OF]->(s2)
        RETURN s1.name AS from_student,
               type(r) AS relationship,
               s2.name AS to_student
        """
        records, _, _ = self.driver.execute_query(
            query,
            student1_name=student1_name,
            student2_name=student2_name,
            database_=self.database,
        )
        return records[0].data() if records else None

    def read_students(self):
        query = """
        MATCH (s:Student)
        RETURN elementId(s) AS id,
               s.name AS name,
               s.age AS age,
               s.city AS city
        ORDER BY s.name
        """
        records, _, _ = self.driver.execute_query(
            query,
            database_=self.database,
        )
        return [record.data() for record in records]

    def search_students(self, city=None, min_age=None):
        query = """
        MATCH (s:Student)
        WHERE ($city IS NULL OR s.city = $city)
          AND ($min_age IS NULL OR s.age >= $min_age)
        RETURN elementId(s) AS id,
               s.name AS name,
               s.age AS age,
               s.city AS city
        ORDER BY s.name
        """
        records, _, _ = self.driver.execute_query(
            query,
            city=city,
            min_age=min_age,
            database_=self.database,
        )
        return [record.data() for record in records]

    def update_student(self, name, age=None, city=None):
        query = """
        MATCH (s:Student {name: $name})
        SET s.age = coalesce($age, s.age),
            s.city = coalesce($city, s.city)
        RETURN elementId(s) AS id,
               s.name AS name,
               s.age AS age,
               s.city AS city
        """
        records, _, _ = self.driver.execute_query(
            query,
            name=name,
            age=age,
            city=city,
            database_=self.database,
        )
        return records[0].data() if records else None

    def delete_relationship(self, student1_name, student2_name):
        query = """
        MATCH (s1:Student {name: $student1_name})
              -[r:FRIEND_OF]->
              (s2:Student {name: $student2_name})
        DELETE r
        RETURN count(r) AS deleted_relationships
        """
        records, _, _ = self.driver.execute_query(
            query,
            student1_name=student1_name,
            student2_name=student2_name,
            database_=self.database,
        )
        return records[0]["deleted_relationships"]

    def delete_student(self, name):
        query = """
        MATCH (s:Student {name: $name})
        DETACH DELETE s
        RETURN count(s) AS deleted_nodes
        """
        records, _, _ = self.driver.execute_query(
            query,
            name=name,
            database_=self.database,
        )
        return records[0]["deleted_nodes"]

    def clear_demo_data(self):
        query = """
        MATCH (s:Student)
        DETACH DELETE s
        RETURN count(s) AS deleted_nodes
        """
        records, _, _ = self.driver.execute_query(
            query,
            database_=self.database,
        )
        return records[0]["deleted_nodes"]
