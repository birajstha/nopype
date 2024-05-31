# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

METADATA_REMOVE_PROVENANCE_METADATA = Metadata(
    id="44f98a54a9edff1763ec9491c845b2141c304315",
    name="metadata-remove-provenance",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class MetadataRemoveProvenanceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metadata_remove_provenance(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def metadata_remove_provenance(
    input_file: str,
    output_file: str,
    runner: Runner = None,
) -> MetadataRemoveProvenanceOutputs:
    """
    metadata-remove-provenance by Washington University School of Medicin.
    
    Remove provenance information from file metadata.
    
    Removes the provenance metadata fields added by workbench during processing.
    
    Args:
        input_file: the file to remove provenance information from
        output_file: output - the name to save the modified file as
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MetadataRemoveProvenanceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METADATA_REMOVE_PROVENANCE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metadata-remove-provenance")
    cargs.append(input_file)
    cargs.append(output_file)
    ret = MetadataRemoveProvenanceOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METADATA_REMOVE_PROVENANCE_METADATA",
    "MetadataRemoveProvenanceOutputs",
    "metadata_remove_provenance",
]
