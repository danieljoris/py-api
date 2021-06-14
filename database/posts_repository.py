from bson import ObjectId

from database.database import post_collection, post_helper

# Retrieve all posts
async def retrieve_posts():
    posts = []
    async for post in post_collection.find():
        posts.append(post_helper(post))
    return posts;


# Add new post
async def create_post(post_data: dict) -> dict:
    post = await post_collection.insert_one(post_data)
    new_post = await post_collection.find_one({"_id": post.inserted_id})
    return post_helper(new_post)


# Retrieve specific post
async def retrieve_post(id: str) -> dict:
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post:
        return post_helper(post)

async def update_post(id: str, data: dict):
    if len(data) < 1:
        return False
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post:
        updated_post = await post_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_post:
            return True
        return False

async def delete_post(id: str) -> bool:
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post:
        await post_collection.delete_one({"_id": ObjectId(id)})
        return True;
    return False
