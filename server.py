STATUS_CODE_OK = 200
STATUS_CODE_UNAUTHORIZED = 500

class Server:
    def send_response(self, status_code: int, response: "json Python object"):
        self.send_response(status_code)
        self.end_headers()
        self.wfile.write(json_str.encode())

#####################
#####################
#####################
#####################
#####################










UnsignedInt = int
Value = UnsignedInt
DEFAULT_VALUE = 0
Key = UnsignedInt


class Layer:
    def __init__(self, key: Key, value: Value):
        self.key = key
        self.value = value


class LayerId:
    def __init__(self, value: UnsignedInt):
        self.value = value

    def next(self):
        self.value += 1


class NotFound: pass


class HistoryInterface:
    def add_layer(self, key: Key, value: Value) -> None:
        raise NotImplementedError()

    def get_last_value_or_default(self, key: Key) -> Value:
        raise NotImplementedError()

    def get_layer(self, id: LayerId) -> Layer | NotFound:
        raise NotImplementedError()


class FatMap:
    def __init__(self, history: HistoryInterface):
        self.history = history

    def add_layer(self, layer: Layer) -> "old Value":
        old_value = self.get_value(layer.key)
        history.add_layer(layer)
        return old_value

    def get_value(self, key: Key) -> Value:
        return self.history.get_last_value_or_default(key)

    def get_layer(self, id: LayerId) -> Layer | NotFound:
        return self.history.get_layer(id)






































