from pydantic import BaseModel, Field


class PostSchema(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    body: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mussum Ipsum, cacilds vidis litro abertis.",
                "description": " Si num tem leite então bota uma pinga aí cumpadi! "
                               "Quem num gosta di mim que vai caçá sua turmis!",
                "body": "Mussum Ipsum, cacilds vidis litro abertis. "
                        "Per aumento de cachacis, eu reclamis. "
                        "Aenean aliquam molestie leo, vitae iaculis nisl. "
                        "Interagi no mé, cursus quis, vehicula ac nisi. "
                        "Casamentiss faiz malandris se pirulitá. "
            }
        }
