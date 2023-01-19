alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position:" + str(alien_0['x_position']))
# run right.
# calculate the offset value based on the current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # the alien is moving fast
    x_increment = 3
# new position is equal to the sum of the old and the increment.

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position:" + str(alien_0['x_position']))
