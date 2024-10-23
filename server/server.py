import os
import fastapi
import json

LAYERS_DIR_NAME = "layers"

api_key = os.environ["API_KEY"]

try: os.mkdir(LAYERS_DIR_NAME)
except: pass

def add_layer(contents):
    try:
        with open("last_layer_number") as f:
            last_layer_number = f.read()
    except FileNotFoundError:
        last_layer_number = "1"
    else:
        last_layer_number = str(int(last_layer_number) + 1)
    with open(os.path.join(LAYERS_DIR_NAME, last_layer_number), "w") as f:
        f.write(json.dumps(contents))
    with open("last_layer_number", "w") as f:
        f.write(last_layer_number)
    return last_layer_number

fastapi_app = fastapi.FastAPI()
def handle(url):
    def wrapper(function):
        @fastapi_app.post(url, response_class=fastapi.responses.PlainTextResponse)
        async def receiver(request: fastapi.Request):
            request = await request.json()
            if request["auth"] == api_key:
                return await function(request)
            raise Exception("Bad credentials")
    return wrapper

@handle("/get_layer")
async def get_layer(request):
    layer_number = request["layer_number"]
    try:
        with open(os.path.join(LAYERS_DIR_NAME, layer_number)) as f:
            layer = f.read()
    except FileNotFoundError:
        return "null"
    return layer

def _get_value(key):
    try:
        with open("last_layer_number") as f:
            last_layer_number = f.read()
    except FileNotFoundError:
        return None
    last_layer_number = int(last_layer_number)
    while last_layer_number > 0:
        with open(os.path.join(LAYERS_DIR_NAME, str(last_layer_number))) as f:
            layer = json.load(f)
        if layer["key"] == key:
            return layer["value"]
        last_layer_number -= 1
    return None

@handle("/get_value")
async def get_value(request):
    return json.dumps(_get_value(request["key"]))

@handle("/modify")
async def modify(request):
    last_layer_number = add_layer(request)
    return json.dumps({
        "layer_number": last_layer_number,
        "old_value": _get_value(request["key"]),
    })
