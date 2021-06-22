


def getuname(request):
    uname = request.META["REMOTE_USER"]
    uname = uname.replace('MHI\\','')
    # uname='U303148' # Project Lead
    # uname ='U303122' # Designer
    # uname = 'Q034800'
    return(uname)