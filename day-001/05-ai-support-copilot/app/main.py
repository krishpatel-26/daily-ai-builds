import logging
from fastapi import FastAPI
from .models import Ticket, CopilotResponse
from .services import build_copilot_result
from .config import settings

logging.basicConfig(level=settings.log_level)
logger = logging.getLogger('support-copilot')
app = FastAPI(title='AI Support Copilot', version='1.0.0')

@app.get('/health')
def health() -> dict:
    return {'status': 'ok', 'environment': settings.app_env}

@app.post('/tickets', response_model=CopilotResponse)
def analyze_ticket(ticket: Ticket) -> CopilotResponse:
    logger.info('Analyzing support ticket for customer=%s', ticket.customer)
    return CopilotResponse(**build_copilot_result(ticket))
