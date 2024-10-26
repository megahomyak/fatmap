import { Database } from "bun:sqlite";

const auth = Bun.env.AUTH;
if (auth === undefined) {
    throw new Error("provide AUTH");
}

const history = new Database("history.db");

function base

Bun.serve({
    port: 8000,
    hostname: "127.0.0.1",
    async fetch(req) {
        if (req.method == "POST") {
            const text = await req.text();
            const list = text.split(" ");
            if (list[0] === auth) {
                const response = {
                    "/get_value": () => {
                        const key = list[1];
                    },
                    "/get_layer": () => {
                        const key = list[1];
                    },
                    "/add_layer": () => {
                        const key = list[1];
                        const value = list[2];
                    },
                }[req.url]();
                if (response !== undefined) {
                    return new Response(response);
                }
            }
        }
        return new Response("no");
    },
});
