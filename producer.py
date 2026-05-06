from fastapi import APIRouter
from app.services.state_reconstruction import reconstruct_entity_state
from app.services.temporal_query import temporal_neighbors

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "healthy"}

@router.get("/entity/{entity_id}/state")
async def get_entity_state(entity_id: str, timestamp: str):

    state = reconstruct_entity_state(entity_id, timestamp)

    return {
        "entity_id": entity_id,
        "timestamp": timestamp,
        "state": state
    }

@router.get("/entity/{entity_id}/neighbors")
async def get_neighbors(entity_id: str, hops: int = 2):

    neighbors = temporal_neighbors(entity_id, hops)

    return {
        "entity_id": entity_id,
        "neighbors": neighbors
    }