from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from starlette import status

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(UserNotFoundException)
def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code = 404,
        content = {
            "status": "error",
            "message": f"User {exc.name} Not Found",
        }
    )

@app.get("/user/{name")
def get_user(name: str):
    if name != "Tanya":
        raise UserNotFoundException(name)
    return {
        "name": name
    }

# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code = 404,
#             detail = "User Not Found",
#         )
#     return {
#         "message": "User found",
#         "name": "Tanya",
#         "id": user_id
#     }
#
