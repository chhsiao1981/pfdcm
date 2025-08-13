# -*- coding: utf-8 -*-

from pfdcm import config
from pfdcm.controllers import pacsQRcontroller


async def get_studies_handler(service: str, patientID: str, accession_number: str):
    query = {}
    if patientID:
        query['patientID'] = patientID
    if accession_number:
        query['accessionNumber'] = accession_number

    ret = await pacsQRcontroller.pypx_do(
        service,
        'default',
        query,
    )
