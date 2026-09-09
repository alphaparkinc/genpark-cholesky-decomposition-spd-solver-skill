"""MCP Server for Cholesky Decomposition Skill."""
import json
import sys
from client import CholeskyDecomposition

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "cholesky_factorize",
                            "description": "Compute Cholesky LL^T decomposition for SPD matrix",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "matrix": {
                                        "type": "array",
                                        "items": {"type": "array", "items": {"type": "number"}}
                                    }
                                },
                                "required": ["matrix"]
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                L = CholeskyDecomposition.factorize(args["matrix"])
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps({"L": L})}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
