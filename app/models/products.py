from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from bson import ObjectId

class Products(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    name: str
    price: float
    description: Optional[str] = None
    stock: int


    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )

class ProductDBModel(Products):
    def model_dump(self, *, mode = "python", include = None, excluse = None, context = None, 
                   exclude_unset = False, exclude_defaults = False, exclude_none = False):
        data = super().model_dump(mode=mode, include=include, excluse=excluse, context=context, exclude_unset=exclude_unset, exclude_defaults=exclude_defaults, exclude_none=exclude_none)
        if self.id:
            data["_id"] = str(self.id)
        return data