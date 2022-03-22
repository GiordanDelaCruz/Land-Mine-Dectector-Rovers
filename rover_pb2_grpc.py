# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rover_pb2 as rover__pb2


class RoverServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.generate_map_list = channel.unary_unary(
                '/RoverService/generate_map_list',
                request_serializer=rover__pb2.mapRequest.SerializeToString,
                response_deserializer=rover__pb2.mapResponse.FromString,
                )
        self.getRoverMoves = channel.unary_unary(
                '/RoverService/getRoverMoves',
                request_serializer=rover__pb2.moveRequest.SerializeToString,
                response_deserializer=rover__pb2.moveResponse.FromString,
                )
        self.get_serial_num = channel.unary_unary(
                '/RoverService/get_serial_num',
                request_serializer=rover__pb2.mineSerialNumRequest.SerializeToString,
                response_deserializer=rover__pb2.mineSerialNumResponse.FromString,
                )
        self.get_successful_flag = channel.unary_unary(
                '/RoverService/get_successful_flag',
                request_serializer=rover__pb2.roverSuccessfulFlagRequest.SerializeToString,
                response_deserializer=rover__pb2.roverSuccessfulFlagResponse.FromString,
                )
        self.get_mine_pin = channel.unary_unary(
                '/RoverService/get_mine_pin',
                request_serializer=rover__pb2.minePinRequest.SerializeToString,
                response_deserializer=rover__pb2.minePinResponse.FromString,
                )


class RoverServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def generate_map_list(self, request, context):
        """[S1] Get map 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getRoverMoves(self, request, context):
        """[S2] Get stream of commands 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_serial_num(self, request, context):
        """[S3] Get mine serial number
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_successful_flag(self, request, context):
        """[S4] Let server know if rover has executed all commands successfully or not (mine might expload)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_mine_pin(self, request, context):
        """[S5] Share a min PIN with the server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RoverServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'generate_map_list': grpc.unary_unary_rpc_method_handler(
                    servicer.generate_map_list,
                    request_deserializer=rover__pb2.mapRequest.FromString,
                    response_serializer=rover__pb2.mapResponse.SerializeToString,
            ),
            'getRoverMoves': grpc.unary_unary_rpc_method_handler(
                    servicer.getRoverMoves,
                    request_deserializer=rover__pb2.moveRequest.FromString,
                    response_serializer=rover__pb2.moveResponse.SerializeToString,
            ),
            'get_serial_num': grpc.unary_unary_rpc_method_handler(
                    servicer.get_serial_num,
                    request_deserializer=rover__pb2.mineSerialNumRequest.FromString,
                    response_serializer=rover__pb2.mineSerialNumResponse.SerializeToString,
            ),
            'get_successful_flag': grpc.unary_unary_rpc_method_handler(
                    servicer.get_successful_flag,
                    request_deserializer=rover__pb2.roverSuccessfulFlagRequest.FromString,
                    response_serializer=rover__pb2.roverSuccessfulFlagResponse.SerializeToString,
            ),
            'get_mine_pin': grpc.unary_unary_rpc_method_handler(
                    servicer.get_mine_pin,
                    request_deserializer=rover__pb2.minePinRequest.FromString,
                    response_serializer=rover__pb2.minePinResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RoverService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RoverService(object):
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
        return grpc.experimental.unary_unary(request, target, '/RoverService/generate_map_list',
            rover__pb2.mapRequest.SerializeToString,
            rover__pb2.mapResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getRoverMoves(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RoverService/getRoverMoves',
            rover__pb2.moveRequest.SerializeToString,
            rover__pb2.moveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/RoverService/get_serial_num',
            rover__pb2.mineSerialNumRequest.SerializeToString,
            rover__pb2.mineSerialNumResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/RoverService/get_successful_flag',
            rover__pb2.roverSuccessfulFlagRequest.SerializeToString,
            rover__pb2.roverSuccessfulFlagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/RoverService/get_mine_pin',
            rover__pb2.minePinRequest.SerializeToString,
            rover__pb2.minePinResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
