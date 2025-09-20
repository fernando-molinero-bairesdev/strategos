from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from diagrams.router import router as diagrams_router

# Create FastAPI app
app = FastAPI(title="Strategos API")

# Important: Add CORS middleware BEFORE including routers
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_methods,
    allow_headers=settings.cors_headers,
    # Add these parameters to help with preflight requests
    max_age=600,  # Cache preflight requests for 10 minutes
    expose_headers=["*"],  # Expose all headers to the browser
)

# Include routers
app.include_router(diagrams_router)

# For running the application with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
