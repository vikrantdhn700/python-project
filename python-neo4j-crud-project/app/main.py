from app.database import Neo4jDatabase


def print_students(title, students):
    print(f"\n--- {title} ---")
    if not students:
        print("No students found.")
        return
    for student in students:
        print(student)


def main():
    db = Neo4jDatabase()

    try:
        db.verify_connection()
        print("Neo4j connection successful!")

        deleted = db.clear_demo_data()
        print(f"Existing demo nodes removed: {deleted}")

        print("\n1. CREATE NODES")
        print(db.create_student("Alice", 22, "Delhi"))
        print(db.create_student("Bob", 24, "Mumbai"))
        print(db.create_student("Charlie", 21, "Delhi"))

        print("\n2. CREATE RELATIONSHIPS")
        print(db.create_friendship("Alice", "Bob"))
        print(db.create_friendship("Alice", "Charlie"))

        print_students("3. READ ALL STUDENTS", db.read_students())

        print_students(
            "4. SEARCH: CITY = Delhi",
            db.search_students(city="Delhi"),
        )

        print_students(
            "SEARCH: MINIMUM AGE = 22",
            db.search_students(min_age=22),
        )

        print("\n5. UPDATE STUDENT")
        print(db.update_student("Alice", age=23, city="Bangalore"))

        print("\n6. DELETE RELATIONSHIP")
        # deleted_relationships = db.delete_relationship("Alice", "Bob")
        # print(f"Deleted relationships: {deleted_relationships}")

        print("\n7. DELETE NODE")
        # deleted_nodes = db.delete_student("Charlie")
        # print(f"Deleted nodes: {deleted_nodes}")

        print_students("FINAL STUDENTS", db.read_students())

        print("\nAll Neo4j operations completed successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    main()
