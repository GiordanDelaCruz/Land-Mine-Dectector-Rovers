from concurrent import futures
import logging

import grpc
import rover_pb2 as pb2
import rover_pb2_grpc as pb2_grpc

from enum import Enum
from turtle import update
import requests

# Global variables
BASE_LINK = "https://coe892.reev.dev/lab1/rover/"

class GroundControl(pb2_grpc.getMapServiceServicer):

    def get_rover_moves(self):
        # 1. Read rover data from API
        api_link = BASE_LINK + str(self.rover_number)
        response = requests.get(api_link)

        # 2. Save sequence of moves
        self.move_sequence = response.json()['data']['moves']
        # print("\nRover {num}\nmove_seq = {moves}".format(num = self.rover_number, moves = self.move_sequence))  
        # print("Move type: {type}".format( type = type(self.move_sequence[0])) )

        return self.move_sequence

    def getMoveSequenceService(self, request, context):

        return pb2.moveResponse(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_getMoveSequenceServiceServicer_to_server(GroundControl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()