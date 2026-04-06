from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, status, Form
from app.dependencies import SessionDep
from . import api_router
from app.services.user_service import UserService
from app.repositories.user import UserRepository
from app.utilities.flash import flash
from app.schemas import UserResponse


# API endpoint for listing users
@api_router.get("/users", response_model=list[UserResponse])
async def list_users(request: Request, db: SessionDep):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    return user_service.get_all_users()

@router.get("/todos")
def todos_page(request: Request):
    todos = [
        {"id": 1, "title": "Study", "completed": False},
        {"id": 2, "title": "Sleep", "completed": True},
    ]

    return templates.TemplateResponse(
        "todos.html",
        {"request": request, "todos": todos}
    )