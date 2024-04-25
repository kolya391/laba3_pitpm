#Query-параметры и валидация строк
#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: str | None = None):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Расширенная валидация
#Импорт Query и Annotated
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()
s

#@app.get("/items/")
#async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Добавим Query в Annotated для query-параметра q
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Альтернативный (устаревший) способ задать Query как значение по умолчанию
#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: str | None = Query(default=None, max_length=50)):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Больше валидации. Вы также можете добавить параметр min_length
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(
#    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
#):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Регулярные выражения
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(
#    q: Annotated[
#        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
#    ] = None,
#):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Значения по умолчанию
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Обязательный параметр
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: Annotated[str, Query(min_length=3)]):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Обязательный параметр с Ellipsis
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Обязательный параметр с None
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: Annotated[str | None, Query(min_length=3)] = ...):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Использование Pydantic's Required вместо Ellipsis
#from typing import Annotated

#from fastapi import FastAPI, Query
#from pydantic import Required

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: Annotated[str, Query(min_length=3)] = Required):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Множество значений для query-параметра
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: Annotated[list[str] | None, Query()] = None):
#    query_items = {"q": q}
#    return query_items
#Query-параметр со множеством значений по умолчанию
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
#    query_items = {"q": q}
#    return query_items

#Если вы перейдёте по ссылке:


#http://localhost:8000/items/
#значение по умолчанию для q будет: ["foo", "bar"] и ответом для вас будет:


#{
#  "q": [
#    "foo",
#    "bar"
#  ]
#}
#Использование list
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: Annotated[list, Query()] = []):
#    query_items = {"q": q}
#    return query_items

#Больше метаданных
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(
#    q: Annotated[str | None, Query(title="Query string", min_length=3)] = None,
#):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Псевдонимы параметров
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results

#Устаревшие параметры
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(
#    q: Annotated[
#        str | None,
#        Query(
#            alias="item-query",
#            title="Query string",
#            description="Query string for the items to search in the database that have a good match",
#            min_length=3,
#            max_length=50,
#            deprecated=True,
#        ),
#    ] = None,
#):
#    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#    if q:
#        results.update({"q": q})
#    return results
#Исключить из OpenAPI
#from typing import Annotated

#from fastapi import FastAPI, Query

#app = FastAPI()


#@app.get("/items/")
#async def read_items(
#    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
#):
#    if hidden_query:
#        return {"hidden_query": hidden_query}
#    else:
#        return {"hidden_query": "Not found"}