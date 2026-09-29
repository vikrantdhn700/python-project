from app.graph_manager import SupplyChainGraph


def print_section(title: str):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def print_rows(rows):
    if not rows:
        print("No results found.")
        return

    for row in rows:
        print(" | ".join(f"{key}: {value}" for key, value in row.items()))


def main():
    graph = SupplyChainGraph()

    try:
        print_section("1. Creating constraints")
        graph.create_constraints()
        print("Constraints created.")

        print_section("2. Creating supply-chain graph")
        graph.create_sample_graph()
        print("Sample graph created.")

        print_section("3. Which products depend on Supplier A?")
        print_rows(graph.products_depending_on_supplier("Supplier A"))

        print_section(
            "4. Which plants could be affected if Component X is unavailable?")
        print_rows(graph.plants_affected_by_component("Component X"))

        print_section("5. Find all suppliers connected to Product Beta")
        print_rows(graph.suppliers_connected_to_product("Product Beta"))

        print_section(
            "6. Find dependency paths from Tier-2 Supplier B to plants")
        print_rows(graph.tier2_supplier_to_plants("Supplier B"))

        print_section("7. Components supplied by suppliers from China")
        print_rows(graph.components_from_country_used_in_products("China"))

        print_section("8. Suppliers of Component X")
        print_rows(graph.suppliers_of_component("Component X"))

        print_section("9. Components with multiple suppliers")
        print_rows(graph.components_with_multiple_suppliers())

        print_section("10. Single-supplier components")
        print_rows(graph.single_supplier_components())

        print_section("11. All plants dependent on Supplier A")
        print_rows(graph.plants_dependent_on_supplier("Supplier A"))

        print_section(
            "12. Shortest dependency path: Supplier B -> Plant Chennai")
        paths = graph.shortest_dependency_path("Supplier B", "Plant Chennai")
        if paths:
            for row in paths:
                print(row["path"])
        else:
            print("No path found.")

        print_section("Done")
        print("Supply-chain graph and queries completed successfully.")

    finally:
        graph.close()


if __name__ == "__main__":
    main()
