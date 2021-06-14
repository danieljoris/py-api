import motor.motor_asyncio

MONGO_DETAILS = "mongodb://daniel:bacate%40%401@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.posts

post_collection = database.get_collection("posts_collection")


def post_helper(post) -> dict:
    return {
        "id": str(post["_id"]),
        "title": post["title"],
        "description": post["description"],
        "body": post["body"],
    }


