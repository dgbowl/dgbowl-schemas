from pydantic import BaseModel


class Sample(BaseModel, extra="allow"):
    name: str
