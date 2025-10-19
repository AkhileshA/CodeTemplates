from fastapi import FastAPI
from api.items import router as items_router

app = FastAPI(title="Service 1", version="1.0.0")

# Include API routers
app.include_router(items_router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to Service 1", "status": "running"}

