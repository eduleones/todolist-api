from http import HTTPStatus

from fastapi import APIRouter, Response

router = APIRouter()


@router.get(
    "/healthcheck",
    status_code=HTTPStatus.OK,
)
async def healthcheck():
    return Response(status_code=HTTPStatus.OK, content="OK")
