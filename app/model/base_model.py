from datetime import datetime
import re
import pytz
from sqlalchemy import Column, DateTime, func, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy.ext.declarative import declarative_base


def resolve_table_name(name: str) -> str:
    names = re.split("(?=[A-Z])", name)
    return "_".join([x.lower() for x in names if x])


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self):
        return resolve_table_name(self.__name__)

    id: Mapped[int] = mapped_column(primary_key=True, index=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), default=datetime.utcnow
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )


class User(Base):
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False, unique=True)
    user_token: Mapped[str] = mapped_column(nullable=False, unique=True)

    name: Mapped[str] = mapped_column(default="", nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)


Base2 = declarative_base()

class MyModel(Base2):
    __tablename__ = 'mymodel'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(DateTime(timezone=True), default=datetime.now(pytz.utc))


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("sqlite:///:memory:", echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(User(email="test@test.com", password="test", user_token="test"))
    session.commit()
    print(session.query(User).all())
    user = session.query(User).first()
    print(user.__dict__)
    print(user.created_at)
    print(user.updated_at)
    import pytz
    created_at = user.created_at.astimezone(pytz.timezone("Asia/Seoul"))
    print(created_at)


    # create tables
    Base2.metadata.create_all(engine)
    session.add(MyModel(name="test"))
    session.commit()
    print(session.query(MyModel).all())
    mymodel = session.query(MyModel).first()
    print(mymodel.__dict__)
    print(mymodel.created_at)

