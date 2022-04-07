import os

from chalicelib.data.base.base_document_extractor import CompoundDocumentExtractor
from chalicelib.data.documents.json_extractor import CompoundJSONExtractor
from chalicelib.data.documents.nosql_extractor import CompoundNoSQLExtractor


def get_document_extractor() -> CompoundDocumentExtractor:
    if os.getenv("ENVIRONMENT") == "prod":
        return CompoundNoSQLExtractor()
    elif os.getenv("ENVIRONMENT") == "local":
        return CompoundJSONExtractor()
    else:
        raise ValueError('environment variable: ENVIRONMENT needs to be set to "prod" or "local"')
