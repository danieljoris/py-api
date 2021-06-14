from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from api.response_util import ResponseModel, ErrorResponseModel
from database.posts_repository import create_post, retrieve_post, retrieve_posts, update_post
from models.post import PostSchema

PREFIX = "/posts"

router = APIRouter(prefix=PREFIX)


@router.post("/")
async def add_post(post: PostSchema = Body(...)):
    post = jsonable_encoder(post)
    new_post = await create_post(post)
    return ResponseModel(new_post, "Post added successfully.")


@router.get("/{id}")
async def get_post(id: str):
    post = await retrieve_post(id)
    if post:
        return ResponseModel(post, "Post retrieved successfully.")
    return ErrorResponseModel("An error occurred", 404, "Could not create a post.")


@router.get("/")
async def get_all_posts():
    posts = await retrieve_posts()
    if posts:
        return ResponseModel(posts, "Posts retrieved successfully.")
    return ResponseModel(posts, "Empty list.")


@router.put("/{id}")
async def update_post_data(id: str):
    request = {}
    updated_post = await update_post(id, request)
    if updated_post:
        return ResponseModel(
            "Post with ID: {} is updated".format(id),
            "Post is updated",
        )
    return ErrorResponseModel(
        "An error occurred.",
        404,
        "There was an error updating the post data."
    )
