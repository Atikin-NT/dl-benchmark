from enum import Enum


class Status(Enum):
    EXIT_SUCCESS = 0
    EXIT_FAILURE = 1

    INFERENCE_FAILURE = 2
    CPP_BENCHMARK_FAILURE = 3

    PROCESS_TIMEOUT = -9
    PROCESS_CREATE_ERROR = 127
    PROCESS_CMD_ERROR = 400
    EXECUTOR_NOT_FOUND = 438