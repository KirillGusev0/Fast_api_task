# -*- coding: utf-8 -*-

# apps/project/repository.py
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete

from apps.project.models import Project


class ProjectRepository:
    
    async def create(self, db: AsyncSession, data) -> Project:
        """
        SQL:
        INSERT INTO projects (title, description, owner_id)
        VALUES (:title, :description, :owner_id)
        RETURNING *;
        """
        stmt = insert(Project).values(
            title=data.title,
            description=data.description,
            owner_id=data.owner_id
        ).returning(Project)

        result = await db.execute(stmt)
        project = result.scalar_one()
        await db.commit()
        return project

    async def get(self, db: AsyncSession, project_id: int) -> Optional[Project]:
        """
        SQL:
        SELECT * FROM projects WHERE id = :id LIMIT 1;
        """
        stmt = select(Project).where(Project.id == project_id)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_all_by_user(self, db: AsyncSession, user_id: int) -> List[Project]:
        """
        SQL:
        SELECT * FROM projects WHERE owner_id = :user_id ORDER BY created_at DESC;
        """
        stmt = select(Project).where(Project.owner_id == user_id).order_by(Project.created_at.desc())
        result = await db.execute(stmt)
        return result.scalars().all()

    async def update(self, db: AsyncSession, project_id: int, data) -> Optional[Project]:
        """
        SQL:
        UPDATE projects SET ... WHERE id = :id RETURNING *;
        """
        stmt = (
            update(Project)
            .where(Project.id == project_id)
            .values({k: v for k, v in data.dict(exclude_unset=True).items()})
            .returning(Project)
        )
        result = await db.execute(stmt)
        updated = result.scalar_one_or_none()
        await db.commit()
        return updated

    async def delete(self, db: AsyncSession, project_id: int) -> bool:
        """
        SQL:
        DELETE FROM projects WHERE id = :id;
        """
        stmt = delete(Project).where(Project.id == project_id)
        result = await db.execute(stmt)
        await db.commit()
        return result.rowcount > 0

