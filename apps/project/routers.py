# -*- coding: utf-8 -*-
# apps/project/routers.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from apps.project.schemas import (
    ProjectCreate, ProjectRead, ProjectUpdate
)
from apps.project.services import ProjectService

router = APIRouter(prefix="/projects", tags=["projects"])
service = ProjectService()


@router.post("/", response_model=ProjectRead)
async def create_project(data: ProjectCreate, db: AsyncSession = Depends(get_db)):
    project = await service.create_project(db, data)
    return project


@router.get("/{project_id}", response_model=ProjectRead)
async def get_project(project_id: int, db: AsyncSession = Depends(get_db)):
    project = await service.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/user/{user_id}", response_model=list[ProjectRead])
async def get_projects_for_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await service.get_user_projects(db, user_id)


@router.patch("/{project_id}", response_model=ProjectRead)
async def update_project(project_id: int, data: ProjectUpdate, db: AsyncSession = Depends(get_db)):
    updated = await service.update_project(db, project_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: int, db: AsyncSession = Depends(get_db)):
    ok = await service.delete_project(db, project_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Project not found")
    return
