# Claude Conversation (Proxy) — Home-Assistant-Integration

Conversation-Agent für Home Assistant, der über den hauseigenen
**`ha-claude-proxy`**-Adapter (NAS, OpenAI-kompatibel) mit **Claude** spricht —
inkl. nativem Tool-Calling, also echter HA-Steuerung über die Assist-LLM-API.

Fork von [michelle-avery/openai-compatible-conversation](https://github.com/michelle-avery/openai-compatible-conversation),
zugeschnitten auf den Adapter: Default-`base_url` zeigt auf den Proxy, API-Key
optional (der Adapter prüft keinen), deutscher Default-Prompt, ohne den
dall-e-Bildservice der Vorlage.

## Voraussetzung

`ha-claude-proxy` läuft erreichbar im LAN. Die Basis-URL im Einrichtungsdialog auf
die Adresse deines Adapters setzen (z. B. `http://homeassistant.local:8080/v1`).

## Installation

**Via HACS (Custom Repository):** HACS → ⋮ → *Custom repositories* → URL dieses
Repos, Kategorie *Integration* → installieren → HA neu starten.

**Manuell:** `custom_components/claude_proxy/` nach `/config/custom_components/`
kopieren, HA neu starten.

## Einrichtung

*Einstellungen → Geräte & Dienste → Integration hinzufügen → „Claude"*

1. **Basis-URL** bestätigen (Default passt), API-Key-Feld leer lassen.
2. Unter *Konfigurieren*: **Instruktionen** (System-Prompt) anpassen,
   **Control Home Assistant** auf *Assist* stellen (Steuerung), Modell/Tokens
   nach Bedarf.
3. *Einstellungen → Sprachassistenten*: Pipeline auf diesen Agenten zeigen lassen.

## Modell

Default `claude-sonnet-4-6` (der Adapter mappt den Namen auf das Claude-Modell).
Frei änderbar in den Optionen.
