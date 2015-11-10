import logging
import random

from baseplate import make_metrics_client, config, diagnostics
from baseplate.integration.thrift import BaseplateProcessorEventHandler

from .toy_thrift import ToyService


logger = logging.getLogger(__name__)


class Handler(ToyService.ContextIface):
    def __init__(self, real_random=False):
        self.real_random = real_random

    def is_healthy(self, context):
        return True

    def get_random(self, context):
        if self.real_random:
            return random.randint(0, 100)
        else:
            return 5

    def multiply(self, context, one, two):
        return one * two


def make_processor(app_config):
    cfg = config.parse_config(app_config, {
        "real_random": config.Boolean,
    })

    metrics_client = make_metrics_client(app_config)

    agent = diagnostics.DiagnosticsAgent()
    agent.register(diagnostics.LoggingDiagnosticsObserver())
    agent.register(diagnostics.MetricsDiagnosticsObserver(metrics_client))

    handler = Handler(real_random=cfg.real_random)
    processor = ToyService.ContextProcessor(handler)
    event_handler = BaseplateProcessorEventHandler(logger, agent)
    processor.setEventHandler(event_handler)

    return processor
