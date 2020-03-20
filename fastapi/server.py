#doc: https://fastapi.tiangolo.com/

#pip install fastapi
#pip install uvicorn

'''
这个用 Python 开发 API 的新框架具有超高性能，而且可以基于 OpenAPI 标准自动生成交互式文档。默认支持 Swagger UI 与 ReDoc，允许直接从浏览器调用、测试 API，从而提高开发效率。用这个框架开发 API，真的是又快又简单。

该支持库还支持现代 Python 最佳实用功能之一：类型提示。FastAPI 在很多方面都使用了类型提示，其中最酷的一个功能是由 Pydantic 加持的自动数据验证与转换。

FastAPI 基于 Starlette 开发，性能与 NodeJS 和 GO 相当，还自带 WebSocket 与 GraphQL 原生支持。

作者：呆鸟的简书
链接：https://www.jianshu.com/p/d65e913e7f26
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


#start
# uvicorn main:app --reload
