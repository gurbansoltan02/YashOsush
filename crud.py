from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_, and_, asc, desc
from models import Users, EmployerProfile, EmployeeProfile, EmployerImage, EmployeeImage, Lessons, Portfolio, Courses
from upload_depends import upload_image, delete_uploaded_image, upload_lesson, delete_uploaded_lesson, upload_portfolio, delete_uploaded_portfolio 


def signUp(req, db: Session):
    user = db.query(Users).filter(
        or_(
            Users.username == req.username,
            Users.email == req.email
        )
    ).first()
    if user:
        return False
    new_add = Users(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True 


def signIn(req, db: Session):
    user = db.query(Users).filter(
        and_(
            or_(
                Users.username == req.email,
                Users.email == req.email
            ),
            Users.password == req.password 
        )
    ).first()
    if user:
        return True


def read_users(db: Session):
    result = db.query(
        Users.user_type,
        Users.username,
        Users.email
    ).all()
    return result


# def read_employees(db: Session):
#     result = db.query(
#         Users.username,
#         Users.email,
#         Users.description
#     ).filter(Users.user_type == 2).all()
#     return result 


# def read_employers(db: Session):
#     result = db.query(
#         Users.username,
#         Users.email,
#         Users.description
#     ).filter(Users.user_type == 1).all()
#     return result 


def create_employer_profile(req, db: Session):
    new_add = EmployerProfile(
        user_id = req.user_id,
        full_name = req.full_name,
        description = req.description
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_employer_profile(db: Session):
    result = db.query(
        EmployerProfile,
        Users.email,
        Users.username
    ).options(joinedload(EmployerProfile.image).load_only('img'))\
        .join(Users, Users.id == EmployerProfile.user_id).all()
    return result


def create_employee_profile(req, db: Session):
    new_add = EmployeeProfile(
        user_id = req.user_id,
        full_name = req.full_name,
        description = req.description,
        phone_number = req.phone_number
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_employee_profile(db: Session):
    result = db.query(
        EmployeeProfile,
        Users.email,
        Users.username
    ).options(joinedload(EmployeeProfile.image).load_only('img'))\
        .options(joinedload(EmployeeProfile.portfolio).load_only('file'))\
            .join(Users, Users.id == EmployeeProfile.user_id).all()
    return result


def create_employer_image(id, file, db: Session):
    uploaded_img_name = upload_image('profile', file)
    new_add = EmployerImage(
        img = uploaded_img_name,
        employer_id = id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def delete_employer_image(id, db: Session):
    image = db.query(EmployerImage).filter(EmployerImage.id == id).first()
    if image.img:
        delete_uploaded_image(image_name=image.img)
        db.query(EmployerImage).filter(EmployerImage.id == id)\
            .delete(synchronize_session=False)
        db.commit()
    return True


def create_employee_image(id, file, db: Session):
    uploaded_img_name = upload_image('profile', file)
    new_add = EmployeeImage(
        img = uploaded_img_name,
        employee_id = id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def delete_employee_image(id, db: Session):
    image = db.query(EmployeeImage).filter(EmployeeImage.id == id).first()
    if image.img:
        delete_uploaded_image(image_name=image.img)
        db.query(EmployeeImage).filter(EmployeeImage.id == id)\
            .delete(synchronize_session=False)
        db.commit()
    return True


def create_portfolio(id, file, db: Session):
    uploaded_name = upload_portfolio('portfolio', file)
    new_add = Portfolio(
        file = uploaded_name,
        employee_id = id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def delete_portfolio(id, db: Session):
    file = db.query(Portfolio).filter(Portfolio.id == id).first()
    if file.file:
        delete_uploaded_portfolio(portfolio_name=file.file)
        db.query(Portfolio).filter(Portfolio.id == id)\
            .delete(synchronize_session=False)
        db.commit()
    return True


def create_course(req, db: Session):
    new_add = Courses(
        name = req.name
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_course(db: Session):
    result = db.query(Courses).all()
    return result


def create_lesson(id, file, db: Session):
    uploaded_name = upload_lesson('lessons', file)
    new_add = Lessons(
        lesson = uploaded_name,
        course_id = id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add


def read_lesson(page, limit, db: Session):
    result = db.query(Lessons)\
        .order_by(desc(Lessons.create_at))\
            .offset((page - 1) * limit)\
                .limit(limit)\
                    .all()
    return result

    
def delete_lesson(id, db: Session):
    lesson = db.query(Lessons).filter(Lessons.id == id).first()
    if lesson.lesson:
        delete_uploaded_lesson(lesson_name=lesson.lesson)
        db.query(Lessons).filter(Lessons.id == id)\
            .delete(synchronize_session=False)
        db.commit()
    return True

