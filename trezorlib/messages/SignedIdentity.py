# Automatically generated by pb2py
from trezorlib import protobuf as p
t = p.MessageType('SignedIdentity')
t.wire_type = 54
t.add_field(1, 'address', p.UnicodeType)
t.add_field(2, 'public_key', p.BytesType)
t.add_field(3, 'signature', p.BytesType)
SignedIdentity = t