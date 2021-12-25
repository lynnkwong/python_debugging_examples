from typing import Optional

import uvicorn
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()


class ResponseEchoed(BaseModel):
    path: str
    query: Optional[str] = None


@app.get("/echo/{path}", response_model=ResponseEchoed)
async def echo(path: str = Path(...), query: Optional[str] = Query(None)):
    # import debugpy
    # debugpy.listen(("0.0.0.0", 5678))
    # debugpy.wait_for_client()
    # debugpy.breakpoint()

    # import rpdb
    # debugger = rpdb.Rpdb(port=4444, addr="0.0.0.0")
    # debugger.set_trace()
    result = ResponseEchoed(path=path, query=query)
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
