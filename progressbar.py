from typing import Iterable
from progressbar import bar
from typing import TypeVar, Iterable

T = TypeVar('T')


def progressbar(iterator: Iterable[T], min_value: int = 0, max_value: int = None,
                widgets=None, prefix: str = None, suffix: str = None, **kwargs) -> Iterable[T]:
    progressbar = bar.ProgressBar(
        min_value=min_value, max_value=max_value,
        widgets=widgets, prefix=prefix, suffix=suffix, **kwargs)

    for result in progressbar(iterator):
        yield result
