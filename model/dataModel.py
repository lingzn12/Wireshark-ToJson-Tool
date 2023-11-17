from typing import List, Optional
from pydantic import BaseModel, IPvAnyAddress
from pydantic.types import PositiveInt, ConstrainedFloat, NonNegativeInt


class Peer(BaseModel):
    peer: NonNegativeInt
    host: IPvAnyAddress
    port: Optional[str]


class Packet(BaseModel):
    packet: PositiveInt
    peer: NonNegativeInt
    index: NonNegativeInt
    timestamp: ConstrainedFloat(ge=0.0)
    data: bytes


class YAMLData(BaseModel):
    peers: List[Peer]
    packets: List[Packet]
