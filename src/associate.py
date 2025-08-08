#to build out the associate class and ID's



# information that needs to be pulled for main.py
# associate name = asssociate_name
# associate ID = associate_id
# assocaite job titlte = job_title


## creating a class for the associate
class Associate:
    ## defining the variables that will be used in the class
    ## these will be used to pull information from the associate class
    employee_name =  ""
    employee_id = ""
    certlevel = ""
    zone = ""
    job_title = ""
    ## constructor to initialize the associate class with the required attributes
    def __init__(self, employee_name, employee_id, certlevel, zone, job_title):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.certlevel = certlevel
        self.zone = zone
        self.job_title = job_title
    ## method to return the associate
    def get_associate(self):
        return {
            "employee_name": self.employee_name,
            "employee_id": self.employee_id,
            "certlevel": self.certlevel,
            "zone": self.zone,
            "job_title": self.job_title
        }
