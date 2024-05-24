# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


V_5TTEDIT_METADATA = Metadata(
    id="076911c966c85ed1562419caa477f3b0ba70edfd",
    name="5ttedit",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class V5tteditConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class V5tteditOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_5ttedit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output modified 5TT image"""


def v_5ttedit(
    input_: InputPathType,
    output: InputPathType,
    cgm: InputPathType | None = None,
    sgm: InputPathType | None = None,
    wm: InputPathType | None = None,
    csf: InputPathType | None = None,
    path: InputPathType | None = None,
    none: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[V5tteditConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> V5tteditOutputs:
    """
    5ttedit by Robert E. Smith (robert.smith@florey.edu.au).
    
    Manually set the partial volume fractions in an ACT five-tissue-type (5TT)
    image using mask images.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/5ttedit.html
    
    Args:
        input_: the 5TT image to be modified
        output: the output modified 5TT image
        cgm: provide a mask of voxels that should be set to cortical grey matter
        sgm: provide a mask of voxels that should be set to sub-cortical grey
            matter
        wm: provide a mask of voxels that should be set to white matter
        csf: provide a mask of voxels that should be set to CSF
        path: provide a mask of voxels that should be set to pathological tissue
        none: provide a mask of voxels that should be cleared (i.e. are
            non-brain); note that this will supersede all other provided masks
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `V5tteditOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_5TTEDIT_METADATA)
    cargs = []
    cargs.append("5ttedit")
    if cgm is not None:
        cargs.extend(["-cgm", execution.input_file(cgm)])
    if sgm is not None:
        cargs.extend(["-sgm", execution.input_file(sgm)])
    if wm is not None:
        cargs.extend(["-wm", execution.input_file(wm)])
    if csf is not None:
        cargs.extend(["-csf", execution.input_file(csf)])
    if path is not None:
        cargs.extend(["-path", execution.input_file(path)])
    if none is not None:
        cargs.extend(["-none", execution.input_file(none)])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(input_))
    cargs.append(execution.input_file(output))
    ret = V5tteditOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V5tteditConfig",
    "V5tteditOutputs",
    "V_5TTEDIT_METADATA",
    "v_5ttedit",
]
