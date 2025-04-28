"""District Staff and Teacher Data

Revision ID: b5c8d9e7f3a1
Revises: a3b5d7c9e1f2
Create Date: 2024-08-15 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import logging
from datetime import datetime

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'b5c8d9e7f3a1'
down_revision = 'a3b5d7c9e1f2'
branch_labels = None
depends_on = None


def upgrade():
    """Create tables for district staff and teacher-related data."""
    
    # Create school_staff_type table (renamed from staff-type to follow naming conventions)
    op.execute("""
        CREATE TABLE school_staff_type (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Insert school staff type data
    op.execute("""
        INSERT INTO school_staff_type (name, date_created, date_updated) VALUES
        ('Teacher', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Instruction Support', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Librarian', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Specialist', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Admin Support', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('All Other Support', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    """)
    
    # Create district_staff table
    op.execute("""
        CREATE TABLE district_staff (
            id SERIAL PRIMARY KEY,
            school_staff_type_id_fk INTEGER NOT NULL,
            district_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            value NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_district_staff_type
                FOREIGN KEY (school_staff_type_id_fk)
                REFERENCES school_staff_type(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_district_staff_district
                FOREIGN KEY (district_id_fk)
                REFERENCES district(id)
                ON DELETE CASCADE,
            CONSTRAINT unique_district_staff
                UNIQUE (school_staff_type_id_fk, district_id_fk, year)
        )
    """)
    
    # Create indices for district_staff
    op.execute("""
        CREATE INDEX idx_district_staff_district_id 
        ON district_staff (district_id_fk)
    """)
    
    op.execute("""
        CREATE INDEX idx_district_staff_year 
        ON district_staff (year)
    """)
    
    op.execute("""
        CREATE INDEX idx_district_staff_type 
        ON district_staff (school_staff_type_id_fk)
    """)
    
    # Create state_staff table
    op.execute("""
        CREATE TABLE state_staff (
            id SERIAL PRIMARY KEY,
            school_staff_type_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            value NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_state_staff_type
                FOREIGN KEY (school_staff_type_id_fk)
                REFERENCES school_staff_type(id)
                ON DELETE CASCADE,
            CONSTRAINT unique_state_staff
                UNIQUE (school_staff_type_id_fk, year)
        )
    """)
    
    # Create indices for state_staff
    op.execute("""
        CREATE INDEX idx_state_staff_year 
        ON state_staff (year)
    """)
    
    op.execute("""
        CREATE INDEX idx_state_staff_type 
        ON state_staff (school_staff_type_id_fk)
    """)
    
    # Create teacher_education_type table
    op.execute("""
        CREATE TABLE teacher_education_type (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Insert teacher education type data
    op.execute("""
        INSERT INTO teacher_education_type (name, date_created, date_updated) VALUES
        ('None', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Bachelor', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Masters', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('Beyond Masters', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    """)
    
    # Create district_teacher_education table
    op.execute("""
        CREATE TABLE district_teacher_education (
            id SERIAL PRIMARY KEY,
            teacher_type_id_fk INTEGER NOT NULL,
            district_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            value NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_district_teacher_education_type
                FOREIGN KEY (teacher_type_id_fk)
                REFERENCES teacher_education_type(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_district_teacher_education_district
                FOREIGN KEY (district_id_fk)
                REFERENCES district(id)
                ON DELETE CASCADE,
            CONSTRAINT unique_district_teacher_education
                UNIQUE (teacher_type_id_fk, district_id_fk, year)
        )
    """)
    
    # Create indices for district_teacher_education
    op.execute("""
        CREATE INDEX idx_district_teacher_education_district_id 
        ON district_teacher_education (district_id_fk)
    """)
    
    op.execute("""
        CREATE INDEX idx_district_teacher_education_year 
        ON district_teacher_education (year)
    """)
    
    op.execute("""
        CREATE INDEX idx_district_teacher_education_type 
        ON district_teacher_education (teacher_type_id_fk)
    """)
    
    # Create state_teacher_education table
    op.execute("""
        CREATE TABLE state_teacher_education (
            id SERIAL PRIMARY KEY,
            teacher_type_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            value NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_state_teacher_education_type
                FOREIGN KEY (teacher_type_id_fk)
                REFERENCES teacher_education_type(id)
                ON DELETE CASCADE,
            CONSTRAINT unique_state_teacher_education
                UNIQUE (teacher_type_id_fk, year)
        )
    """)
    
    # Create indices for state_teacher_education
    op.execute("""
        CREATE INDEX idx_state_teacher_education_year 
        ON state_teacher_education (year)
    """)
    
    op.execute("""
        CREATE INDEX idx_state_teacher_education_type 
        ON state_teacher_education (teacher_type_id_fk)
    """)
    
    # Create district_teacher_average_salary table
    op.execute("""
        CREATE TABLE district_teacher_average_salary (
            id SERIAL PRIMARY KEY,
            district_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            salary NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_district_teacher_average_salary_district
                FOREIGN KEY (district_id_fk)
                REFERENCES district(id)
                ON DELETE CASCADE,
            CONSTRAINT unique_district_teacher_average_salary
                UNIQUE (district_id_fk, year)
        )
    """)
    
    # Create indices for district_teacher_average_salary
    op.execute("""
        CREATE INDEX idx_district_teacher_average_salary_district_id 
        ON district_teacher_average_salary (district_id_fk)
    """)
    
    op.execute("""
        CREATE INDEX idx_district_teacher_average_salary_year 
        ON district_teacher_average_salary (year)
    """)
    
    # Create state_teacher_average_salary table
    op.execute("""
        CREATE TABLE state_teacher_average_salary (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            salary NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_state_teacher_average_salary
                UNIQUE (year)
        )
    """)
    
    # Create index for state_teacher_average_salary
    op.execute("""
        CREATE INDEX idx_state_teacher_average_salary_year 
        ON state_teacher_average_salary (year)
    """)
    
    # Create teacher_salary_band_type table
    op.execute("""
        CREATE TABLE teacher_salary_band_type (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Insert teacher salary band type data
    op.execute("""
        INSERT INTO teacher_salary_band_type (name, description, date_created, date_updated) VALUES
        ('BA', 'Bachelors', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('BA15', 'Bachelors + 15 credits', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('BA30', 'Bachelors + 30 credits', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('MA', 'Masters', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('MA15', 'Masters + 15 credits', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
        ('MA30', 'Masters + 30 credits', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    """)
    
    # Create district_teacher_salary_band table
    op.execute("""
        CREATE TABLE district_teacher_salary_band (
            id SERIAL PRIMARY KEY,
            district_id_fk INTEGER NOT NULL,
            teacher_salary_band_type_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            min_salary NUMERIC(15,2),
            max_salary NUMERIC(15,2),
            steps INTEGER,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_district_teacher_salary_band_district
                FOREIGN KEY (district_id_fk)
                REFERENCES district(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_district_teacher_salary_band_type
                FOREIGN KEY (teacher_salary_band_type_id_fk)
                REFERENCES teacher_salary_band_type(id)
                ON DELETE CASCADE,
            CONSTRAINT unique_district_teacher_salary_band
                UNIQUE (district_id_fk, teacher_salary_band_type_id_fk, year)
        )
    """)
    
    # Create indices for district_teacher_salary_band
    op.execute("""
        CREATE INDEX idx_district_teacher_salary_band_district_id 
        ON district_teacher_salary_band (district_id_fk)
    """)
    
    op.execute("""
        CREATE INDEX idx_district_teacher_salary_band_year 
        ON district_teacher_salary_band (year)
    """)
    
    op.execute("""
        CREATE INDEX idx_district_teacher_salary_band_type 
        ON district_teacher_salary_band (teacher_salary_band_type_id_fk)
    """)


def downgrade():
    """Remove tables for district staff and teacher-related data."""
    
    # Drop tables in reverse order of creation to respect foreign key constraints
    op.execute("DROP TABLE IF EXISTS district_teacher_salary_band")
    
    op.execute("DROP TABLE IF EXISTS teacher_salary_band_type")
    
    op.execute("DROP TABLE IF EXISTS district_teacher_average_salary")
    
    op.execute("DROP TABLE IF EXISTS state_teacher_average_salary")
    
    op.execute("DROP TABLE IF EXISTS district_teacher_education")
    
    op.execute("DROP TABLE IF EXISTS state_teacher_education")
    
    op.execute("DROP TABLE IF EXISTS teacher_education_type")
    
    op.execute("DROP TABLE IF EXISTS district_staff")
    
    op.execute("DROP TABLE IF EXISTS state_staff")
    
    op.execute("DROP TABLE IF EXISTS school_staff_type") 