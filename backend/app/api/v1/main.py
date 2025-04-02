from fastapi import APIRouter

from app.api.v1.routes import util, location, measurement, enrollment, finance

api_router = APIRouter()
api_router.include_router(location.router, prefix="/location", tags=["Location"])
api_router.include_router(measurement.router, prefix="/measurement", tags=["Measurement"])
api_router.include_router(enrollment.router, prefix="/enrollment", tags=["Enrollment"])
api_router.include_router(finance.router, prefix="/finance", tags=["Finance"])
api_router.include_router(util.router, prefix="/util", tags=["Utilities"])