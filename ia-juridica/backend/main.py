from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.graph.router import Router
from backend.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Initialize router
router_agent = Router()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = await router_agent.route(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
