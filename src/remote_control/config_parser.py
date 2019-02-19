from lxml import etree


class machine:
    def __init__(self, params):
        self.ip = params[0]
        self.login = params[1]
        self.psw = params[2]
        self.os_type = params[3]
        self.path_to_ftp_client = params[4]
        self.path_to_OpenVINO_env = params[5]
        self.benchmark_config = params[6] 


def parse_config(config):
    with open(config) as file:
        openconfig = file.read()
    utf_parser = etree.XMLParser(encoding = 'utf-8')
    root = etree.fromstring(openconfig.encode('utf-8'), parser = utf_parser)
    machine_list = []
    for machine_tag in root.getchildren():
        machine_parameters = [None] * 7
        for machine_parameter in machine_tag.getchildren():
            if machine_parameter.tag == 'Ip':
                machine_parameters[0] = machine_parameter.text
            if machine_parameter.tag == 'Login':
                machine_parameters[1] = machine_parameter.text
            if machine_parameter.tag == 'Password':
                machine_parameters[2] = machine_parameter.text
            if machine_parameter.tag == 'Os_type':
                machine_parameters[3] = machine_parameter.text
            if machine_parameter.tag == 'Path_to_ftp_client':
                machine_parameters[4] = (machine_parameter.text)
            if machine_parameter.tag == 'Path_to_OpenVINO_env':
                machine_parameters[5] = (machine_parameter.text)
            if machine_parameter.tag == 'Benchmark_config':
                machine_parameters[6] = (machine_parameter.text)
        machine_list.append(machine(machine_parameters))
    return machine_list