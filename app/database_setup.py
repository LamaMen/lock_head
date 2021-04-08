from sqlalchemy import Column, ForeignKey, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TechTask(Base):
    __tablename__ = 'tech_task'

    tech_task_id = Column(String(250), nullable=False, primary_key=True)


class Boxes(Base):
    __tablename__ = 'boxes'

    box_id = Column(Integer, nullable=False, primary_key=True)
    tech_task_id = Column(String(250), ForeignKey('tech_task.tech_task_id'))


engine = create_engine('sqlite:///boxes-equals.db')

Base.metadata.create_all(engine)
