distance_mi = 5
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True
if distance_mi:
    if distance_mi <= 1 and not is_raining:
        print('True')
    elif distance_mi <= 6 :
        if has_bike and not is_raining:
            print('True')
        else:
            print('False')
    elif has_car or has_ride_share_app:
        print('True')
    else:
        print('False')
else:
    print('False')