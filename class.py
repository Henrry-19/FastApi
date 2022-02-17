from pydantic import BaseModel

class House(BaseModel): 
    age: float
    mother_education: float
    father_education: float
    commute_time: float
    study_time: float
    failures: float
    family_quality: float
    free_time: float
    go_out: float
    weekday_alcohol_usage: float
    weekend_alcohol_usage: float
    health: float
    absences: float
    period1_score: float
    period2_score: float
    school_GP: float
    school_MS: float

    sex_F: float
    sex_M: float
    address_Rural: float
    address_Urban: float
    family_size_GT3: float

    family_size_LE3: float
    parents_status_A: float
    parents_status_T: float
    mother_job_at_home: float
    mother_job_health: float

    mother_job_other: float
    mother_job_services: float
    mother_job_teacher: float
    father_job_at_home: float
    father_job_health: float



    father_job_other: float
    father_job_services: float
    father_job_teacher: float
    reason_course: float
    reason_home: float


    reason_other: float
    reason_reputation: float
    guardian_father: float
    guardian_mother: float
    guardian_other: float

    school_support_no: float
    school_support_yes: float
    family_support_no: float
    family_support_yes: float
    paid_classes_no: float
    paid_classes_yes: float


    activities_no: float
    activities_yes: float
    nursery_no: float
    nursery_yes	: float
    desire_higher_edu_no: float
    desire_higher_edu_yes: float

    internet_no: float
    internet_yes	: float
    romantic_no: float
    romantic_yes: float



    class Config:
        schema_extra = {
            "age": 3.14,
            "mother_education":3.14,
            "father_education":3.14,
            "commute_time": 3.14,
            "study_time": 3.14,
            "failures": 3.14,
            "family_quality": 3.14,
            "free_time": 3.14,
            "go_out": 3.14,
            "weekday_alcohol_usage": 3.14,
            "weekend_alcohol_usage": 3.14,
            "health": 3.14,
            "absences": 3.14,
            "period1_score": 3.14,
            "period2_score": 3.14,
            "school_GP": 3.14,
            "school_MS": 3.14,


            "sex_F": 3.14,
            "sex_M": 3.14,
            "address_Rural": 3.14,
            "address_Urban": 3.14,
            "family_size_GT3":3.14,

            "family_size_LE3":3.14,
            "parents_status_A": 3.14,
            "parents_status_T": 3.14,
            "mother_job_at_home":3.14,
            "mother_job_health": 3.14,

            "mother_job_other": 3.14,
            "mother_job_services": 3.14,
            "mother_job_teacher": 3.14,
            "father_job_at_home": 3.14,
            "father_job_health": 3.14,



            "father_job_other": 3.14,
            "father_job_services": 3.14,
            "father_job_teacher": 3.14,
            "reason_course": 3.14,
            "reason_home": 3.14,


            "reason_other":3.14,
            "reason_reputation": 3.14,
            "guardian_father": 3.14,
            "guardian_mother": 3.14,
            "guardian_other": 3.14,

            "school_support_no": 3.14,
            "school_support_yes": 3.14,
            "family_support_no": 3.14,
            "family_support_yes": 3.14,
            "paid_classes_no": 3.14,
            "paid_classes_yes": 3.14,


            "activities_no": 3.14,
            "activities_yes": 3.14,
            "nursery_no": 3.14,
            "nursery_yes": 3.14,
            "desire_higher_edu_no": 3.14,
            "desire_higher_edu_yes": 3.14,

            "internet_no": 3.14,
            "internet_yes": 3.14,
            "romantic_no": 3.14,
            "romantic_yes": 3.14
, 
        }
