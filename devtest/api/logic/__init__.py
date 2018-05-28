from collections import deque
from itertools import count


price = {}


class PricingLogic:

    def __repr__(self):
        return "<PricingLogic: {}>".format(self.panel_id)


# Method that's meaningfully faster than sum(1 for i in it) when the iterable may be long
# while maintaining fixed memory overhead behavior
def ilen(it):
    # Make a stateful counting iterator
    cnt = count()
    # zip it with the input iterator, then drain until input exhausted at C level
    deque(zip(it, cnt), 0)  # cnt must be second zip arg to avoid advancing too far
    # Since count 0 based, the next value is the count
    return next(cnt)


def recur_collection_search(collection):
    for v in (collection.values() if isinstance(collection, dict) else collection):
        if isinstance(v, list):
            if len(v) > 10:
                yield True
            # search list deeper
            yield from recur_collection_search(v)
        elif isinstance(v, dict):
            # search dict deeper
            yield from recur_collection_search(v)
