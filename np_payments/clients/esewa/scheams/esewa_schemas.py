from pydantic import BaseModel
from typing import Optional


class ConstructEsewaRequest(BaseModel):
    amount: float
    success_url: str
    failure_url: str
    product_code: str
    product_service_charge: float = 0.0
    product_delivery_charge: float = 0.0
    tax_amount: float = 0.0
    total_amount: float
    transaction_uuid: Optional[str] = None


class EsewaRequestPayload(BaseModel):
    amount: float
    success_url: str
    failure_url: str
    product_code: str
    product_service_charge: float = 0.0
    product_delivery_charge: float = 0.0
    tax_amount: float = 0.0
    total_amount: float
    transaction_uuid: str
    signature: str
    signed_field_names: str
