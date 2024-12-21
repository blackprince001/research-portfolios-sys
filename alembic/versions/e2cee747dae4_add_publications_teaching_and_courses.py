"""add_publications_teaching_and_courses

Revision ID: e2cee747dae4
Revises: bc81747ee6ae
Create Date: 2024-12-20 {timestamp}

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e2cee747dae4"
down_revision: Union[str, None] = "bc81747ee6ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create publications table
    op.create_table(
        "publications",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("abstract", sa.String(), nullable=False),
        sa.Column("authors", sa.String(), nullable=False),
        sa.Column("publication_type", sa.String(), nullable=False),
        sa.Column("journal", sa.String(), nullable=True),
        sa.Column("conference", sa.String(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("doi", sa.String(), nullable=True),
        sa.Column("url", sa.String(), nullable=True),
        sa.Column("pdf_link", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_publication_user_id", ondelete="CASCADE"
        ),
    )
    # Create index for faster user publication lookups
    op.create_index("idx_publication_user_id", "publications", ["user_id"])

    # Create teaching experiences table
    op.create_table(
        "teaching_experiences",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("institution", sa.String(), nullable=False),
        sa.Column("position", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("start_date", sa.String(), nullable=False),
        sa.Column("end_date", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_teaching_user_id", ondelete="CASCADE"
        ),
    )
    # Create index for faster user teaching lookups
    op.create_index("idx_teaching_user_id", "teaching_experiences", ["user_id"])

    # Create courses table
    op.create_table(
        "courses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("teaching_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["teaching_id"],
            ["teaching_experiences.id"],
            name="fk_course_teaching_id",
            ondelete="CASCADE",
        ),
    )
    # Create index for faster teaching course lookups
    op.create_index("idx_course_teaching_id", "courses", ["teaching_id"])


def downgrade() -> None:
    # Drop tables in reverse order of creation to handle dependencies
    # Drop indices first
    op.drop_index("idx_course_teaching_id", table_name="courses")
    op.drop_index("idx_teaching_user_id", table_name="teaching_experiences")
    op.drop_index("idx_publication_user_id", table_name="publications")

    # Drop tables
    op.drop_table("courses")
    op.drop_table("teaching_experiences")
    op.drop_table("publications")
