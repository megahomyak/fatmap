import http from "node:http";

const auth = process.env.AUTH;
if (auth === undefined) {
    throw new Error("provide AUTH");
}

const server = http.createServer((req, res) => {

    res.writeHead(200);
    res.end();
});

server.listen(8000);
