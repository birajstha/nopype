# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:56:52.605346

import typing

from ..styxdefs import *


V_3D_TPROJECT_METADATA = Metadata(
    id="4574317b83608382b8ab96808a150aafbcffa71d",
    name="3dTproject",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dTprojectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tproject(...)`.
    """
    out_file: OutputPathType
    """Output file."""


def v_3d_tproject(
    runner: Runner,
    in_file: InputPathType,
    tr: float | int | None = None,
    automask: bool = False,
    bandpass: list[float | int] = None,
    blur: float | int | None = None,
    cenmode: typing.Literal["KILL", "ZERO", "NTRP"] | None = None,
    censor: InputPathType | None = None,
    censortr: list[str] = None,
    concat: InputPathType | None = None,
    dsort: list[InputPathType] = None,
    mask: InputPathType | None = None,
    noblock: bool = False,
    norm: bool = False,
    ort: InputPathType | None = None,
    polort: int | None = None,
    stopband: list[float | int] = None,
) -> V3dTprojectOutputs:
    """
    3dTproject, as implemented in Nipype (module: nipype.interfaces.afni, interface:
    TProject).
    
    This program projects (detrends) out various 'nuisance' time series from
    each voxel in the input dataset. Note that all the projections are done via
    linear regression, including the frequency-based options such as
    ``-passband``. In this way, you can bandpass time-censored data, and at the
    same time, remove other time series of no interest (e.g., physiological
    estimates, motion parameters). Shifts voxel time series from input so that
    separate slices are aligned to the same temporal origin.
    
    Args:
        runner: Command runner
        in_file: Input file to 3dtproject.
        tr: Use time step dd for the frequency calculations,rather than the
            value stored in the dataset header.
        automask: Generate a mask automatically.
        bandpass: (a float, a float). Remove all frequencies except those in the
            range.
        blur: Blur (inside the mask only) with a filter that haswidth (fwhm) of
            fff millimeters.spatial blurring (if done) is after the timeseries
            filtering.
        cenmode: 'kill' or 'zero' or 'ntrp'. Specifies how censored time points
            are treated in the output dataset:* mode = zero -- put zero values in
            their place; output dataset is same length as input* mode = kill --
            remove those time points; output dataset is shorter than input* mode =
            ntrp -- censored values are replaced by interpolated neighboring (in
            time) non-censored values, before any projections, and then the analysis
            proceeds without actual removal of any time points -- this feature is to
            keep the spanish inquisition happy.* the default mode is kill !!!.
        censor: Filename of censor .1d time series.this is a file of 1s and 0s,
            indicating whichtime points are to be included (1) and which areto be
            excluded (0).
        censortr: List of strings that specify time indexes to be removed from
            the analysis. each string isof one of the following forms:* ``37`` =>
            remove global time index #37* ``2:37`` => remove time index #37 in run
            #2* ``37..47`` => remove global time indexes #37-47* ``37-47`` => same
            as above* ``2:37..47`` => remove time indexes #37-47 in run #2*
            ``*:0-2`` => remove time indexes #0-2 in all runs * time indexes within
            each run start at 0. * run indexes start at 1 (just be to confusing). *
            n.b.: 2:37,47 means index #37 in run #2 and global time index 47; it
            does not mean index #37 in run #2 and index #47 in run #2.
        concat: The catenation file, as in 3ddeconvolve, containing thetr
            indexes of the start points for each contiguous runwithin the input
            dataset (the first entry should be 0).* also as in 3ddeconvolve, if the
            input dataset is automatically catenated from a collection of datasets,
            then the run start indexes are determined directly, and '-concat' is not
            needed (and will be ignored).* each run must have at least 9 time points
            after censoring, or the program will not work!* the only use made of
            this input is in setting up the bandpass/stopband regressors.* '-ort'
            and '-dsort' regressors run through all time points, as read in. if you
            want separate projections in each run, then you must either break these
            ort files into appropriate components, or you must run 3dtproject for
            each run separately, using the appropriate pieces from the ort files via
            the ``{...}`` selector for the 1d files and the ``[...]`` selector for
            the datasets.
        dsort: Remove the 3d+time time series in dataset fset.* that is, 'fset'
            contains a different nuisance time series for each voxel (e.g., from
            anaticor).* multiple -dsort options are allowed.
        mask: Only operate on voxels nonzero in the mset dataset.* voxels
            outside the mask will be filled with zeros.* if no masking option is
            given, then all voxels will be processed.
        noblock: Also as in 3ddeconvolve, if you want the program to treatan
            auto-catenated dataset as one long run, use this option.however,
            '-noblock' will not affect catenation if you usethe '-concat' option.
        norm: normalize each output time series to have sum ofsquares = 1. this
            is the last operation.
        ort: Remove each column in file.each column will have its mean removed.
        polort: Remove polynomials up to and including degree pp.* default value
            is 2.* it makes no sense to use a value of pp greater than 2, if you are
            bandpassing out the lower frequencies!* for catenated datasets, each run
            gets a separate set set of pp+1 legendre polynomial regressors.* use of
            -polort -1 is not advised (if data mean != 0), even if -ort contains
            constant terms, as all means are removed.
        stopband: (a float, a float). Remove all frequencies in the range.
    Returns:
        NamedTuple of outputs (described in `V3dTprojectOutputs`).
    """
    if bandpass is not None and (len(bandpass) != 2): 
        raise ValueError(f"Length of 'bandpass' must be 2 but was {len(bandpass)}")
    if stopband is not None and (len(stopband) != 2): 
        raise ValueError(f"Length of 'stopband' must be 2 but was {len(stopband)}")
    if (
        (mask is not None) +
        automask
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "mask,\n"
            "automask"
        )
    execution = runner.start_execution(V_3D_TPROJECT_METADATA)
    cargs = []
    cargs.append("3dTproject")
    cargs.extend(["-input", execution.input_file(in_file)])
    cargs.append("[OUT_FILE]")
    if tr is not None:
        cargs.extend(["-TR", str(tr)])
    if automask:
        cargs.append("-automask")
    if bandpass is not None:
        cargs.extend(["-bandpass", *map(str, bandpass)])
    if blur is not None:
        cargs.extend(["-blur", str(blur)])
    if cenmode is not None:
        cargs.extend(["-cenmode", cenmode])
    if censor is not None:
        cargs.extend(["-censor", execution.input_file(censor)])
    if censortr is not None:
        cargs.extend(["-CENSORTR", *censortr])
    if concat is not None:
        cargs.extend(["-concat", execution.input_file(concat)])
    if dsort is not None:
        cargs.extend(["-dsort", *[execution.input_file(f) for f in dsort]])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if noblock:
        cargs.append("-noblock")
    if norm:
        cargs.append("-norm")
    if ort is not None:
        cargs.extend(["-ort", execution.input_file(ort)])
    if polort is not None:
        cargs.extend(["-polort", str(polort)])
    if stopband is not None:
        cargs.extend(["-stopband", *map(str, stopband)])
    ret = V3dTprojectOutputs(
        out_file=execution.output_file(f"{in_file}", optional=True),
    )
    execution.run(cargs)
    return ret
