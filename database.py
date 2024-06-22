from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# エンジンの作成
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

# セッションの作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラスの宣言
Base = declarative_base()