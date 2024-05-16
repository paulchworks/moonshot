from typing import Annotated, Optional

from pydantic import Field

from moonshot.src.connectors_endpoints.connector_endpoint_arguments import (
    ConnectorEndpointArguments as ConnectorEndpointPydanticModel,
)


class EndpointCreateDTO(ConnectorEndpointPydanticModel):
    id: Optional[str] = None


class EndpointUpdateDTO(ConnectorEndpointPydanticModel):
    id: Optional[str] = None
    name: Optional[str] = None
    connector_type: Optional[str] = None
    uri: Optional[str] = None
    token: Optional[str] = None
    max_calls_per_second: Optional[int] = None
    max_concurrency: Optional[int] = None
    params: Optional[dict] = None
    created_date: Optional[str] = None
