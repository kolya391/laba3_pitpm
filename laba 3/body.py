#Тело запроса

#Комманда для запуска:uvicorn body:app --reload

#Импортирование BaseModel из Pydantic -----------

#from typing import Union

#from fastapi import FastAPI
#from pydantic import BaseModel


#class Item(BaseModel):
    #name: str
    #description: Union[str, None] = None
    #price: float
    #tax: Union[float, None] = None


#app = FastAPI()


#@app.post("/items/")
#async def create_item(item: Item):
    #return item

#Создание вашей собственной модели----------

#from typing import Union

#from fastapi import FastAPI
#from pydantic import BaseModel


#class Item(BaseModel):
    #name: str
    #description: Union[str, None] = None
    #price: float
    #tax: Union[float, None] = None


#app = FastAPI()


#@app.post("/items/")
#async def create_item(item: Item):
    #return item

#Объявление как параметра функции-----------

#from typing import Union

#from fastapi import FastAPI
#from pydantic import BaseModel


#class Item(BaseModel):
    #name: str
    #description: Union[str, None] = None
    #price: float
    #tax: Union[float, None] = None


#app = FastAPI()


#@app.post("/items/")
#async def create_item(item: Item):
    #return item

#Использование модели ----------

#from typing import Union

#from fastapi import FastAPI
#from pydantic import BaseModel


#class Item(BaseModel):
    #name: str
    #description: Union[str, None] = None
    #price: float
    #tax: Union[float, None] = None


#app = FastAPI()


#@app.post("/items/")
#async def create_item(item: Item):
    #item_dict = item.dict()
    #if item.tax:
        #price_with_tax = item.price + item.tax
        #item_dict.update({"price_with_tax": price_with_tax})
    #return item_dict

#Тело запроса + параметры пути -----------

#from typing import Union

#from fastapi import FastAPI
#from pydantic import BaseModel


#class Item(BaseModel):
    #name: str
    #description: Union[str, None] = None
    #price: float
    #tax: Union[float, None] = None


#app = FastAPI()


#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
    #return {"item_id": item_id, **item.dict()}

#Тело запроса + параметры пути + параметры запроса---------

#from typing import Union

#from fastapi import FastAPI
#from pydantic import BaseModel


#class Item(BaseModel):
    #name: str
    #description: Union[str, None] = None
    #price: float
    #tax: Union[float, None] = None


#app = FastAPI()


#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    #result = {"item_id": item_id, **item.dict()}
    #if q:
        #result.update({"q": q})
    #return result

