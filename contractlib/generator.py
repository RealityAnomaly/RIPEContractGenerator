import os
import importlib
import logging
import pylatex as pl

driver_modules = {}


def _load_driver(name):
    existing = driver_modules.get(name)
    if existing is not None:
        return existing
    
    driver = importlib.import_module(f'.drivers.{name}', __package__)
    if driver is None:
        raise Exception(f'Invalid driver {name}')
    logging.debug(f'loaded driver {name}')

    driver_modules[name] = driver
    return driver


def generate(data):
    doc = pl.Document(geometry_options={"tmargin": "1in", "bmargin": "1in", "lmargin": "1.4in", "rmargin": "1.4in"})

    driver = _load_driver(data['driver'])
    driver.generate(data, doc)
    return doc
