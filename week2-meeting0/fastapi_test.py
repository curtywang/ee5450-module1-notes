import uvicorn
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


# HTTP (HyperText Transport Protocol) on top of TCP/IP
# HTTP GET
# HTTP POST


@app.get("/")
def read_root():
    return {"Greetings": "Hello EE 5450",
            "Messages": ["some msg", "some other msg"]}


# the ? operator below allows you to specify optional key-value pairs in the URL as parameters
# http://localhost:8000/items/5?some_key=Python
# http://localhost:8000/items/5?some_key=Java --> ?
@app.post("/items/{item_id}")
def post_item(item_id: int, some_key: Optional[str] = None):
    """
    Posts an item with item_id and some_key informaiton

    :param item_id:
    :param some_key:
    :return:
    """
    if some_key == "Python":
        return {"GOD MODE": True}
    return {"item_id": item_id, "some_key": some_key}


if __name__ == '__main__':
    uvicorn.run('fastapi_test:app', port=8000, log_level='info', reload=True)
