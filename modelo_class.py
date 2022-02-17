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
            "example":{
                "age": 17,
                "mother_education":2,
                "father_education":2,
                "commute_time": 2,
                "study_time": 1,
                "failures": 0,
                "family_quality": 5,
                "free_time": 5,
                "go_out": 5,
                "weekday_alcohol_usage": 3,
                "weekend_alcohol_usage": 5,
                "health": 5,
                "absences": 0,
                "period1_score": 8,
                "period2_score": 13,
                "school_GP": 0,
                "school_MS": 1,


                "sex_F": 0,
                "sex_M": 1,
                "address_Rural": 1,
                "address_Urban": 0,
                "family_size_GT3":1,

                "family_size_LE3":0,
                "parents_status_A": 0,
                "parents_status_T": 1,
                "mother_job_at_home":0,
                "mother_job_health":0,

                "mother_job_other":1,
                "mother_job_services": 0,
                "mother_job_teacher": 0,
                "father_job_at_home": 0,
                "father_job_health": 0,



                "father_job_other": 1,
                "father_job_services": 0,
                "father_job_teacher": 0,
                "reason_course": 1,
                "reason_home":0,


                "reason_other":0,
                "reason_reputation":0,
                "guardian_father":0,
                "guardian_mother":1,
                "guardian_other":0,

                "school_support_no": 1,
                "school_support_yes": 0,
                "family_support_no": 1,
                "family_support_yes": 0,
                "paid_classes_no": 1,
                "paid_classes_yes":0,


                "activities_no":0,
                "activities_yes": 1,
                "nursery_no": 0,
                "nursery_yes": 1,
                "desire_higher_edu_no": 1,
                "desire_higher_edu_yes":0,

                "internet_no":1,
                "internet_yes":0,
                "romantic_no":0,
                "romantic_yes":1
            }
        }