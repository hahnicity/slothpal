"""
slothpal.context
~~~~~~~~~~~~~~~~
"""
from peak.util.proxies import ObjectProxy

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
