# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FABBER_DUALECHO_METADATA = Metadata(
    id="5c2326924038c0979ee7f34535218a21f50eb2ea.boutiques",
    name="fabber_dualecho",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FabberDualechoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber_dualecho(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """All output files will be stored in the output directory specified by the
    user."""


def fabber_dualecho(
    output_directory: str,
    method: str,
    model: str,
    data: InputPathType,
    data_order: str | None = "interleave",
    mask_file: InputPathType | None = None,
    mt_list: float | None = None,
    supp_data: InputPathType | None = None,
    options_file: InputPathType | None = None,
    help_flag: bool = False,
    list_methods_flag: bool = False,
    list_models_flag: bool = False,
    list_params_flag: bool = False,
    desc_params_flag: bool = False,
    list_outputs_flag: bool = False,
    evaluate: str | None = None,
    evaluate_params: str | None = None,
    evaluate_nt: float | None = None,
    simple_output_flag: bool = False,
    overwrite_flag: bool = False,
    link_to_latest_flag: bool = False,
    load_models: InputPathType | None = None,
    dump_param_names_flag: bool = False,
    save_model_fit_flag: bool = False,
    save_residuals_flag: bool = False,
    save_model_extras_flag: bool = False,
    save_mvn_flag: bool = False,
    save_mean_flag: bool = False,
    save_std_flag: bool = False,
    save_var_flag: bool = False,
    save_zstat_flag: bool = False,
    save_noise_mean_flag: bool = False,
    save_noise_std_flag: bool = False,
    save_free_energy_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> FabberDualechoOutputs:
    """
    FMRIB's Advanced Bayesian Estimation and Inference tool for FMRI analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fabber
    
    Args:
        output_directory: Directory for output files (including logfile).
        method: Use this inference method.
        model: Use this forward model.
        data: Specify a single input data file.
        data_order: If multiple data files are specified, how they will be\
            handled: concatenate = one after the other, interleave = first record\
            from each file, then second, etc.
        mask_file: Mask file. Inference will only be performed where mask value\
            > 0.
        mt_list: List of masked time points, indexed from 1. These will be\
            ignored in the parameter updates.
        supp_data: 'Supplemental' timeseries data, required for some models.
        options_file: File containing additional options, one per line, in the\
            same form as specified on the command line.
        help_flag: Print this usage method. If given with --method or --model,\
            display relevant method/model usage information.
        list_methods_flag: List all known inference methods.
        list_models_flag: List all known forward models.
        list_params_flag: List model parameters (requires model configuration\
            options to be given).
        desc_params_flag: Descript model parameters (name, description, units)\
            - requires model configuration options to be given. Note that not all\
            models provide parameter descriptions.
        list_outputs_flag: List additional model outputs (requires model\
            configuration options to be given).
        evaluate: Evaluate model. Set to name of output required or blank for\
            default output. Requires model configuration options, --evaluate-params\
            and --evaluate-nt.
        evaluate_params: List of parameter values for evaluation.
        evaluate_nt: Number of time points for evaluation - must be consistent\
            with model options where appropriate.
        simple_output_flag: Instead of usual standard output, simply output\
            series of lines each giving progress as percentage.
        overwrite_flag: If set will overwrite existing output. If not set, new\
            output directories will be created by appending '+' to the directory\
            name.
        link_to_latest_flag: Try to create a link to the most recent output\
            directory with the prefix _latest.
        load_models: Load models dynamically from the specified filename, which\
            should be a DLL/shared library.
        dump_param_names_flag: Write the file paramnames.txt containing the\
            names of the model parameters.
        save_model_fit_flag: Output the model prediction as a 4d volume.
        save_residuals_flag: Output the residuals (difference between the data\
            and the model prediction).
        save_model_extras_flag: Output any additional model-specific timeseries\
            data.
        save_mvn_flag: Output the final MVN distributions.
        save_mean_flag: Output the parameter means.
        save_std_flag: Output the parameter standard deviations.
        save_var_flag: Output the parameter variances.
        save_zstat_flag: Output the parameter Zstats.
        save_noise_mean_flag: Output the noise means. The noise distribution\
            inferred is the precision of a Gaussian noise source.
        save_noise_std_flag: Output the noise standard deviations.
        save_free_energy_flag: Output the free energy, if calculated.
        debug_flag: Output large amounts of debug information. ONLY USE WITH\
            VERY SMALL NUMBERS OF VOXELS.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FabberDualechoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_DUALECHO_METADATA)
    cargs = []
    cargs.append("fabber")
    cargs.append(output_directory)
    cargs.append("--method")
    cargs.extend([
        "--method",
        method
    ])
    cargs.append("--model")
    cargs.extend([
        "--model",
        model
    ])
    cargs.append("--data")
    cargs.extend([
        "--data",
        execution.input_file(data)
    ])
    if data_order is not None:
        cargs.extend([
            "--data-order",
            data_order
        ])
    if mask_file is not None:
        cargs.extend([
            "--mask",
            execution.input_file(mask_file)
        ])
    if mt_list is not None:
        cargs.extend([
            "--mt<n>",
            str(mt_list)
        ])
    if supp_data is not None:
        cargs.extend([
            "--suppdata",
            execution.input_file(supp_data)
        ])
    if options_file is not None:
        cargs.extend([
            "--optfile",
            execution.input_file(options_file)
        ])
    if help_flag:
        cargs.append("--help")
    if list_methods_flag:
        cargs.append("--listmethods")
    if list_models_flag:
        cargs.append("--listmodels")
    if list_params_flag:
        cargs.append("--listparams")
    if desc_params_flag:
        cargs.append("--descparams")
    if list_outputs_flag:
        cargs.append("--listoutputs")
    if evaluate is not None:
        cargs.extend([
            "--evaluate",
            evaluate
        ])
    if evaluate_params is not None:
        cargs.extend([
            "--evaluate-params",
            evaluate_params
        ])
    if evaluate_nt is not None:
        cargs.extend([
            "--evaluate-nt",
            str(evaluate_nt)
        ])
    if simple_output_flag:
        cargs.append("--simple-output")
    if overwrite_flag:
        cargs.append("--overwrite")
    if link_to_latest_flag:
        cargs.append("--link-to-latest")
    if load_models is not None:
        cargs.extend([
            "--loadmodels",
            execution.input_file(load_models)
        ])
    if dump_param_names_flag:
        cargs.append("--dump-param-names")
    if save_model_fit_flag:
        cargs.append("--save-model-fit")
    if save_residuals_flag:
        cargs.append("--save-residuals")
    if save_model_extras_flag:
        cargs.append("--save-model-extras")
    if save_mvn_flag:
        cargs.append("--save-mvn")
    if save_mean_flag:
        cargs.append("--save-mean")
    if save_std_flag:
        cargs.append("--save-std")
    if save_var_flag:
        cargs.append("--save-var")
    if save_zstat_flag:
        cargs.append("--save-zstat")
    if save_noise_mean_flag:
        cargs.append("--save-noise-mean")
    if save_noise_std_flag:
        cargs.append("--save-noise-std")
    if save_free_energy_flag:
        cargs.append("--save-free-energy")
    if debug_flag:
        cargs.append("--debug")
    ret = FabberDualechoOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(output_directory + "/*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FABBER_DUALECHO_METADATA",
    "FabberDualechoOutputs",
    "fabber_dualecho",
]
