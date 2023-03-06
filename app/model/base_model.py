from datetime import datetime
import re
import pytz
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


def resolve_table_name(name: str) -> str:
    names = re.split("(?=[A-Z])", name)
    return "_".join([x.lower() for x in names if x])


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self):
        return resolve_table_name(self.__name__)

    id: int = mapped_column(primary_key=True, index=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now(), default=datetime.now(pytz.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        nullable=False,
        server_default=func.now(),
        default=datetime.now(pytz.utc),
        onupdate=datetime.now(pytz.utc),
    )


class User(Base):
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False, unique=True)
    user_token: Mapped[str] = mapped_column(nullable=False, unique=True)

    name: Mapped[str] = mapped_column(default="", nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("sqlite:///:memory:", echo=True)
    # postgres engine
    engine = create_engine("postgresql://damon:@localhost:5432/fca", echo=True)
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # session.add(User(email="test4@test.com", password="test4", user_token="test4"))
    # session.commit()
    # print(session.query(User).all())
    # user = session.query(User).first()
    # print(user.__dict__)
    # print(user.created_at)
    # print(user.updated_at)
    # import pytz
    #
    # print(user.created_at.astimezone(pytz.timezone("Asia/Seoul")))
    # print(user.created_at)
    # # print with timezone
    # print(user.created_at.astimezone())
    users = session.query(User).all()
    for user in users:
        print(user.created_at.astimezone(pytz.utc))
        print(user.updated_at)
        print(type(user.name))
        print(user.name.__dict__)
        # Mapped is not so good. it can't type tracking.
    # create tables
    # Base2.metadata.create_all(engine)
    # session.add(MyModel(name="test"))
    # session.commit()
    # print(session.query(MyModel).all())
    # mymodel = session.query(MyModel).first()
    # print(mymodel.__dict__)
    # print(mymodel.created_at)
    # print(mymodel.created_at.astimezone())
    # print(mymodel.created_at.astimezone(pytz.utc))
