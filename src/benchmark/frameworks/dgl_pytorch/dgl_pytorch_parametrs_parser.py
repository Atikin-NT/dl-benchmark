from ..config_parser.dependent_parameters_parser import DependentParametersParser
from ..config_parser.framework_parameters_parser import FrameworkParameters


class DGLPyTorchParametersParser(DependentParametersParser):
    def parse_parameters(self, curr_test):
        return DGLPyTorchParameters()


class DGLPyTorchParameters(FrameworkParameters):
    def __init__(self):
        pass