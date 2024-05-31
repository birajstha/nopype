# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

VOLUME_LABEL_IMPORT_METADATA = Metadata(
    id="e9d70dc54a1dd1fbee743a47b24464f06bc378b4",
    name="volume-label-import",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeLabelImportOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_label_import(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output workbench label volume"""


def volume_label_import(
    input_: InputPathType,
    label_list_file: str,
    output: InputPathType,
    opt_discard_others: bool = False,
    opt_unlabeled_value_value: int | None = None,
    opt_subvolume_subvol: str | None = None,
    opt_drop_unused_labels: bool = False,
    runner: Runner = None,
) -> VolumeLabelImportOutputs:
    """
    volume-label-import by Washington University School of Medicin.
    
    Import a label volume to workbench format.
    
    Creates a label volume from an integer-valued volume file. The label name
    and color information is stored in the volume header in a nifti extension,
    with a similar format as in caret5, see -volume-help. You may specify the
    empty string (use "") for <label-list-file>, which will be treated as if it
    is an empty file. The label list file must have the following format (2
    lines per label):
    
    <labelname>
    <key> <red> <green> <blue> <alpha>
    ...
    
    Label names are specified on a separate line from their value and color, in
    order to let label names contain spaces. Whitespace is trimmed from both
    ends of the label name, but is kept if it is in the middle of a label. Do
    not specify the "unlabeled" key in the file, it is assumed that 0 means not
    labeled unless -unlabeled-value is specified. The value of <key> specifies
    what value in the imported file should be used as this label (these same key
    values are also used in the output file). The values of <red>, <green>,
    <blue> and <alpha> must be integers from 0 to 255, and will specify the
    color the label is drawn as (alpha of 255 means fully opaque, which is
    probably what you want).
    
    By default, it will create new label names with names like LABEL_5 for any
    values encountered that are not mentioned in the list file, specify
    -discard-others to instead set these values to the "unlabeled" key.
    
    Args:
        input_: the input volume file
        label_list_file: text file containing the values and names for labels
        output: the output workbench label volume
        opt_discard_others: set any voxels with values not mentioned in the
            label list to the ??? label
        opt_unlabeled_value_value: set the value that will be interpreted as
            unlabeled: the numeric value for unlabeled (default 0)
        opt_subvolume_subvol: select a single subvolume to import: the subvolume
            number or name
        opt_drop_unused_labels: remove any unused label values from the label
            table
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeLabelImportOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_LABEL_IMPORT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-label-import")
    cargs.append(execution.input_file(input_))
    cargs.append(label_list_file)
    cargs.append(execution.input_file(output))
    if opt_discard_others:
        cargs.append("-discard-others")
    if opt_unlabeled_value_value is not None:
        cargs.extend(["-unlabeled-value", str(opt_unlabeled_value_value)])
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    if opt_drop_unused_labels:
        cargs.append("-drop-unused-labels")
    ret = VolumeLabelImportOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_LABEL_IMPORT_METADATA",
    "VolumeLabelImportOutputs",
    "volume_label_import",
]
