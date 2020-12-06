import panflute as pf


def headerConvert(elem, doc):
    if isinstance(elem, pf.Header):
        if 'custom-style' in elem.attributes:
            return pf.Div(pf.Para(*elem.content),
                          identifier=elem.identifier,
                          classes=elem.classes,
                          attributes=elem.attributes)
        if 'unnumbered' in elem.classes:
            attributes = ({"custom-style": f"Unnumbered Header {elem.level}"})
            attributes.update(elem.attributes)
            return pf.Div(pf.Para(*elem.content),
                          identifier=elem.identifier,
                          classes=elem.classes,
                          attributes=attributes)

    return elem


def main(doc=None):
    return pf.run_filter(headerConvert, doc=doc)


if __name__ == "__main__":
    main()
