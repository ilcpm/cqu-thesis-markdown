#!/usr/bin/env python3
import panflute as pf
from urllib import parse

def action(elem, doc):
    if isinstance(elem, (pf.Header, pf.Span)):
        elem.identifier = parse.quote(elem.identifier)
        return elem


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == "__main__":
    main()
