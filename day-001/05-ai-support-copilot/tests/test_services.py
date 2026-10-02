from app.models import Ticket
from app.services import build_copilot_result, route

def test_auth_ticket_routes_correctly():
    ticket = Ticket(customer='Acme', subject='Webhook returns 401', message='Authorization token is rejected after rotation.')
    result = build_copilot_result(ticket)
    assert result['category'] == 'Authentication'
    assert result['confidence'] > 0.8
    assert result['retrieved_articles']

def test_unknown_ticket_can_escalate():
    ticket = Ticket(customer='Acme', subject='Unexpected behavior', message='Something is wrong.')
    category, confidence = route(ticket)
    assert category == 'API'
    assert confidence < 0.7
