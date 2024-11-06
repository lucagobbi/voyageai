from typing import Type, List

from cat.mad_hatter.decorators import hook
from cat.factory.embedder import EmbedderSettings
from langchain_voyageai import VoyageAIEmbeddings
from pydantic import ConfigDict


class EmbedderVoyageAIConfig(EmbedderSettings):
    """Configuration for Voyage AI Embedder.

    This class contains the configuration for the Expedition AI Embedder.
    """

    voyage_api_key: str
    model: str = "voyage-3"
    _pyclass: Type = VoyageAIEmbeddings

    model_config = ConfigDict(
        json_schema_extra={
            "humanReadableName": "Voyage AI Embedder",
            "description": "Configuration for Voyage AI Embedder",
            "link": "https://docs.voyageai.com/docs/introduction"
        }
    )

@hook
def factory_allowed_embedders(allowed, cat) -> List:
    allowed.append(EmbedderVoyageAIConfig)
    return allowed
