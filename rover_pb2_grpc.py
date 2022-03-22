# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rover_pb2 as rover__pb2


class getMapServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.generate_map_list = channel.unary_unary(
                '/getMapService/generate_map_list',
                request_serializer=rover__pb2.mapRequest.SerializeToString,
                response_deserializer=rover__pb2.mapResponse.FromString,
                )


class getMapServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def generate_map_list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_getMapServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'generate_map_list': grpc.unary_unary_rpc_method_handler(
                    servicer.generate_map_list,
                    request_deserializer=rover__pb2.mapRequest.FromString,
                    response_serializer=rover__pb2.mapResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'getMapService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class getMapService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def generate_map_list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/getMapService/generate_map_list',
            rover__pb2.mapRequest.SerializeToString,
            rover__pb2.mapResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class getMoveSequenceServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_rover_moves = channel.unary_unary(
                '/getMoveSequenceService/get_rover_moves',
                request_serializer=rover__pb2.moveRequest.SerializeToString,
                response_deserializer=rover__pb2.moveResponse.FromString,
                )


class getMoveSequenceServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_rover_moves(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_getMoveSequenceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_rover_moves': grpc.unary_unary_rpc_method_handler(
                    servicer.get_rover_moves,
                    request_deserializer=rover__pb2.moveRequest.FromString,
                    response_serializer=rover__pb2.moveResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'getMoveSequenceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class getMoveSequenceService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_rover_moves(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/getMoveSequenceService/get_rover_moves',
            rover__pb2.moveRequest.SerializeToString,
            rover__pb2.moveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class getMineSerialNumStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_serial_num = channel.unary_unary(
                '/getMineSerialNum/get_serial_num',
                request_serializer=rover__pb2.mineSerialNumRequest.SerializeToString,
                response_deserializer=rover__pb2.mineSerialNumResponse.FromString,
                )


class getMineSerialNumServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_serial_num(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_getMineSerialNumServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_serial_num': grpc.unary_unary_rpc_method_handler(
                    servicer.get_serial_num,
                    request_deserializer=rover__pb2.mineSerialNumRequest.FromString,
                    response_serializer=rover__pb2.mineSerialNumResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'getMineSerialNum', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class getMineSerialNum(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_serial_num(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/getMineSerialNum/get_serial_num',
            rover__pb2.mineSerialNumRequest.SerializeToString,
            rover__pb2.mineSerialNumResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class getSuccessfulFlagStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_successful_flag = channel.unary_unary(
                '/getSuccessfulFlag/get_successful_flag',
                request_serializer=rover__pb2.roverSuccessfulFlagRequest.SerializeToString,
                response_deserializer=rover__pb2.roverSuccessfulFlagResponse.FromString,
                )


class getSuccessfulFlagServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_successful_flag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_getSuccessfulFlagServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_successful_flag': grpc.unary_unary_rpc_method_handler(
                    servicer.get_successful_flag,
                    request_deserializer=rover__pb2.roverSuccessfulFlagRequest.FromString,
                    response_serializer=rover__pb2.roverSuccessfulFlagResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'getSuccessfulFlag', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class getSuccessfulFlag(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_successful_flag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/getSuccessfulFlag/get_successful_flag',
            rover__pb2.roverSuccessfulFlagRequest.SerializeToString,
            rover__pb2.roverSuccessfulFlagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class shareMinePinStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_mine_pin = channel.unary_unary(
                '/shareMinePin/get_mine_pin',
                request_serializer=rover__pb2.minePinRequest.SerializeToString,
                response_deserializer=rover__pb2.minePinResponse.FromString,
                )


class shareMinePinServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_mine_pin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_shareMinePinServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_mine_pin': grpc.unary_unary_rpc_method_handler(
                    servicer.get_mine_pin,
                    request_deserializer=rover__pb2.minePinRequest.FromString,
                    response_serializer=rover__pb2.minePinResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'shareMinePin', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class shareMinePin(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_mine_pin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/shareMinePin/get_mine_pin',
            rover__pb2.minePinRequest.SerializeToString,
            rover__pb2.minePinResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
