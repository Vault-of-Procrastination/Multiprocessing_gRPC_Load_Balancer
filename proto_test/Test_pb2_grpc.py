# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto_test.Test_pb2 as Test__pb2


class Test_StreamerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.One_to_One = channel.unary_unary(
                '/Test_Streamer/One_to_One',
                request_serializer=Test__pb2.send_msg.SerializeToString,
                response_deserializer=Test__pb2.response_msg.FromString,
                )
        self.Many_to_One = channel.stream_unary(
                '/Test_Streamer/Many_to_One',
                request_serializer=Test__pb2.send_msg.SerializeToString,
                response_deserializer=Test__pb2.response_msg.FromString,
                )
        self.One_to_Many = channel.unary_stream(
                '/Test_Streamer/One_to_Many',
                request_serializer=Test__pb2.send_msg.SerializeToString,
                response_deserializer=Test__pb2.response_msg.FromString,
                )
        self.Many_to_Many = channel.stream_stream(
                '/Test_Streamer/Many_to_Many',
                request_serializer=Test__pb2.send_msg.SerializeToString,
                response_deserializer=Test__pb2.response_msg.FromString,
                )


class Test_StreamerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def One_to_One(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Many_to_One(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def One_to_Many(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Many_to_Many(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Test_StreamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'One_to_One': grpc.unary_unary_rpc_method_handler(
                    servicer.One_to_One,
                    request_deserializer=Test__pb2.send_msg.FromString,
                    response_serializer=Test__pb2.response_msg.SerializeToString,
            ),
            'Many_to_One': grpc.stream_unary_rpc_method_handler(
                    servicer.Many_to_One,
                    request_deserializer=Test__pb2.send_msg.FromString,
                    response_serializer=Test__pb2.response_msg.SerializeToString,
            ),
            'One_to_Many': grpc.unary_stream_rpc_method_handler(
                    servicer.One_to_Many,
                    request_deserializer=Test__pb2.send_msg.FromString,
                    response_serializer=Test__pb2.response_msg.SerializeToString,
            ),
            'Many_to_Many': grpc.stream_stream_rpc_method_handler(
                    servicer.Many_to_Many,
                    request_deserializer=Test__pb2.send_msg.FromString,
                    response_serializer=Test__pb2.response_msg.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Test_Streamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Test_Streamer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def One_to_One(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Test_Streamer/One_to_One',
            Test__pb2.send_msg.SerializeToString,
            Test__pb2.response_msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Many_to_One(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Test_Streamer/Many_to_One',
            Test__pb2.send_msg.SerializeToString,
            Test__pb2.response_msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def One_to_Many(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Test_Streamer/One_to_Many',
            Test__pb2.send_msg.SerializeToString,
            Test__pb2.response_msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Many_to_Many(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Test_Streamer/Many_to_Many',
            Test__pb2.send_msg.SerializeToString,
            Test__pb2.response_msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)