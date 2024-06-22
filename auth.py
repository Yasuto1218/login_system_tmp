from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models, schemas


# パスワードハッシュ値の設定
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# パスワードをハッシュ化
def get_password_hash(password):
    return pwd_context.hash(password)

# パスワードを検証
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# ユーザーの取得
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# ユーザーの作成
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ユーザの認証
def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email=email)
    if not user or not verify_password(password, user.hashed_password):
        return False
    return user