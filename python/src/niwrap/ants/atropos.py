# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ATROPOS_METADATA = Metadata(
    id="89ba3be34b24cc2c34a5c94b22919ec83f82ec3c.boutiques",
    name="atropos",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AtroposOutputs(typing.NamedTuple):
    """
    Output object returned when calling `atropos(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    classified_image: OutputPathType
    """The classified image output file."""
    posterior_probability_images: OutputPathType
    """Optional posterior probability images output files."""


def atropos(
    intensity_image: list[str],
    initialization: str,
    mask_image: str,
    likelihood_model: str,
    output: str,
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    bspline: str | None = "6,1x1x...,3",
    partial_volume_label_set: list[str] | None = None,
    use_partial_volume_likelihoods: typing.Literal[0, 1] | None = None,
    posterior_formulation: str | None = None,
    convergence: str = "[5,0.001]",
    mrf: str | None = "0.3,1x1x...",
    icm: str | None = "1,1,''",
    use_random_seed: typing.Literal[0, 1] | None = None,
    minimize_memory_usage: typing.Literal[0, 1] | None = None,
    winsorize_outliers: str | None = None,
    use_euclidean_distance: typing.Literal[0, 1] | None = None,
    label_propagation: str | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    runner: Runner | None = None,
) -> AtroposOutputs:
    """
    A finite mixture modeling (FMM) segmentation approach with possibilities for
    specifying prior constraints. These prior constraints include the specification
    of a prior label image, prior probability images (one for each class), and/or an
    MRF prior to enforce spatial smoothing of the labels. All segmentation images
    including priors and masks must be in the same voxel and physical space. Similar
    algorithms include FAST and SPM.
    
    Author: Advanced Normalization Tools (ANTs) Contributors
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        intensity_image: One or more scalar images is specified for\
            segmentation. For segmentation scenarios with no prior information, the\
            first scalar image encountered on the command line is used to order\
            labelings such that the class with the smallest intensity signature is\
            class '1' through class 'N' which represents the voxels with the\
            largest intensity values. The optional adaptive smoothing weight\
            parameter is applicable only when using prior label or probability\
            images. This scalar parameter is to be specified between [0,1] which\
            smooths each labeled region separately and modulates the intensity\
            measurement at each voxel in each intensity image between the original\
            intensity and its smoothed counterpart. The smoothness parameters are\
            governed by the -b/--bspline option.
        initialization: To initialize the FMM parameters, one of the specified\
            options (Random, Otsu, KMeans, PriorProbabilityImages, or\
            PriorLabelImage) must be used.
        mask_image: The image mask (which is required) defines the region which\
            is to be labeled by the Atropos algorithm.
        likelihood_model: Both parametric and non-parametric options exist in\
            Atropos.
        output: The output consists of a labeled image where each voxel in the\
            masked region is assigned a label from 1, 2, ..., N. Optionally, one\
            can also output the posterior probability images specified in the same\
            format as the prior probability images, e.g. posterior%02d.nii.gz\
            (C-style file name formatting).
        image_dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, Atropos tries to infer\
            the dimensionality from the first input image.
        bspline: If the adaptive smoothing weights are > 0, the intensity\
            images are smoothed in calculating the likelihood values. This is to\
            account for subtle intensity differences across the same tissue\
            regions.
        partial_volume_label_set: The partial volume estimation option allows\
            one to model mixtures of classes within single voxels.
        use_partial_volume_likelihoods: The user can specify whether or not to\
            use the partial volume likelihoods.
        posterior_formulation: Different posterior probability formulations are\
            possible as are different update options.
        convergence: Convergence is determined by calculating the mean maximum\
            posterior probability over the region of interest at each iteration.\
            When this value decreases or increases less than the specified\
            threshold from the previous iteration or the maximum number of\
            iterations is exceeded the program terminates.
        mrf: Markov random field (MRF) theory provides a general framework for\
            enforcing spatially contextual constraints on the segmentation\
            solution.
        icm: Asynchronous updating requires the construction of an ICM code\
            image which is a label image (with labels in the range\
            {1,..,MaximumICMCode}) constructed such that no MRF neighborhood has\
            duplicate ICM code labels.
        use_random_seed: Initialize internal random number generator with a\
            random seed.
        minimize_memory_usage: By default, memory usage is not minimized,\
            however, if this is needed, the various probability and distance images\
            are calculated on the fly instead of being stored in memory at each\
            iteration. Also, if prior probability images are used, only the\
            non-negligible pixel values are stored in memory.
        winsorize_outliers: To remove the effects of outliers in calculating\
            the weighted mean and weighted covariance, the user can opt to remove\
            the outliers through the options specified below.
        use_euclidean_distance: Given prior label or probability images, the\
            labels are propagated throughout the masked region so that every voxel\
            in the mask is labeled.
        label_propagation: The propagation of each prior label can be\
            controlled by the lambda and boundary probability parameters.
        verbose: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AtroposOutputs`).
    """
    if partial_volume_label_set is not None and not (1 <= len(partial_volume_label_set)): 
        raise ValueError(f"Length of 'partial_volume_label_set' must be greater than 1 but was {len(partial_volume_label_set)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(ATROPOS_METADATA)
    cargs = []
    cargs.append("Atropos")
    if image_dimensionality is not None:
        cargs.extend([
            "--image-dimensionality",
            str(image_dimensionality)
        ])
    cargs.extend([
        "--intensity-image",
        *intensity_image
    ])
    if bspline is not None:
        cargs.extend([
            "--bspline",
            bspline
        ])
    cargs.extend([
        "--initialization",
        initialization
    ])
    if partial_volume_label_set is not None:
        cargs.extend([
            "--partial-volume-label-set",
            *partial_volume_label_set
        ])
    if use_partial_volume_likelihoods is not None:
        cargs.extend([
            "--use-partial-volume-likelihoods",
            str(use_partial_volume_likelihoods)
        ])
    if posterior_formulation is not None:
        cargs.extend([
            "--posterior-formulation",
            posterior_formulation
        ])
    cargs.extend([
        "-x",
        mask_image
    ])
    cargs.extend([
        "--convergence",
        convergence
    ])
    cargs.extend([
        "--likelihood-model",
        likelihood_model
    ])
    if mrf is not None:
        cargs.extend([
            "-m",
            mrf
        ])
    if icm is not None:
        cargs.extend([
            "--icm",
            icm
        ])
    if use_random_seed is not None:
        cargs.extend([
            "--use-random-seed",
            str(use_random_seed)
        ])
    cargs.extend([
        "-o",
        output
    ])
    if minimize_memory_usage is not None:
        cargs.extend([
            "--minimize-memory-usage",
            str(minimize_memory_usage)
        ])
    if winsorize_outliers is not None:
        cargs.extend([
            "--winsorize-outliers",
            winsorize_outliers
        ])
    if use_euclidean_distance is not None:
        cargs.extend([
            "--use-euclidean-distance",
            str(use_euclidean_distance)
        ])
    if label_propagation is not None:
        cargs.extend([
            "--label-propagation",
            label_propagation
        ])
    if verbose is not None:
        cargs.extend([
            "--verbose",
            str(verbose)
        ])
    ret = AtroposOutputs(
        root=execution.output_file("."),
        classified_image=execution.output_file("[CLASSIFIED_IMAGE]"),
        posterior_probability_images=execution.output_file("[POSTERIOR_PROBABILITY_IMAGE_FILE_FORMAT]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ATROPOS_METADATA",
    "AtroposOutputs",
    "atropos",
]
