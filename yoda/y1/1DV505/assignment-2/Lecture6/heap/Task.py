class Task:
    addition_time = 0

    def __init__(self, priority, description):
        if isinstance(priority, int) and isinstance(description, str):
            self.priority = priority
            self.description = description
        else:
            raise TypeError("Priority has to be a integer and description has"
                            " to be string type")
        # used to compare if the priority are the same the insertion time
        # gets brought in
        self.addition_time = Task.addition_time
        Task.addition_time += 1

    def __str__(self):
        return f"{self.priority} {self.description}"

    def __gt__(self, new):
        if not isinstance(new, Task):
            raise TypeError("Comparison has to be between two Task objects")
        # edge case if they are the same priority the insertion time is
        # compared
        if new.priority == self.priority:
            return new.addition_time > self.addition_time
        return new.priority < self.priority

    def __ge__(self, new):
        if not isinstance(new, Task):
            raise TypeError("Comparison has to be between two Task objects")
        if new.priority == self.priority:
            return new.addition_time > self.addition_time
        return self.priority >= new.priority
