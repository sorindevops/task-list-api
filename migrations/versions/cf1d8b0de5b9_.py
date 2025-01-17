"""empty message

Revision ID: cf1d8b0de5b9
Revises: 
Create Date: 2022-11-11 18:24:46.976383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf1d8b0de5b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goal',
    sa.Column('goal_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('goal_id')
    )
    op.create_table('task',
    sa.Column('task_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=80), nullable=True),
    sa.Column('completed_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('task_id')
    )
    op.create_index(op.f('ix_task_completed_at'), 'task', ['completed_at'], unique=False)
    op.create_index(op.f('ix_task_description'), 'task', ['description'], unique=False)
    op.create_index(op.f('ix_task_title'), 'task', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_title'), table_name='task')
    op.drop_index(op.f('ix_task_description'), table_name='task')
    op.drop_index(op.f('ix_task_completed_at'), table_name='task')
    op.drop_table('task')
    op.drop_table('goal')
    # ### end Alembic commands ###
