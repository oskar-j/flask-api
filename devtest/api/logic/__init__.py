price = {}


class PricingLogic:

    def __repr__(self):
        return "<PricingLogic: {}>".format(self.panel_id)


def recur_array_search(dict_var):
    for k, v in dict_var.items():
        if isinstance(v, list):
            if len(v) > 10:
                yield True
        elif isinstance(v, dict):
            recur_array_search(v)
