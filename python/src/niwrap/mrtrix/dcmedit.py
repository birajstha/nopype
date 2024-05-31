# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

DCMEDIT_METADATA = Metadata(
    id="d829a602d8b0ae7db1422fb208af58fe0bfe5b6c",
    name="dcmedit",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class DcmeditTag:
    """
    replace specific tag.
    """
    group: str
    """replace specific tag."""
    element: str
    """replace specific tag."""
    newvalue: str
    """replace specific tag."""
    
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
        cargs.append("-tag")
        cargs.append(self.group)
        cargs.append(self.element)
        cargs.append(self.newvalue)
        return cargs


@dataclasses.dataclass
class DcmeditConfig:
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


class DcmeditOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dcmedit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dcmedit(
    file: InputPathType,
    anonymise: bool = False,
    id_: str | None = None,
    tag: list[DcmeditTag] = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DcmeditConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> DcmeditOutputs:
    """
    dcmedit by J-Donald Tournier (jdtournier@gmail.com).
    
    Edit DICOM file in-place.
    
    Note that this command simply replaces the existing values without modifying
    the DICOM structure in any way. Replacement text will be truncated if it is
    too long to fit inside the existing tag.
    
    WARNING: this command will modify existing data! It is recommended to run
    this command on a copy of the original data set to avoid loss of data.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/dcmedit.html
    
    Args:
        file: the DICOM file to be edited.
        anonymise: remove any identifiable information, by replacing the
            following tags:
            - any tag with Value Representation PN will be replaced
            with 'anonymous'
            - tag (0010,0030) PatientBirthDate will be replaced with
            an empty string
            WARNING: there is no guarantee that this command will
            remove all identiable information, since such information
            may be contained in any number of private vendor-specific
            tags. You will need to double-check the results
            independently if you need to ensure anonymity.
        id_: replace all ID tags with string supplied. This consists of tags
            (0010, 0020) PatientID and (0010, 1000) OtherPatientIDs
        tag: replace specific tag.
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
        NamedTuple of outputs (described in `DcmeditOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMEDIT_METADATA)
    cargs = []
    cargs.append("dcmedit")
    if anonymise:
        cargs.append("-anonymise")
    if id_ is not None:
        cargs.extend(["-id", id_])
    if tag is not None:
        cargs.extend([a for c in [s.run(execution) for s in tag] for a in c])
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
    cargs.append(execution.input_file(file))
    ret = DcmeditOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DCMEDIT_METADATA",
    "DcmeditConfig",
    "DcmeditOutputs",
    "DcmeditTag",
    "dcmedit",
]
