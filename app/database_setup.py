from sqlalchemy import Column, ForeignKey, String, Integer, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TechTask(Base):
    __tablename__ = 'tech_task'

    tech_task_id = Column(String(250), nullable=False, primary_key=True)
    number = Column(Integer())


class Boxes(Base):
    __tablename__ = 'boxes'

    box_id = Column(Integer, nullable=False, primary_key=True)
    tech_task_id = Column(String(250), ForeignKey('tech_task.tech_task_id'))


class Logs(Base):
    __tablename__ = 'logs'

    log_id = Column(Integer, primary_key=True)
    worker = Column(String(100))
    date = Column(DateTime, nullable=False)
    tech_task_id = Column(String(250))


engine = create_engine('sqlite:///boxes-equals.db')

Base.metadata.create_all(engine)
