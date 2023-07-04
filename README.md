# Argument

Custom argument parsing class.

## Usage

`program = Argument()`

`program.add(label="-a", long="", range=(), type=str, target=lambda _: _, required=True, default=None, message="")`

`result = program.parse()`

- A parsing program is created by calling the class itself.
- Then any argument can be added by _.add()_ method.
- result is a dictionary returned by the .parse() method.
- Target expects function names.
- When range is specified, type is always set to str.

Default values for the arguments are exactly as stated above.
_long_ is to be used as another name for the added argument
(e.g. "--argument"). But it is not implemented yet.
