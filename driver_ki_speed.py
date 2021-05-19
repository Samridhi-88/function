def driver_speed(speed):
	a=speed-70
	point=a//5,   
	if speed<70:
		print('ok')
	if speed>70:
		if point<=12:
			print('point:',point)
	if point>12:
		print('license suspended ')
speed=int(input('enter the number'))
driver_speed(speed)                      

# driver speed