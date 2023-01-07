# coding: utf-8

from leancloud import Engine
from leancloud import LeanEngineError

engine = Engine()


@engine.define
def leancloud(**params):
    import index
    index.handler(None,None)

if __name__ == '__main__':
    leancloud()