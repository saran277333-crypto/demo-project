"""FastAPI dependency injection helpers."""

from typing import Annotated

from fastapi import Depends, Request

from codeshift_hr.config import Settings
from codeshift_hr.store import RecordStore


def get_app_settings(request: Request) -> Settings:
    return request.app.state.settings


def get_store(request: Request) -> RecordStore:
    return request.app.state.store


SettingsDep = Annotated[Settings, Depends(get_app_settings)]
StoreDep = Annotated[RecordStore, Depends(get_store)]
