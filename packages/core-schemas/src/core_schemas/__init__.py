"""Esquemas Pydantic del contrato de datos dental.

Punto único de importación. Los notebooks 01 y 04 serializan su salida a estos
modelos: el campo de gaussianas se referencia por hash desde un `TwinSnapshot`,
en vez de embeberse.
"""

from core_schemas.models import (
    SCHEMA_VERSION,
    ClinicalAttributes,
    Color,
    FDICode,
    GaussianPrimitive,
    Modality,
    ModalityIngestion,
    ModalityStatus,
    PatientDigitalTwin,
    Provenance,
    RegionalObservation,
    Support,
    TwinSnapshot,
)

__all__ = [
    "SCHEMA_VERSION",
    "ClinicalAttributes",
    "Color",
    "FDICode",
    "GaussianPrimitive",
    "Modality",
    "ModalityIngestion",
    "ModalityStatus",
    "PatientDigitalTwin",
    "Provenance",
    "RegionalObservation",
    "Support",
    "TwinSnapshot",
]
