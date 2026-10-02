import re
from .config import settings
from .models import Ticket

KNOWLEDGE_BASE = [
    ('Authentication', 'Webhook requests return 401 when the signing secret or authorization token is invalid. Rotate the credential and update the integration configuration.'),
    ('Webhooks', 'Webhook delivery failures can be diagnosed by checking endpoint status code, signature verification, retry logs, and recent credential changes.'),
    ('Billing', 'Billing questions should be checked against the customer plan, invoice status, and recent subscription changes.'),
    ('API', 'API errors should be triaged using the endpoint, status code, request ID, and recent deployment or configuration changes.'),
]

def _tokens(text: str) -> set[str]:
    return set(re.findall(r'[a-z0-9]+', text.lower()))

def route(ticket: Ticket) -> tuple[str, float]:
    text = f'{ticket.subject} {ticket.message}'.lower()
    if any(x in text for x in ('401', '403', 'login', 'password', 'token', 'auth')):
        return 'Authentication', 0.92
    if any(x in text for x in ('webhook', 'callback', 'delivery')):
        return 'Webhooks', 0.89
    if any(x in text for x in ('invoice', 'payment', 'billing', 'charge')):
        return 'Billing', 0.90
    return 'API', 0.62

def retrieve(ticket: Ticket) -> list[str]:
    query = _tokens(f'{ticket.subject} {ticket.message}')
    ranked = sorted(((len(query & _tokens(content)), title, content) for title, content in KNOWLEDGE_BASE), reverse=True)
    return [f'{title}: {content}' for score, title, content in ranked[:settings.top_k] if score]

def generate_response(ticket: Ticket, category: str, articles: list[str]) -> str:
    context = ' '.join(articles)
    return f'Thanks for contacting support regarding {ticket.subject}. We classified this as {category}. Based on our knowledge base: {context} Please share the request ID and timestamp if the issue persists.'

def build_copilot_result(ticket: Ticket) -> dict:
    category, confidence = route(ticket)
    articles = retrieve(ticket)
    escalation = confidence < 0.7 or 'security' in ticket.message.lower()
    reason = 'Low routing confidence' if confidence < 0.7 else ('Potential security issue' if escalation else None)
    return {'category': category, 'confidence': confidence, 'retrieved_articles': articles, 'suggested_response': generate_response(ticket, category, articles), 'should_escalate': escalation, 'escalation_reason': reason}
