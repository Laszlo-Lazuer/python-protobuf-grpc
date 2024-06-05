import google.protobuf.json_format as json_format

import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2
import proto.enumerations_pb2 as enumerations_pb2
import proto.oneofs_pb2 as oneofs_pb2
import proto.maps_pb2 as maps_pb2
import proto.exercise_addressbook_pb2 as exercise_addressbook_pb2

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

def enums():
    return enumerations_pb2.Enumaration(
        eye_color=enumerations_pb2.EYE_COLOR_GREEN
        # eye_color=1 # could be by ordinal number but not readable
    )

def oneofs():
    # print element inside object
    message = oneofs_pb2.Result(message="a message")
    print(message)

    message.id = 42 # setting multiple times it will clear prior values
    print(message)

def maps():
    message = maps_pb2.MapExample();
    message.ids["myid"].id = 42
    message.ids["myid2"].id = 43
    message.ids["myid3"].id = 44
    print(message)

def file(message):
    path = "simple.bin"

    print("Write to file")
    print(message)
    with open(path, "wb") as f:
        bytes_as_str = message.SerializeToString()
        f.write(bytes_as_str)

    print("Read from file")
    with open(path, "rb") as f:
        t = type(message)
        message2 = t().FromString(f.read())
        print(message2)

def person():
    # Complex
    message = exercise_addressbook_pb2.AddressBook()
    # message.one_dummy.id = 42
    # message.one_dummy.name = "My name"
    message.people.add(id=43, name="My name 2", email="bob@aol.com")
    message.people.add(id=44, name="My name 3", email="bob2@aol.com")
    message.people.add(id=45, name="My name 4", email="bob3@aol.com")
    return message

    #
    # return exercise_addressbook_pb2.Person(
    #     id=42,
    #     is_simple=True,
    #     name="My name",
    #     sample_lists=[1,2,3]
    # )

def file_address(message):
    path = "phonebook.bin"

    print("Write to file")
    print(message)
    with open(path, "wb") as f:
        bytes_as_str = message.SerializeToString()
        f.write(bytes_as_str)

    print("Read from file")
    with open(path, "rb") as f:
        t = type(message)
        message2 = t().FromString(f.read())
        print(message2)

def to_json(message):
    return json_format.MessageToJson(
        message,
        indent=None, # disable pretty print
        preserving_proto_field_name=True, # Maintains snake case
        )

def from_json(json_str, type):
    return json_format.Parse(
        json_str,
        type(),
        ignore_unknown_fields=True # Ignore fields unknown to the message.
        )

if __name__ == '__main__':
    # print(simple())
    # print(complex())
    # print(enums())
    # print(oneofs())
    # print(maps())
    # file(simple())
    # json_str = to_json(complex())
    # print(from_json('{"id":42, "unknown": "test"}', simple_pb2.Simple)) # serialization
    # print(from_json(json_str, complex_pb2.Complex)) #deserialized from json
    file_address(person())

