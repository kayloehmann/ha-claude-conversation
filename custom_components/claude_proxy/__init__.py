"""The Claude Conversation (Proxy) integration.

Forked from michelle-avery/openai-compatible-conversation, zugeschnitten auf den
hauseigenen ha-claude-proxy-Adapter. Der dall-e Bild-Service der Vorlage entfällt
(Claude/der Adapter unterstützt keine Bildgenerierung).
"""

from __future__ import annotations

import openai

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_API_KEY, Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.httpx_client import get_async_client

from .const import CONF_BASE_URL, LOGGER

PLATFORMS = (Platform.CONVERSATION,)

type ClaudeProxyConfigEntry = ConfigEntry[openai.AsyncClient]


async def async_setup_entry(hass: HomeAssistant, entry: ClaudeProxyConfigEntry) -> bool:
    """Set up Claude Conversation (Proxy) from a config entry."""
    client = openai.AsyncOpenAI(
        api_key=entry.data.get(CONF_API_KEY) or "not-needed",
        http_client=get_async_client(hass),
        base_url=entry.data[CONF_BASE_URL],
    )

    try:
        await hass.async_add_executor_job(
            client.with_options(timeout=10.0).models.list
        )
    except openai.AuthenticationError as err:
        LOGGER.error("Authentifizierung am Adapter fehlgeschlagen: %s", err)
        return False
    except openai.OpenAIError as err:
        raise ConfigEntryNotReady(err) from err

    entry.runtime_data = client

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Claude Conversation (Proxy)."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
