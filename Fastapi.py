from fastapi import FastAPI,Path,Query,HTTPException,status
import uvicorn
from typing import Optional
from pydantic import BaseModel
#intilise the FastAPI
app = FastAPI()

# #create an endpoint with "/"(root) using get method
# @app.get("/")
# def home():
#     return {"Data":"Test"}
#
# @app.get("/about")
# def about():
#     return {"Data":"About"}

#Request body ---> POST Method
class Item(BaseModel):
    name:str
    price:int
    brand:Optional[str] = None

#Request body ----> PUT Method
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None
    brand: Optional[str] = None


#PATH/ENDPOINT PARAMETER:
inventory = {
    1: {
        "name":"Milk",
        "price":25,
        "brand":"Regular"
    },
    2: {
        "name": "Orange",
        "price": 100,
        "brand": "Chinese"
    }
}
# @app.get("/get-item/{item_id}/{name}")
# def get_item(item_id:int,name:str):  #--->type hint
#     return inventory[item_id]
@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(description="The ID of the item you like to view")):  #--->type hint
    return inventory[item_id]


#Query parameter
@app.get("/get-by-name")
def get_item(*,name: Optional[str] = None,test:int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
                   return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

#Path and Query parameter
@app.get("/get-by-name/{item_id}")
def get_item(*,item_id: int, name: Optional[str] = None,test:int):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
                   return inventory[item_id]
    return {"Data":"Not Found"}

#Request Body - sending bunch of information
@app.post("/create-item/{item_id}")
def create_item(item_id:int,item :Item):
    if item_id in inventory:
        raise HTTPException(status_code=400,detail="Item ID already exists")
    inventory[item_id] = item #{"name":item.name,"brand":item.brand,"price":item.price}
    return inventory[item_id]

#Request Body - Update an Item
@app.put("/update-item/{item_id}")
def update_item(item_id:int ,item:UpdateItem):
    if item_id not in inventory:
        return {"Error":"Item ID does not exists"}
    if item.name != None:
        inventory[item_id]["name"] = item.name
    if item.price != None:
        inventory[item_id]["price"] = item.price
    if item.brand != None:
        inventory[item_id]["brand"] = item.brand
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id:int = Query(description="The ID of the item to delete")):
    if item_id not in inventory:
        return {"Error":"ID does not exist"}
    del inventory[item_id]
    return {"Sucess":"Item deleted"}

if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=8080)

