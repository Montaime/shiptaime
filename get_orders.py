import json
import requests

def DataComparer(data, pirateShipData):
    return data["buyer_name"] == pirateShipData["buyer_name"] and data["buyer_email"] == pirateShipData[
        "buyer_email"] and data["ship_to_street"] == pirateShipData["ship_to_street"]


id = 0

GET_ORDERS_URL = "https://bandcamp.com/api/merchorders/3/get_orders"
UPDATE_SHIPPED_URL = "https://bandcamp.com/api/merchorders/2/update_shipped"

PARAMS = {
    "band_id": id,
    "unshipped_only": "true",
    "format": "json"
}

r = requests.get(url = GET_ORDERS_URL, params = PARAMS)

data = json.loads(r.json())

pirateShipData = {"stuff": "stuff"}

paymentIdHolder = []
ship = []

for x in data:
    count = sum(DataComparer(x, pirateShipData) for y in pirateShipData)

    if count > 1:
        if data["payment_id"] not in paymentIdHolder:
            print("Handle this payment manually: " + data["payment_id"])
            paymentIdHolder.append(data["payment_id"])
    elif count == 1:
        shipDict = {
            "id": data["payment_id"],
            "id_type": "p",
            "shipped": True
        }
        ship.append(shipDict)

shipData = {"items": ship}
response = requests.post(url = UPDATE_SHIPPED_URL, data = json.dumps(shipData))