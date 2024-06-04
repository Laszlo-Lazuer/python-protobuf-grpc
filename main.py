import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2

def simple():
    return simple_pb2.Simple(
        id=42,
        is_simple=True,
        name="My name",
        sample_lists=[1,2,3]
    )

def complex():
    message = complex_pb2.Complex()
    message.one_dummy.id = 42
    message.one_dummy.name = "My name"
    message.multiple_dummies.add(id=43, name="My name 2")
    message.multiple_dummies.add(id=44, name="My name 3")
    message.multiple_dummies.add(id=45, name="My name 4")
    return message


if __name__ == '__main__':
    # print(simple())
    print(complex())