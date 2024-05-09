from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from ..container import Container
from ..services.runner_service import RunnerService
from ..services.utils.exceptions_handler import ServiceException

router = APIRouter()


@router.get("/api/v1/runs")
@inject
def get_all_runners(
    runner_service: RunnerService = Depends(Provide[Container.runner_service]),
) -> list:
    """
    Retrieve all runners from the database.

    Args:
        runner_service (RunnerService): The service responsible for retrieving runners.

    Returns:
        list: A list of all runners.

    Raises:
        HTTPException: An error with status code 404 if no runners are found.
                       An error with status code 400 if there is a validation error.
                       An error with status code 500 for any other server-side error.
    """
    try:
        return runner_service.get_all_runner()
    except ServiceException as e:
        if e.error_code == "FileNotFound":
            raise HTTPException(
                status_code=404, detail=f"Failed to retrieve runners: {e.msg}"
            )
        elif e.error_code == "ValidationError":
            raise HTTPException(
                status_code=400, detail=f"Failed to retrieve runners: {e.msg}"
            )
        else:
            raise HTTPException(
                status_code=500, detail=f"Failed to retrieve runners: {e.msg}"
            )


@router.get("/api/v1/runs/name")
@inject
def get_all_runner_name(
    runner_service: RunnerService = Depends(Provide[Container.runner_service]),
) -> list:
    """
    Retrieve all runner names from the database.

    Args:
        runner_service (RunnerService): The service responsible for retrieving runner names.

    Returns:
        list: A list of all runner names.

    Raises:
        HTTPException: An error with status code 404 if no runner names are found.
                       An error with status code 400 if there is a validation error.
                       An error with status code 500 for any other server-side error.
    """
    try:
        return runner_service.get_all_runner_name()
    except ServiceException as e:
        if e.error_code == "FileNotFound":
            raise HTTPException(
                status_code=404, detail=f"Failed to retrieve runner names: {e.msg}"
            )
        elif e.error_code == "ValidationError":
            raise HTTPException(
                status_code=400, detail=f"Failed to retrieve runner names: {e.msg}"
            )
        else:
            raise HTTPException(
                status_code=500, detail=f"Failed to retrieve runner names: {e.msg}"
            )


@router.get("/api/v1/runs/{runner_id}")
@inject
def get_runner_by_id(
    runner_id: str,
    runner_service: RunnerService = Depends(Provide[Container.runner_service]),
) -> dict:
    """
    Retrieve a specific runner by their ID from the database.

    Args:
        runner_id (str): The unique identifier of the runner to retrieve.
        runner_service (RunnerService): The service responsible for retrieving the runner.

    Returns:
        dict: The runner information if found.

    Raises:
        HTTPException: An error with status code 404 if the runner is not found.
                       An error with status code 400 if there is a validation error.
                       An error with status code 500 for any other server-side error.
    """
    try:
        run = runner_service.get_runner_by_id(runner_id)
        return run
    except ServiceException as e:
        if e.error_code == "FileNotFound":
            raise HTTPException(
                status_code=404, detail=f"Failed to retrieve runner: {e.msg}"
            )
        elif e.error_code == "ValidationError":
            raise HTTPException(
                status_code=400, detail=f"Failed to retrieve runner: {e.msg}"
            )
        else:
            raise HTTPException(
                status_code=500, detail=f"Failed to retrieve runner: {e.msg}"
            )


@router.delete("/api/v1/runs/{runner_id}")
@inject
def delete_runner(
    runner_id: str,
    runner_service: RunnerService = Depends(Provide[Container.runner_service]),
) -> dict:
    """
    Delete a specific runner by their ID from the database.

    Args:
        runner_id (str): The unique identifier of the runner to delete.
        runner_service (RunnerService): The service responsible for deleting the runner.

    Returns:
        dict: A message indicating the successful deletion of the runner.

    Raises:
        HTTPException: An error with status code 404 if the runner is not found.
                       An error with status code 400 if there is a validation error.
                       An error with status code 500 for any other server-side error.
    """
    try:
        runner_service.delete_run(runner_id)
        return {"message": "Runner deleted successfully"}
    except ServiceException as e:
        if e.error_code == "FileNotFound":
            raise HTTPException(
                status_code=404, detail=f"Failed to delete runner: {e.msg}"
            )
        elif e.error_code == "ValidationError":
            raise HTTPException(
                status_code=400, detail=f"Failed to delete runner: {e.msg}"
            )
        else:
            raise HTTPException(
                status_code=500, detail=f"Failed to delete runner: {e.msg}"
            )
