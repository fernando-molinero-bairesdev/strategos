#!/usr/bin/env python3
"""
Example script demonstrating Strategos API usage.
"""

import json
import requests
import time

BASE_URL = "http://localhost:8000"

def test_api():
    """Test the Strategos API functionality."""
    print("🚀 Testing Strategos API...")
    
    # Test root endpoint
    print("\n1. Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test data package
    print("\n2. Testing data package...")
    
    # Create a data item
    data_item = {
        "name": "sample_data",
        "content": {"numbers": [1, 2, 3, 4, 5], "text": "Hello World"},
        "description": "Sample data for testing",
        "tags": ["test", "example"]
    }
    
    response = requests.post(f"{BASE_URL}/data/items", json=data_item)
    print(f"Created data item: {response.status_code}")
    created_item = response.json()
    print(f"Item ID: {created_item['id']}")
    
    # Get all data items
    response = requests.get(f"{BASE_URL}/data/items")
    print(f"Retrieved data items: {response.status_code}")
    print(f"Total items: {len(response.json())}")
    
    # Test diagram package
    print("\n3. Testing diagram package...")
    
    # Create a flowchart diagram
    diagram_data = {
        "title": "Sample Process Flow",
        "diagram_type": "flowchart",
        "description": "A simple process flow diagram",
        "nodes": [
            {"label": "Start", "node_type": "circle", "x": 50, "y": 50, "color": "#90EE90"},
            {"label": "Input Data", "node_type": "rectangle", "x": 50, "y": 150, "color": "#87CEEB"},
            {"label": "Process", "node_type": "rectangle", "x": 50, "y": 250, "color": "#DDA0DD"},
            {"label": "Decision", "node_type": "diamond", "x": 50, "y": 350, "color": "#F0E68C"},
            {"label": "Output", "node_type": "rectangle", "x": 200, "y": 350, "color": "#FFB6C1"},
            {"label": "End", "node_type": "circle", "x": 50, "y": 450, "color": "#FFA07A"}
        ],
        "edges": [
            {"source_node": "Start", "target_node": "Input Data"},
            {"source_node": "Input Data", "target_node": "Process"},
            {"source_node": "Process", "target_node": "Decision"},
            {"source_node": "Decision", "target_node": "Output", "label": "Yes"},
            {"source_node": "Decision", "target_node": "End", "label": "No"},
            {"source_node": "Output", "target_node": "End"}
        ]
    }
    
    response = requests.post(f"{BASE_URL}/diagram/diagrams", json=diagram_data)
    print(f"Created diagram: {response.status_code}")
    created_diagram = response.json()
    diagram_id = created_diagram['id']
    print(f"Diagram ID: {diagram_id}")
    print(f"Nodes: {created_diagram['node_count']}, Edges: {created_diagram['edge_count']}")
    
    # Render diagram as SVG
    response = requests.get(f"{BASE_URL}/diagram/diagrams/{diagram_id}/render", params={"format": "svg"})
    print(f"Rendered diagram: {response.status_code}")
    svg_data = response.json()
    
    # Save SVG to file
    with open("/tmp/sample_diagram.svg", "w") as f:
        f.write(svg_data['content'])
    print("SVG diagram saved to /tmp/sample_diagram.svg")
    
    # Test data processing
    print("\n4. Testing data processing...")
    
    process_request = {
        "operation": "count",
        "content": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    
    response = requests.post(f"{BASE_URL}/data/process", json=process_request)
    print(f"Processed data: {response.status_code}")
    print(f"Result: {response.json()}")
    
    # Get diagram templates
    print("\n5. Testing diagram templates...")
    response = requests.get(f"{BASE_URL}/diagram/templates")
    print(f"Retrieved templates: {response.status_code}")
    templates = response.json()['templates']
    print(f"Available templates: {len(templates)}")
    for template in templates:
        print(f"  - {template['name']}: {template['description']}")
    
    print("\n✅ API testing completed successfully!")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the API server.")
        print("Make sure the server is running with: python main.py")
    except Exception as e:
        print(f"❌ Error during testing: {e}")