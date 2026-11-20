"""Health and readiness endpoints."""

from fastapi import APIRouter, Response

from codeshift_hr.api.deps import SettingsDep, StoreDep

router = APIRouter(tags=["health"])


@router.get("/health")
def health(settings: SettingsDep) -> dict[str, str]:
    """Liveness: confirms that the process is alive."""
    return {"status": "ok", "app": settings.app_name, "env": settings.app_env}


@router.get("/ready")
def ready(store: StoreDep, response: Response) -> dict:
    """Readiness: confirms that required records are available."""
    checks = {"records_loaded": store.ready}
    ok = all(checks.values())
    if not ok:
        response.status_code = 503
    return {"status": "ready" if ok else "not_ready", "checks": checks}
