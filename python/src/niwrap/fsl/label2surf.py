# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

LABEL2SURF_METADATA = Metadata(
    id="315ef032b1536f62bbbd41475d45ef54234a6d4e",
    name="label2surf",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class Label2surfOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label2surf(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_surf: OutputPathType
    """Resulting output surface file"""


def label2surf(
    input_surface: InputPathType,
    output_surface: str,
    labels: InputPathType,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> Label2surfOutputs:
    """
    label2surf by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Transform a group of labels into a surface.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fslutils
    
    Args:
        input_surface: Input surface file.
        output_surface: Output surface file.
        labels: ASCII list of label files.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Label2surfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL2SURF_METADATA)
    cargs = []
    cargs.append("label2surf")
    cargs.append("--surf")
    cargs.extend(["--surf", execution.input_file(input_surface)])
    cargs.append("--out")
    cargs.extend(["--out", output_surface])
    cargs.append("--labels")
    cargs.extend(["--labels", execution.input_file(labels)])
    if verbose_flag:
        cargs.append("--verbose")
    if help_flag:
        cargs.append("--help")
    ret = Label2surfOutputs(
        root=execution.output_file("."),
        out_surf=execution.output_file(f"{output_surface}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL2SURF_METADATA",
    "Label2surfOutputs",
    "label2surf",
]
