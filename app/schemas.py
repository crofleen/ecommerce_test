from pydantic import BaseModel


class CreateProduct(BaseModel):
    name: str
    description: str | None
    price: int
    image_url: str | None
    stock: int
    category: int


class CreateCategory(BaseModel):
    name: str
    parent_id: int | None