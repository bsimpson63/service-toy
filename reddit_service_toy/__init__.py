import logging

from baseplate import make_metrics_client, config, diagnostics
from baseplate.integration.thrift import BaseplateProcessorEventHandler

from .toy_thrift import ToyService


logger = logging.getLogger(__name__)


class Handler(ToyService.ContextIface):
    def __init__(self):
        pass

    def is_healthy(self, context):
        # TODO: check that your service has everything it needs to to function
        return True

    # TODO: implement your service here!


def make_processor(app_config):
    cfg = config.parse_config(app_config, {
        # TODO: add your config spec here
    })

    metrics_client = make_metrics_client(app_config)

    agent = diagnostics.DiagnosticsAgent()
    agent.register(diagnostics.LoggingDiagnosticsObserver())
    agent.register(diagnostics.MetricsDiagnosticsObserver(metrics_client))

    handler = Handler()
    processor = ToyService.ContextProcessor(handler)
    event_handler = BaseplateProcessorEventHandler(logger, agent)
    processor.setEventHandler(event_handler)

    return processor
