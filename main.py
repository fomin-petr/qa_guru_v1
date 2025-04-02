from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str


class ResponseModel(BaseModel):
    data: User
    support: Support


@app.get("/api/users/{user_id}", response_model=ResponseModel)
def get_user(user_id: int):
    # Пример данных, которые можно было бы получить из базы данных или другого источника
    users = {
        2: {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        }
    }

    support_data = {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }

    user = users.get(user_id)
    if not user:
        # todo improve exception
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "data": user,
        "support": support_data,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
