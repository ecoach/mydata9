from djangotailoring.subjects import DjangoSubjectLoader
from mydata1.models import S_12Data

class ECoachSubjectLoader(DjangoSubjectLoader):
    sources = {
        #'MTS_SOURCE_NAME': MODEL_OBJECT_CLASS ... the table name should matche the class name
        'S_12': S_12Data,
    }


