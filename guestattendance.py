#application developed by managerclaire
def totalguests():
    guests_in = int(input("In-town guests invited: "))
    guests_out = int(input("Out-of-town guests invited: "))
    bridal_party = int(input("Bridal party: "))
    totalg = guests_in + guests_out + bridal_party
    attendance = .65*guests_out + .9*guests_in + bridal_party
    attendance = int(attendance)
    print("Approximately {} guests will attend.".format(attendance))
    pct_attend = (float(attendance)/float(totalg))*100
    print("Your attendance rate will be about {}%.".format(pct_attend))

totalguests()
