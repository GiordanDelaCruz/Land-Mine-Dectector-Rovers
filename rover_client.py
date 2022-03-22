from __future__ import print_function

import logging

import grpc
import rover_pb2 as pb2
import rover_pb2_grpc as pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.RoverServiceStub(channel)

        # Create a valid request message
        input = pb2.moveRequest()

        response = stub.get_rover_moves(input)
    print("Greeter client received: " + response.move_sequence)


if __name__ == '__main__':
    logging.basicConfig()
    run()
