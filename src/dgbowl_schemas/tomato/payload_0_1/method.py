from pydantic import BaseModel


class Method(BaseModel, extra="allow"):
    device: str
    technique: str
