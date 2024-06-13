from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class send_msg(_message.Message):
    __slots__ = ("send",)
    SEND_FIELD_NUMBER: _ClassVar[int]
    send: str
    def __init__(self, send: _Optional[str] = ...) -> None: ...

class response_msg(_message.Message):
    __slots__ = ("success", "msg")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    success: bool
    msg: str
    def __init__(self, success: bool = ..., msg: _Optional[str] = ...) -> None: ...
