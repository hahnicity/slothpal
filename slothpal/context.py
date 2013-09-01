"""
slothpal.context
~~~~~~~~~~~~~~~~
"""
from peak.util.proxies import ObjectProxy

from slothpal import constants

context = ObjectProxy(None)


class PayPalContext(dict):
    def __init__(self, **kwargs):
        self.update(kwargs)

    def push(self):
        """
        Push the configuration to the global proxy
        """
        if context.__subject__ is not self:
            self._parent = context.__subject__
            context.__subject__ = self
        return self

    def pop(self):
        """
        Reset the configuration object to its initial state
        """
        if context.__subject__ is self:
            context.__subject__ = self._parent

    def __enter__(self):
        return self.push()

    def __exit__(self, type, val, tb):
        self.pop()


def add_urls(config):
    """
    Add PayPal specific URLs to the configuration dict. If the sandbox
    environment is desired set the url endpoint to that
    """
    if config.get("is_sandbox"):
        config.update(endpoint=constants.SANDBOX_ENDPOINT)
    else:
        config.update(endpoint=constants.LIVE_ENDPOINT)


def paypal_context(config):
    """
    Initialize the context manager that will handle all PayPal configuration
    """
    add_urls(config)
    return PayPalContext(paypal=config)
