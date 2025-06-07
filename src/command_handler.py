class CommandHandler(object):
    def __init__(self, database):
        self.database = database

    def handle_command(self, command):
        command_parts = command.strip().split()
        if not command_parts:
            return "Error: No command provided"

        cmd = command_parts[0].lower()
        args = command_parts[1:]

        if cmd == "set":
            return self._handle_set(args)
        elif cmd == "get":
            return self._handle_get(args)
        elif cmd == "delete":
            return self._handle_delete(args)
        else:
            return f"Error: Unknown command '{cmd}'"

    def _handle_set(self, args):
        if len(args) != 2:
            return "Error: SET command requires 2 arguments"
        key, value = args
        self.database.set(key, value)
        return "OK"

    def _handle_get(self, args):
        if len(args) != 1:
            return "Error: GET command requires 1 argument"
        key = args[0]
        value = self.database.get(key)
        return value if value is not None else "nil"

    def _handle_delete(self, args):
        if len(args) != 1:
            return "Error: DELETE command requires 1 argument"
        key = args[0]
        self.database.delete(key)
        return "OK"