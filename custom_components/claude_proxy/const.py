"""Constants for the Claude Proxy Conversation integration."""

import logging

DOMAIN = "claude_proxy"
LOGGER = logging.getLogger(__package__)

CONF_RECOMMENDED = "recommended"
CONF_PROMPT = "prompt"
CONF_CHAT_MODEL = "chat_model"
CONF_MAX_TOKENS = "max_tokens"
CONF_TEMPERATURE = "temperature"
CONF_TOP_P = "top_p"
CONF_BASE_URL = "base_url"

# Defaults sind auf den hauseigenen ha-claude-proxy-Adapter (NAS, VLAN 111)
# zugeschnitten. Der Adapter spricht OpenAI /v1 und proxyt zu Claude.
RECOMMENDED_CHAT_MODEL = "claude-sonnet-4-6"
RECOMMENDED_MAX_TOKENS = 1024
RECOMMENDED_TEMPERATURE = 1.0
RECOMMENDED_TOP_P = 1.0
RECOMMENDED_BASE_URL = "http://10.111.0.104:8080/v1"

# Persona-Default (in der UI frei überschreibbar). Die HA-LLM-API hängt die
# Tool-/Entity-Instruktionen automatisch an.
DEFAULT_PROMPT = (
    "Du bist der Sprachassistent in Kays Zuhause. Antworte kurz, natürlich und "
    "auf Deutsch — sprich gesprochene Sätze, keine Listen oder Markdown. Wenn du "
    "ein Gerät steuern sollst, tu es direkt und bestätige knapp. Bei Unklarheit "
    "(z. B. mehrdeutiger Raum) frag kurz nach."
)
