import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Server Configuration
HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", "8000"))  # Properly handle Railway's PORT

app = FastAPI(
    title="Strategy AI Basic Backend",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Strategy AI Basic Backend is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT) 