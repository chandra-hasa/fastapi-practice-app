from fastapi import FastAPI
import models
import database
from router import authentication, blog, user

app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


models.Base.metadata.create_all(database.engine)
