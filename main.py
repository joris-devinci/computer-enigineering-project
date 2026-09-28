import numpy
from fastapi import FastAPI

app = FastAPI()

@app.get("/collection")
def get_inventory():
    pass

@app.post("/user/login")
def login():
    pass

@app.post("/user/register")
def register():
    pass

@app.post("/cart")
def add_to_cart():
    pass

@app.get("/cart")
def get_cart():
    pass

@app.post("/order")
def check_out():
    pass

@app.get("/order")
def get_orders():
    pass

def main():
    print("Hello from computer-enigineering-project!")


if __name__ == "__main__":
    main()
