from djangotailoring.subjects import DjangoSubjectLoader
from mydata4.models import Source1

class ECoachSubjectLoader(DjangoSubjectLoader):
    sources = {
        #'MTS_SOURCE_NAME': MODEL_OBJECT_CLASS ... the table name should matche the class name
        'Source1': Source1,
    }


