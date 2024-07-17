# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_AUTO_TLRC_METADATA = Metadata(
    id="38e060c8112b9cab9afd0bbc8d762c36d4cec2fe",
    name="@auto_tlrc",
)


class AutoTlrcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_auto_tlrc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType | None
    """Transformed anatomical volume dataset in TLRC space."""
    transform_file: OutputPathType | None
    """Transform used to align the anatomical dataset to the template."""


def _auto_tlrc(
    base_template: InputPathType,
    input_anat: InputPathType,
    apar: InputPathType,
    input_dataset: InputPathType,
    no_ss: bool = False,
    warp_orig_vol: bool = False,
    dxyz: float | int | None = None,
    dx: float | int | None = None,
    dy: float | int | None = None,
    dz: float | int | None = None,
    pad_base: float | int | None = None,
    keep_tmp: bool = False,
    clean: bool = False,
    xform: str | None = None,
    no_avoid_eyes: bool = False,
    ncr: bool = False,
    onepass: bool = False,
    twopass: bool = False,
    maxite: float | int | None = None,
    not_ok_maxite: bool = False,
    inweight: bool = False,
    rigid_equiv: bool = False,
    init_xform: str | None = None,
    no_pre: bool = False,
    out_space: str | None = None,
    v_3d_allineate: bool = False,
    v_3d_alcost: str | None = None,
    overwrite: bool = False,
    pad_input: float | int | None = None,
    onewarp: bool = False,
    twowarp: bool = False,
    rmode: str | None = None,
    prefix: str | None = None,
    suffix: str | None = None,
    keep_view: bool = False,
    base_copy: str | None = None,
    base_list: bool = False,
    use_gz: bool = False,
    verb: bool = False,
    runner: Runner | None = None,
) -> AutoTlrcOutputs:
    """
    @auto_tlrc by Ziad S. Saad.
    
    A script to transform an anatomical dataset to align with some standard
    space template and to apply the same TLRC transform obtained with @auto_tlrc
    in Usage 1 mode to other datasets.
    
    More information: https://afni.nimh.nih.gov/afni/suma
    
    Args:
        base_template: Reference anatomical volume. Usually this volume is in\
            some standard space like TLRC or MNI space.
        input_anat: Original anatomical volume (+orig). The skull is removed by\
            this script unless instructed otherwise (-no_ss).
        apar: An anatomical dataset in TLRC space created using Usage 1 of\
            @auto_tlrc.
        input_dataset: Dataset (typically EPI time series or statistical\
            dataset) to transform to TLRC space per the transform in TLRC_parent.
        no_ss: Do not strip skull of input data set because the skull has\
            already been removed or because the template still has the skull.
        warp_orig_vol: Produce a TLRC version of the input volume, rather than\
            a TLRC version of the skull-stripped input.
        dxyz: Cubic voxel size of output DSET in TLRC space. Default is the\
            resolution of the template.
        dx: Size of voxel in the x direction (Right-Left). Default is 1mm.
        dy: Size of voxel in the y direction (Anterior-Posterior). Default is\
            1mm.
        dz: Size of voxel in the z direction (Inferior-Superior). Default is\
            1mm.
        pad_base: Pad the base dataset by MM mm in each direction. Default is\
            15 mm.
        keep_tmp: Keep temporary files.
        clean: Clean all temporary files, likely left from -keep_tmp option\
            then exit.
        xform: Transform to use for warping: Choose from affine_general or\
            shift_rotate_scale. Default is affine_general.
        no_avoid_eyes: An option that gets passed to 3dSkullStrip. Use it when\
            parts of the frontal lobes get clipped.
        ncr: Do not use -coarserot option for 3dWarpDrive, which is a default.
        onepass: Turns off -twopass option for 3dWarpDrive. This will speed up\
            the registration but might fail if the datasets are far apart.
        twopass: Opposite of -onepass, default.
        maxite: Maximum number of iterations for 3dWarpDrive. Default is 50 for\
            first pass and then doubled to 100 in second pass.
        not_ok_maxite: Continue running even if maximum iterations is reached.
        inweight: Apply -weight INPUT (in 3dWarpDrive). By default, 3dWarpDrive\
            uses the BASE dataset to weight the alignment cost.
        rigid_equiv: Output the rigid-body version of the alignment. Resultant\
            volume is NOT in TLRC space.
        init_xform: Apply affine transform in XFORM0.1D before beginning\
            registration and then include XFORM0.1D in the final transform.
        no_pre: Delete temporary dataset created by -init_xform.
        out_space: Set the output to a particular space.
        v_3d_allineate: Use 3dAllineate with the lpa+ZZ cost function instead\
            of 3dWarpDrive.
        v_3d_alcost: Use another cost function like nmi for 3dAllineate.
        overwrite: Overwrite existing output.
        pad_input: Pad the input dataset by MM mm in each direction.
        onewarp: Create follower data with one interpolation step, instead of\
            two. This option reduces blurring of the output data.
        twowarp: Create follower data with two interpolations step, instead of\
            one. This option is for backward compatibility.
        rmode: Resampling mode. Choose from: linear, cubic, NN or quintic.\
            Default for 'Usage 1' is cubic.
        prefix: Name of the output dataset.
        suffix: Name the output dataset by appending this suffix to the prefix\
            of the input data.
        keep_view: Do not mark output dataset as +tlrc.
        base_copy: Copy base (template) dataset into COPY_PREFIX.
        base_list: List the full path of the base dataset.
        use_gz: When using '-suffix ..', behave as if you had provided a prefix\
            with '*.gz' at the end.
        verb: Increase verbosity of the script.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AutoTlrcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_AUTO_TLRC_METADATA)
    cargs = []
    cargs.append("@auto_tlrc")
    cargs.append("[OPTIONS]")
    cargs.append("<-base")
    cargs.append("template>")
    cargs.append("<-input")
    cargs.append("anat>")
    ret = AutoTlrcOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(f"{prefix}.nii.gz") if prefix is not None else None,
        transform_file=execution.output_file(f"{prefix}.Xat.1D", optional=True) if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AutoTlrcOutputs",
    "_AUTO_TLRC_METADATA",
    "_auto_tlrc",
]
