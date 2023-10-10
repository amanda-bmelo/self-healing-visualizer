from typing import Any


class Scheduler:
    def __init__(self, fn, *args, t=0, **kw) -> None:
        self.fn = fn
        self.args = args
        self.kw = kw
        self.t = t

    def __call__(self) -> Any:
        self.fn(*self.args, **self.kw)

    def __repr__(self) -> str:
        return f"<{self.fn.__name__}[t={self.t - GlobalClock.t}]:>"

class GlobalClock:
    t = 0
    current_batch = []
    next_batch = []

    @classmethod
    def roll_next_batch(cls):
        cls.t += 1
        nb = []
        cb = []
        for fn in cls.next_batch:
            if fn.t <= cls.t:
                cb.append(fn)
            else:
                nb.append(fn)
        cls.current_batch = cb
        cls.next_batch = nb
        return cls.current_batch
    
    @classmethod
    def run_all_batches(cls, middleware):
        fns = []
        while(fns != [] or GlobalClock.next_batch != []):
            for fn in fns:
                fn()
            fns = GlobalClock.roll_next_batch()
            middleware(cls)


    @classmethod
    def schedule(cls, fn, dt=0):
        def _fn(*args, **kw):
            GlobalClock.next_batch.append(Scheduler(fn, *args, t=GlobalClock.t + dt, **kw))
        return _fn