price = {}


class PricingLogic:

    def __repr__(self):
        return "<PricingLogic: {}>".format(self.panel_id)


def recur_array_search(list_var):
    for el in list_var:
        if isinstance(el, list):
            if len(el) > 10:
                yield True
            # search list deeper
            yield from recur_array_search(el)
        elif isinstance(el, dict):
            # search dict deeper
            yield from recur_dict_search(el)


def recur_dict_search(dict_var):
    for k, v in dict_var.items():
        if isinstance(v, list):
            if len(v) > 10:
                yield True
            # search list deeper
            yield from recur_array_search(v)
        elif isinstance(v, dict):
            # search dict deeper
            yield from recur_dict_search(v)
