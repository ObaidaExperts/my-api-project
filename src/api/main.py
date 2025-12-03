"""Main API application."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

API_VERSION = "0.2.0"

app = FastAPI(
    title="My API Project",
    description="Python API with conventional commits",
    version=API_VERSION,
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "My API Project",
        "version": API_VERSION,
        "message": "Welcome to the API",
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return JSONResponse(
        status_code=200,
        content={"status": "healthy", "version": API_VERSION},
    )


@app.get("/version")
async def get_version():
    """Get API version."""
    return {"version": API_VERSION}
