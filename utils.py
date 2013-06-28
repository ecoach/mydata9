from django.contrib.auth.models import User
from .models import Source1

def configure_source_data(username):
    # THIS IS A HACK TO ENSURE ALL THE ENTRY POINTS ADD THE RIGHT SOURCE ROW FOR A USER

    # ensure the user entry
    me = User.objects.filter(username=username)
    if len(me) < 1:
        me = User(username=username)
        me.save() 
        #return False
    else:
        me = me[0]

    # ensure the source entry
    ss = Source1.objects.filter(user_id=me)
    if len(ss) < 1:
        # After the enrollment period add a copy of Albert Einstein's data to non-enrolled users 
        ss = Source1(user_id=me)
        ss.save()
        return True
    else:
        # user already has source data - len(ss) should always be == 1
        return False
         
            
 
