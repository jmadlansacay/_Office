

from attend_main.models import MainAccountsAccountDetails

def getuname(request):
    # uname = request.META["REMOTE_USER"]
    # uname = uname.replace('MHI\\','')
    # uname='U303148' # Project Lead
    uname ='Q034800' # Designer
    # uname = 'Q034800'
    return(uname)


def getuserdetail(request):
    usr = getuname(request)
    udetail ={}
    if len(MainAccountsAccountDetails.objects.using('main').filter(mhi_id=usr)) == 0:
        return ('')
    else:
        a = MainAccountsAccountDetails.objects.using('main').get(mhi_id=usr)
        udetail.update({'uid' : a.mhi_id})
        udetail.update({'uname' : a.last_name+', '+a.first_name})
        udetail.update({'uccess' : a.access})
        udetail.update({'pic' : a.picture_file})
        # udetail = [{'uid' : a.mhi_id},{'uname' : a.last_name+', '+a.first_name}]
        return(udetail)


