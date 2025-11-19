# -*- coding: utf-8 -*-

# apps/project/services.py
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from apps.project.repository import ProjectRepository
from apps.project.schemas import ProjectCreate, ProjectUpdate
from apps.project.models import Project


class ProjectService:
    

    def __init__(self):
        self.repo = ProjectRepository()

    async def create_project(self, db: AsyncSession, data: ProjectCreate) -> Project:
        return await self.repo.create(db, data)

    async def get_project(self, db: AsyncSession, project_id: int) -> Optional[Project]:
        return await self.repo.get(db, project_id)

    async def get_user_projects(self, db: AsyncSession, user_id: int) -> List[Project]:
        return await self.repo.get_all_by_user(db, user_id)

    async def update_project(self, db: AsyncSession, project_id: int, data: ProjectUpdate) -> Optional[Project]:
        return await self.repo.update(db, project_id, data)

    async def delete_project(self, db: AsyncSession, project_id: int) -> bool:
        return await self.repo.delete(db, project_id)
