class Queue:
    """
    This class implement the Queue with 2 stacks, and 2 functions.
    :param stack_int only for take in
    :param stack_out only for take out
    """
    def __init__(self):

        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if not self.stack_out:
            if not self.stack_in:
                # stack_in and stack_out both empty
                return -1
            else:
                # pop data from stack_in to stack_out
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()
