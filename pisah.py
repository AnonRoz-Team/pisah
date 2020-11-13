import sys,os
try:
	for site in open(sys.argv[1]).read().splitlines():
		try:
#			if 'google' and 'suspendedpage' in site:continue
#			p=site.replace('https://www.google.com/url?sa=t&source=web&rct=j&url=','').split('&')[0]
			_p=site.split('/')[0]+'//'+site.split('/')[2]
			open('.p','a+').write(_p+'\n')
		except:continue
	podo=[]
	for site2 in open('.p').read().splitlines():
		try:
			if site2 in podo:continue
			else:print site2;podo.append(site2);open('p_'+sys.argv[1],'a+').write(site2+'\n')
		except:continue
	os.system('rm -rf .p')
	print '\nDone saved in p_'+sys.argv[1]
except IndexError:
	exit('use : python2 pisah.py list.txt')
