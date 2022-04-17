# local
from ivy.container.base import ContainerBase

# ToDo: implement all methods here as public instance methods


# noinspection PyMissingConstructor
class ContainerWithSearching(ContainerBase):

    def __init__(self):
        import ivy.functional.ivy.searching as searching
        ContainerBase.add_instance_methods(self, searching)
