import json
from mock_tools import mock_search


def decide_topic(persona):
    if "crypto" in persona.lower():
        return "crypto"
    elif "ai" in persona.lower():
        return "AI"
    else:
        return "market"


def generate_post(bot_id, persona):
    topic = decide_topic(persona)
    context = mock_search(topic)

    # simple generation logic (can replace with LLM later)
    post = f"As a {bot_id}, I think {context}. This clearly shows future direction."

    result = {
        "bot_id": bot_id,
        "topic": topic,
        "post_content": post[:280],
    }

    return json.dumps(result)
