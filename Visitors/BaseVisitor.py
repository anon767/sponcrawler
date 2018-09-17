from abc import ABC, abstractmethod


class BaseVisitor:
    @abstractmethod
    def parse(self, content):
        pass
