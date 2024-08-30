# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FNIRT_METADATA = Metadata(
    id="7ec7fbf4a7475816c652cbd66bc1bba77609c146",
    name="fnirt",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class FnirtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fnirt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    field_file_outfile: OutputPathType | None
    """File with warp field."""
    fieldcoeff_file_outfile: OutputPathType | None
    """File with field coefficients."""
    jacobian_file_outfile: OutputPathType | None
    """File containing jacobian of the field."""
    log_file_outfile: OutputPathType | None
    """Name of log-file."""
    modulatedref_file_outfile: OutputPathType | None
    """File containing intensity modulated --ref."""
    out_intensitymap_file_outfile: OutputPathType
    """Files containing info pertaining to intensity mapping."""
    warped_file_outfile: OutputPathType | None
    """Warped image."""


def fnirt(
    in_file: InputPathType,
    ref_file: InputPathType,
    affine_file: InputPathType | None = None,
    config_file: typing.Literal["T1_2_MNI152_2mm", "FA_2_FMRIB58_1mm"] | None = None,
    field_file: InputPathType | None = None,
    fieldcoeff_file: InputPathType | None = None,
    jacobian_file: InputPathType | None = None,
    log_file: InputPathType | None = None,
    modulatedref_file: str | None = None,
    refmask_file: InputPathType | None = None,
    warped_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> FnirtOutputs:
    """
    fnirt by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    FSL non-linear registration.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FNIRT
    
    Args:
        in_file: Name of input image.
        ref_file: Name of reference image.
        affine_file: Name of file containing affine transform.
        config_file: 't1_2_mni152_2mm' or 'fa_2_fmrib58_1mm' or file or string.\
            Name of config file specifying command line arguments.
        field_file: file. Name of output file with field.
        fieldcoeff_file: string representing a file. Name of output file with\
            field coefficients.
        jacobian_file: A file. Name of file for writing out the jacobian of the\
            field (for diagnostic or vbm purposes).
        log_file: Name of log-file.
        modulatedref_file: string representing a file. Name of file for writing\
            out intensity modulated --ref (for diagnostic purposes).
        refmask_file: Name of file with mask in reference space.
        warped_file: Name of output-file containing the --in image after it has\
            been warped to the --ref image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FnirtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FNIRT_METADATA)
    cargs = []
    cargs.append("fnirt")
    if affine_file is not None:
        cargs.append(("--aff=" + execution.input_file(affine_file)))
    if config_file is not None:
        cargs.append(("--config=" + config_file))
    if field_file is not None:
        cargs.append(("--fout=" + execution.input_file(field_file)))
    if fieldcoeff_file is not None:
        cargs.append(("--cout=" + execution.input_file(fieldcoeff_file)))
    cargs.append(("--in=" + execution.input_file(in_file)))
    if jacobian_file is not None:
        cargs.append(("--jout=" + execution.input_file(jacobian_file)))
    if log_file is not None:
        cargs.append(("--logout=" + execution.input_file(log_file)))
    if modulatedref_file is not None:
        cargs.append(("--refout=" + modulatedref_file))
    cargs.append(("--ref=" + execution.input_file(ref_file)))
    if refmask_file is not None:
        cargs.append(("--refmask=" + execution.input_file(refmask_file)))
    if warped_file is not None:
        cargs.append(("--iout=" + execution.input_file(warped_file)))
    ret = FnirtOutputs(
        root=execution.output_file("."),
        field_file_outfile=execution.output_file(f"{pathlib.Path(field_file).name}.nii.gz", optional=True) if field_file is not None else None,
        fieldcoeff_file_outfile=execution.output_file(f"{pathlib.Path(fieldcoeff_file).name}.nii.gz", optional=True) if fieldcoeff_file is not None else None,
        jacobian_file_outfile=execution.output_file(f"{pathlib.Path(jacobian_file).name}.mat", optional=True) if jacobian_file is not None else None,
        log_file_outfile=execution.output_file(f"{pathlib.Path(log_file).name}.txt", optional=True) if log_file is not None else None,
        modulatedref_file_outfile=execution.output_file(f"{modulatedref_file}.nii.gz", optional=True) if modulatedref_file is not None else None,
        out_intensitymap_file_outfile=execution.output_file(f"[OUT_INTENSITYMAP_FILE]", optional=True),
        warped_file_outfile=execution.output_file(f"{pathlib.Path(warped_file).name}.nii.gz", optional=True) if warped_file is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FNIRT_METADATA",
    "FnirtOutputs",
    "fnirt",
]
