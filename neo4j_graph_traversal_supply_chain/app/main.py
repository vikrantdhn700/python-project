from app.graph_manager import SupplyChainGraph


def main():
    graph = SupplyChainGraph()
    try:
        print("Creating constraints...")
        graph.create_constraints()
        print("Creating supply-chain sample graph...")
        graph.create_sample_graph()
        print("\nRunning traversal queries...")
        graph.execute_traversal_queries()
        print("\nDone.")
    finally:
        graph.close()


if __name__ == "__main__":
    main()
