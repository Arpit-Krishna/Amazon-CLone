from fastapi import Body,APIRouter,HTTPException,status
from fastapi.middleware import cors

# from pydantic_models import TodoRequest,TodoResponse
router = APIRouter(tags=["products"])
amazon = [
    
      {
        "imageUrl":"https://m.media-amazon.com/images/I/31YE9kV-D+L._SY300_SX300_.jpg",
        "title":"Honeywell High-Speed Type C to RJ45 Gigabit Ethernet Adapter, 10/100/1000 MBPS",
        "price":"1650"
      },
      {"imageUrl":"https://m.media-amazon.com/images/I/510ZopFr3FL._SY741_.jpg",
        "title":"CableCreation USB to Ethernet Adapter, USB 3.0 to 10/100/1000 Gigabit ",
        "price":"1225"
      },
      {
        "imageUrl":"https://m.media-amazon.com/images/I/31YE9kV-D+L._SY300_SX300_.jpg",
        "title":"Honeywell High-Speed Type C to RJ45 Gigabit Ethernet Adapter, 10/100/1000 MBPS",
        "price":"1650"
      }
]


# create product
@router.post('/api/v1/product')
async def createProduct(Product: dict = Body(...)):
    amazon.append(Product)
    return Product


# get all products
@router.get('/api/v1/products')
def getAllProduct():
    return amazon

# get a product by title
@router.get('/api/v1/products/{title}')
def getProductByTitle(title: str):
    response = None
    print("title",title)
    for product in amazon:
        print(product)
        if product['title'] == title:
            response = {"status": "200", "message":"todo found","data":product}
            break
    if response:
        return response
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="product not found")
# update a product by title

# delete a product by title
@router.delete('/api/v1/products/{title}')
def getProductByTitle(title: str):
    response = {"status": 404, "message":"product not found to delete","data":{}}
    for prod_idx,product in enumerate(amazon):
        if product['title'] == title:
            amazon.pop(prod_idx)
            response = {"status": 200, "message":"todo deleted","data":product}
            break
    return response

@router.put('/api/v1/products/{title}')
def updateProductByPut(title:str,Product: dict = Body(...)):
    response = None
    for product in range(len(amazon)):
        if amazon[product]['title'] == title:
            amazon[product]=Product
            response = {"status": "200", "message":"todo found","data":product}
            break
    if response:
        return response
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail="product not found")
    