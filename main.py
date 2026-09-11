distance_mi = 5
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True
if distance_mi:
    print('False')
if distance_mi <= 1 and is_raining != True:
    print('True')
elif distance_mi <= 6 and has_bike == True and is_raining != True :
        print('True')
elif distance_mi > 6 and (has_car == True or has_ride_share_app == True) :
    print('True')
else:
    print('False')




