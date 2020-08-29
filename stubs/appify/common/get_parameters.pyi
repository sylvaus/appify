from typing import Callable, Dict, Optional

from appify.common.doc_parser.doc_parser import DocParser
from appify.common.parameter_info import ParameterInfo, ParameterName


def get_parameter_default_annotations(func: Callable, keep_instance_ref: bool = False) -> Dict[
    ParameterName, ParameterInfo]:
    ...


def get_parameter_infos(func: Callable, doc_parser: Optional[DocParser] = None) -> Dict[ParameterName, ParameterInfo]:
    ...
