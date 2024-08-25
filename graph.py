import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def load_transactions_from_excel(file_path):
    """Load transactions from an Excel file."""
    data = pd.read_excel(file_path, header=1)  # Adjust header if necessary
    data.columns = data.columns.str.strip()  # Clean column names
    return data

def build_graph(transactions):
    """Build a transaction graph from the fetched transactions."""
    graph = nx.DiGraph()
    
    for _, tx in transactions.iterrows():
        from_address = tx['from_address']
        to_address = tx['to_address']
        
        # Add edges to the graph
        graph.add_edge(from_address, to_address)
    
    return graph

def visualize_graph(graph):
    """Visualize the transaction graph."""
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
    plt.title("Transaction Graph")
    plt.show()

# Main execution
if __name__ == "__main__":
    file_path = 'eth.xlsx'  # Replace with your actual file path
    transactions = load_transactions_from_excel(file_path)
    
    if not transactions.empty:
        graph = build_graph(transactions)
        visualize_graph(graph)
    else:
        print("No transactions found in the dataset.")
