from fastapi import FastAPI

products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]

app = FastAPI()

@app.get('/product')
def search_product(keyword: str | None = None, max_price: float | None = None):
    if max_price is not None and max_price < 0:
        return {"detail": "max_price không được âm"}
    if max_price is None and keyword is None:
        return products
    result = []
    if keyword is not None and max_price is not None:
        result.append(pro for pro in products if keyword.lower() in pro['name'].lower() and pro['price'] <= max_price)
    elif keyword is not None and max_price is None:
        result.append(pro for pro in products if keyword.lower() in pro['name'].lower())
    elif keyword is None and max_price is not None:
        result.append(pro for pro in products if pro['price'] <= max_price)
    return result