import strawberry
import typing
from strawberry.types import Info
from . import types
from . import queries
from . import mutations
from strawberry.permission import BasePermission
from common.permissions import OnlyLoggedIn


@strawberry.type
class Query:
    all_rooms: typing.List[types.RoomType] = strawberry.field(
        resolver=queries.get_all_rooms,
        permission_classes=[OnlyLoggedIn],
    )
    room: typing.Optional[types.RoomType] = strawberry.field(
        resolver=queries.get_room,
    )


@strawberry.type
class Mutation:
    room: typing.Optional[types.RoomType] = strawberry.mutation(
        resolver=mutations.add_room,
        permission_classes=[OnlyLoggedIn],
    )
