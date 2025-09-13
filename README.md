# Strategos

A FastAPI-based Python diagram tool with comprehensive data management capabilities.

## Features

### Data Package (`/data`)
- **Data Management**: Create, read, update, and delete data items
- **Data Processing**: Transform and process data with various operations
- **Data Export**: Export data in multiple formats (JSON)
- **RESTful API**: Complete CRUD operations for data items

### Diagram Package (`/diagram`)
- **Diagram Creation**: Create flowcharts, UML diagrams, network diagrams, and more
- **Node Management**: Add various types of nodes (rectangle, circle, diamond, etc.)
- **Edge Management**: Connect nodes with customizable edges and labels
- **SVG Rendering**: Generate SVG visualizations of diagrams
- **Templates**: Pre-built diagram templates for common use cases

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### API Documentation

Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI).

### Example Usage

#### Creating a Data Item
```bash
curl -X POST http://localhost:8000/data/items \
  -H "Content-Type: application/json" \
  -d '{"name": "example", "content": {"key": "value"}, "description": "Example data"}'
```

#### Creating a Diagram
```bash
curl -X POST http://localhost:8000/diagram/diagrams \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Flowchart",
    "diagram_type": "flowchart",
    "nodes": [
      {"label": "Start", "node_type": "circle", "x": 100, "y": 50},
      {"label": "End", "node_type": "circle", "x": 100, "y": 150}
    ],
    "edges": [{"source_node": "Start", "target_node": "End"}]
  }'
```

#### Rendering a Diagram as SVG
```bash
curl "http://localhost:8000/diagram/diagrams/1/render?format=svg"
```

## API Endpoints

### Root Endpoints
- `GET /` - Welcome message and API information
- `GET /health` - Health check

### Data Package Endpoints
- `GET /data/` - Package information
- `GET /data/items` - List all data items
- `POST /data/items` - Create new data item
- `GET /data/items/{id}` - Get specific data item
- `PUT /data/items/{id}` - Update data item
- `DELETE /data/items/{id}` - Delete data item
- `POST /data/process` - Process data
- `GET /data/export` - Export data

### Diagram Package Endpoints
- `GET /diagram/` - Package information
- `GET /diagram/diagrams` - List all diagrams
- `POST /diagram/diagrams` - Create new diagram
- `GET /diagram/diagrams/{id}` - Get specific diagram
- `PUT /diagram/diagrams/{id}` - Update diagram
- `DELETE /diagram/diagrams/{id}` - Delete diagram
- `POST /diagram/diagrams/{id}/nodes` - Add node to diagram
- `POST /diagram/diagrams/{id}/edges` - Add edge to diagram
- `GET /diagram/diagrams/{id}/render` - Render diagram
- `GET /diagram/templates` - Get diagram templates

## Project Structure

```
strategos/
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
├── data/               # Data management package
│   ├── __init__.py     # Data API routes
│   ├── models.py       # Data models and schemas
│   └── services.py     # Data business logic
└── diagram/            # Diagram management package
    ├── __init__.py     # Diagram API routes
    ├── models.py       # Diagram models and schemas
    └── services.py     # Diagram business logic
```
