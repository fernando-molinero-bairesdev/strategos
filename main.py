"""
FastAPI application entry point for Strategos.
"""

from fastapi import FastAPI
from data import router as data_router
from diagram import router as diagram_router

app = FastAPI(
    title="Strategos",
    description="Python diagram tool with data management capabilities",
    version="1.0.0"
)

# Include routers from packages
app.include_router(data_router, prefix="/data", tags=["data"])
app.include_router(diagram_router, prefix="/diagram", tags=["diagram"])


@app.get("/")
async def root():
    """Root endpoint returning basic API information."""
    return {
        "message": "Welcome to Strategos API",
        "version": "1.0.0",
        "description": "Python diagram tool with data management capabilities"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)