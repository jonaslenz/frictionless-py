from __future__ import annotations

from typing import Any, Optional

from fastapi import Request
from pydantic import BaseModel

from ...project import Project
from ...router import router


class Props(BaseModel):
    path: str
    data: Optional[Any] = None
    toPath: Optional[str] = None


class Result(BaseModel):
    path: str


@router.post("/package/patch")
def endpoint(request: Request, props: Props) -> Result:
    return action(request.app.get_project(), props)


def action(project: Project, props: Props) -> Result:
    from ... import endpoints

    # Base patch
    result = endpoints.json.patch.action(
        project,
        endpoints.json.patch.Props(
            path=props.path,
            data=props.data,
            toPath=props.toPath,
        ),
    )

    # Update records
    # TODO: update records based on package.resources

    return Result(path=result.path)
